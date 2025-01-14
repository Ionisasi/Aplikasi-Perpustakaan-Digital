import os
import sqlite3
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QMessageBox, QPushButton,QDateEdit,QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QDate
from view.UI_HomePage import Ui_Form as Ui_HomePage

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class homePage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)

        # Menghubungkan fungsi untuk menampilkan buku ke scroll area
        self.display_random_books()

    def display_random_books(self):
        # Mendapatkan layout dari scroll area
        scroll_layout = self.ui.scrollAreaWidgetContents.layout()
        if scroll_layout is None:
            scroll_layout = QVBoxLayout()
            self.ui.scrollAreaWidgetContents.setLayout(scroll_layout)

        # Ambil 5 buku secara acak dari database
        try:
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, judul, cover FROM buku ORDER BY RANDOM() LIMIT 5")
                books = cursor.fetchall()

                # Untuk setiap buku, buat elemen dan tambahkan ke scroll layout
                for book in books:
                    book_id, title, cover = book
                    book_widget = self.create_book_widget(book_id, title, cover)
                    scroll_layout.addWidget(book_widget)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def create_book_widget(self, book_id, title, cover_path):
        widget = QWidget()
        layout = QVBoxLayout()

        cover_button = QPushButton(self)
        pixmap = QPixmap(cover_path)
        scaled_pixmap = pixmap.scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        cover_button.setIcon(scaled_pixmap)
        cover_button.setIconSize(scaled_pixmap.size())
        cover_button.setFixedSize(150, 200)
        cover_button.setStyleSheet("border: none;")

        cover_button.clicked.connect(lambda: self.show_book_info(book_id))

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setFixedWidth(150)
        title_label.setStyleSheet("color: white; font-weight: bold;")

        layout.addWidget(cover_button)
        layout.addWidget(title_label)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignCenter)
        widget.setLayout(layout)

        return widget

    def show_book_info(self, book_id):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT judul, tahun_terbit, pengarang, penerbit, kategori, jumlah FROM buku WHERE id = ?",
            (book_id,),
        )
        book = cursor.fetchone()
        conn.close()

        if book:
            title, year, author, publisher, category, quantity = book

            # Membuat dialog baru
            dialog = QDialog(self)
            dialog.setFixedSize(650,300)
            dialog.setWindowTitle("Informasi Buku dan Peminjaman")
            dialog.setModal(True)

            # Membuat layout untuk dialog
            layout = QVBoxLayout(dialog)

            # Informasi Buku
            info_label = QLabel(
                f"<b>Judul:</b> {title}<br>"
                f"<b>Tahun Terbit:</b> {year}<br>"
                f"<b>Pengarang:</b> {author}<br>"
                f"<b>Penerbit:</b> {publisher}<br>"
                f"<b>Kategori:</b> {category}<br>"
                f"<b>Jumlah Tersedia:</b> {quantity}"
            )
            info_label.setStyleSheet("font-size: 14px;")
            layout.addWidget(info_label)

            # Tanggal peminjaman (otomatis tanggal hari ini)
            borrow_date_label = QLabel("Tanggal Peminjaman:")
            layout.addWidget(borrow_date_label)

            borrow_date = QDateEdit(dialog)
            borrow_date.setDate(QDate.currentDate())
            borrow_date.setCalendarPopup(True)
            borrow_date.setEnabled(False)  # Tanggal peminjaman otomatis hari ini
            layout.addWidget(borrow_date)

            # Tanggal tenggat (user memilih)
            return_date_label = QLabel("Tanggal Tenggat Pengembalian:")
            layout.addWidget(return_date_label)

            return_date = QDateEdit(dialog)
            return_date.setDate(QDate.currentDate().addDays(7))  # Default 7 hari ke depan
            return_date.setCalendarPopup(True)
            return_date.setEnabled(False)
            layout.addWidget(return_date)

            # Tombol untuk melakukan peminjaman
            borrow_button = QPushButton("Pinjam", dialog)
            borrow_button.setStyleSheet("background-color: #007BFF; color: white; font-weight: bold;")
            layout.addWidget(borrow_button)

            # Fungsi untuk memproses peminjaman
            def process_borrow():
                if quantity > 0:  # Pastikan ada stok buku yang tersedia
                    # Tanggal peminjaman dan pengembalian
                    borrow_date_str = borrow_date.date().toString("yyyy-MM-dd")
                    return_date_str = return_date.date().toString("yyyy-MM-dd")

                    # Simpan ke database
                    conn = sqlite3.connect(database_path)
                    cursor = conn.cursor()

                    # Insert ke tabel peminjaman
                    cursor.execute(
                        "INSERT INTO peminjaman (tanggal_pinjam, tanggal_kembali, anggota_id) VALUES (?, ?, ?)",
                        (borrow_date_str, return_date_str, self.user_id),
                    )
                    peminjaman_id = cursor.lastrowid

                    # Insert ke tabel peminjaman_detail
                    cursor.execute(
                        "INSERT INTO peminjaman_detail (peminjaman_id, buku_id) VALUES (?, ?)",
                        (peminjaman_id, book_id),
                    )

                    # Update jumlah buku
                    cursor.execute(
                        "UPDATE buku SET jumlah = jumlah - 1 WHERE id = ?",
                        (book_id,),
                    )
                    conn.commit()
                    conn.close()

                    QMessageBox.information(dialog, "Berhasil", f"Buku berhasil dipinjam.")
                    dialog.accept()
                else:
                    QMessageBox.warning(dialog, "Gagal", "Buku tidak tersedia.")

            borrow_button.clicked.connect(process_borrow)

            # Tombol untuk menutup dialog
            close_button = QPushButton("Tutup", dialog)
            close_button.clicked.connect(dialog.reject)
            layout.addWidget(close_button)

            dialog.exec()
