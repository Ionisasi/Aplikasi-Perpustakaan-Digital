import os
import sqlite3
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QMessageBox, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from view.UI_HomePage import Ui_Form as Ui_HomePage

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class homePage(QWidget):
    def __init__(self, user_id):
        super().__init__()
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

        cover_button.clicked.connect(lambda: self.show_book_details(book_id))

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
