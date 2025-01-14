import sqlite3
import os
from PySide6.QtCore import QTimer, QDate, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox, QDialog, QLineEdit, QDateEdit
from PySide6.QtGui import QPixmap
from datetime import datetime
from view.UI_KoleksiBuku import Ui_Form as Ui_KoleksiBuku

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class KoleksiBuku(QWidget):
    def __init__(self, kategori=None, ui_class=Ui_KoleksiBuku):
        super().__init__()
        self.kategori = kategori  # Kategori buku (Fiksi/Non Fiksi)
        self.ui = ui_class()
        self.ui.setupUi(self)  # Setup UI dari widget
        self.ui.headerTitle.setText(f"BUKU {kategori.upper() if kategori else 'SEMUA'}")
        
        self.books_displayed = set()  # Melacak buku yang telah ditampilkan
        self.setup_timer()  # Memulai pengamat database

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_new_books)
        self.timer.start(2000)  # Memeriksa setiap 2 detik

    def check_for_new_books(self):
        books = self.fetch_books()
        for book in books:
            book_id, title, cover_path = book
            if book_id not in self.books_displayed:
                self.add_book_to_display(book_id, title, cover_path)

        borrowed_books = self.fetch_borrowed_books()
        for book in borrowed_books:
            book_id, title, cover_path = book
            if book_id not in self.books_displayed:
                self.add_book_to_display(book_id, title, cover_path)

    def fetch_books(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        if self.kategori:
            cursor.execute("SELECT id, judul, cover FROM buku WHERE kategori = ?", (self.kategori,))
        else:
            cursor.execute("SELECT id, judul, cover FROM buku")  # Mengambil semua buku jika kategori None

        books = cursor.fetchall()
        conn.close()
        return books

    def fetch_borrowed_books(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Mengambil buku yang dipinjam
        cursor.execute("""
            SELECT b.id, b.judul, b.cover
            FROM peminjaman p
            JOIN peminjaman_detail pd ON p.id = pd.peminjaman_id
            JOIN buku b ON pd.buku_id = b.id
            WHERE p.tanggal_kembali IS NULL  -- Buku yang belum dikembalikan
        """)
        
        books = cursor.fetchall()
        conn.close()
        return books

    def add_book_to_display(self, book_id, title, cover_path):
        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        layout = self.ui.scrollAreaWidgetContents.layout()

        if layout.count() == 0 or layout.itemAt(layout.count() - 1).layout().count() >= 5:
            row_layout = QHBoxLayout()
            layout.addLayout(row_layout)

        row_layout = layout.itemAt(layout.count() - 1).layout()

        book_widget = self.create_book_widget(book_id, title, cover_path)
        row_layout.addWidget(book_widget)
        self.books_displayed.add(book_id)

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

            # Input untuk jumlah peminjaman
            borrow_label = QLabel("Masukkan jumlah buku yang ingin dipinjam:")
            borrow_label.setStyleSheet("margin-top: 15px;")
            layout.addWidget(borrow_label)

            borrow_input = QLineEdit(dialog)
            borrow_input.setPlaceholderText("Jumlah buku")
            layout.addWidget(borrow_input)

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
            layout.addWidget(return_date)

            # Tombol untuk melakukan peminjaman
            borrow_button = QPushButton("Pinjam", dialog)
            borrow_button.setStyleSheet("background-color: #007BFF; color: white; font-weight: bold;")
            layout.addWidget(borrow_button)

            # Fungsi untuk memproses peminjaman
            def process_borrow():
                try:
                    borrow_count = int(borrow_input.text())
                    if borrow_count > 0 and borrow_count <= quantity:
                        # Tanggal peminjaman dan pengembalian
                        borrow_date_str = borrow_date.date().toString("yyyy-MM-dd")
                        return_date_str = return_date.date().toString("yyyy-MM-dd")

                        # Simpan ke database
                        conn = sqlite3.connect(database_path)
                        cursor = conn.cursor()

                        # Insert ke tabel peminjaman
                        cursor.execute(
                            "INSERT INTO peminjaman (tanggal_pinjam, tanggal_kembali, anggota_id) VALUES (?, ?, ?)",
                            (borrow_date_str, return_date_str, 1),  # Anggota ID: 1 sebagai contoh
                        )
                        peminjaman_id = cursor.lastrowid

                        # Insert ke tabel peminjaman_detail
                        cursor.execute(
                            "INSERT INTO peminjaman_detail (peminjaman_id, buku_id) VALUES (?, ?)",
                            (peminjaman_id, book_id),
                        )

                        # Update jumlah buku
                        cursor.execute(
                            "UPDATE buku SET jumlah = jumlah - ? WHERE id = ?",
                            (borrow_count, book_id),
                        )
                        conn.commit()
                        conn.close()

                        QMessageBox.information(dialog, "Berhasil", f"{borrow_count} buku berhasil dipinjam.")
                        dialog.accept()
                    else:
                        QMessageBox.warning(dialog, "Gagal", "Jumlah yang dimasukkan tidak valid atau melebihi stok.")
                except ValueError:
                    QMessageBox.warning(dialog, "Gagal", "Masukkan jumlah yang valid.")

            borrow_button.clicked.connect(process_borrow)

            # Tombol untuk menutup dialog
            close_button = QPushButton("Tutup", dialog)
            close_button.clicked.connect(dialog.reject)
            layout.addWidget(close_button)

            dialog.exec()