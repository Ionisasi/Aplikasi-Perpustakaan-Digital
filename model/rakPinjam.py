import os
import sqlite3
from PySide6.QtCore import QDate, Qt, QDateTime
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from view.UI_KoleksiBuku import Ui_Form as UI_rakPinjam

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class rakPinjamPage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_rakPinjam()
        self.ui.setupUi(self)
        self.user_id = user_id  # Simpan user_id
        self.ui.headerTitle.setText("RAK PINJAM")
        self.ui.search.setVisible(False)

        # Track displayed books
        self.books_displayed = set()

        # Setup layout for books
        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        self.book_layout = self.ui.scrollAreaWidgetContents.layout()

        # Tampilkan buku yang dipinjam
        self.tampilkan_buku_dipinjam()

    def tampilkan_buku_dipinjam(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        query = """
        SELECT b.id, b.judul, b.cover, p.tanggal_pinjam, p.tanggal_kembali
        FROM peminjaman_detail pd
        JOIN peminjaman p ON pd.peminjaman_id = p.id
        JOIN buku b ON pd.buku_id = b.id
        WHERE p.anggota_id = ?;
        """
        try:
            cursor.execute(query, (self.user_id,))
            results = cursor.fetchall()

            for book_id, title, cover_path, tanggal_pinjam, tanggal_kembali in results:
                if book_id not in self.books_displayed:
                    self.add_book_to_display(
                        book_id, title, cover_path, tanggal_pinjam, tanggal_kembali
                    )

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def add_book_to_display(self, book_id, title, cover_path, tanggal_pinjam, tanggal_kembali):
        # Tambahkan buku ke row layout
        book_widget = self.create_book_widget(book_id, title, cover_path, tanggal_pinjam, tanggal_kembali)
        self.book_layout.addWidget(book_widget)
        self.books_displayed.add(book_id)

    def create_book_widget(self, book_id, title, cover_path, tanggal_pinjam, tanggal_kembali):
        widget = QWidget()
        
        # Gunakan Ui_Form untuk setup widget
        from view.pinjamWrapper import Ui_Form
        book_ui = Ui_Form()
        book_ui.setupUi(widget)

        # Atur elemen-elemen dalam widget
        book_ui.coverImg.setPixmap(QPixmap(cover_path) if os.path.exists(cover_path) else QPixmap())
        book_ui.judulBuku.setText(title)
        book_ui.tanggalPeminjaman.setDate(
            QDate.fromString(tanggal_pinjam, "yyyy-MM-dd") if tanggal_pinjam else QDate.currentDate()
        )
        book_ui.tanggalDeadline.setDate(
            QDate.fromString(tanggal_kembali, "yyyy-MM-dd") if tanggal_kembali else QDate.currentDate().addDays(7)
        )
        book_ui.KembalikanBtn.clicked.connect(lambda: self.return_book(book_id, widget))

        return widget

    def return_book(self, book_id, widget):
        pass

