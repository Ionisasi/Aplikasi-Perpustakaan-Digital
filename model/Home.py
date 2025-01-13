import os
import sqlite3
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from view.UI_HomePage import Ui_Form as Ui_HomePage

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class homePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)

        # Menghubungkan fungsi untuk menampilkan buku ke scroll area
        self.display_random_books()

    def display_random_books(self):
        # Mendapatkan layout dari scroll area
        scroll_layout = QHBoxLayout(self.ui.scrollAreaWidgetContents)  # Mengubah menjadi QHBoxLayout untuk horizontal
        
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

    def create_book_widget(self, book_id, title, cover):
        # Membuat widget untuk setiap buku dengan cover yang bisa diklik untuk melihat detail
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Label untuk cover buku (menggunakan QPixmap untuk gambar)
        cover_label = QLabel()
        if cover and os.path.exists(cover):
            pixmap = QPixmap(cover)
            cover_label.setPixmap(pixmap.scaled(100, 150, Qt.KeepAspectRatio))  # Ukuran gambar disesuaikan
            cover_label.setAlignment(Qt.AlignCenter)
            cover_label.mousePressEvent = lambda event, book_id=book_id: self.show_book_details(book_id)  # Klik untuk detail
        layout.addWidget(cover_label)

        # Label untuk judul buku
        title_label = QLabel(title)
        title_label.setWordWrap(True)  # Aktifkan word wrap untuk judul yang panjang
        title_label.setAlignment(Qt.AlignCenter)  # Rata tengah
        layout.addWidget(title_label)

        # Mengatur ukuran widget agar lebih konsisten dalam tampilan horizontal
        widget.setFixedWidth(120)  # Menjaga ukuran widget buku tetap konsisten
        return widget

    def show_book_details(self, book_id):
        # Menampilkan detail buku ketika cover ditekan
        try:
            with sqlite3.connect(database_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT judul, pengarang, penerbit, tahun_terbit, kategori, jumlah FROM buku WHERE id = ?", (book_id,))
                book_details = cursor.fetchone()

                if book_details:
                    judul, pengarang, penerbit, tahun_terbit, kategori, jumlah = book_details
                    detail_message = f"Judul: {judul}\nPengarang: {pengarang}\nPenerbit: {penerbit}\nTahun Terbit: {tahun_terbit}\nKategori: {kategori}\nJumlah Tersedia: {jumlah}"
                    QMessageBox.information(self, "Detail Buku", detail_message)
                else:
                    QMessageBox.warning(self, "Error", "Buku tidak ditemukan.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")
