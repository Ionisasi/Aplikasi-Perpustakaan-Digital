import os
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from view.UI_KoleksiFiksi import Ui_Koleksi as UI_KoleksiFiksi

class KoleksiFiksi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_KoleksiFiksi  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget

        # List widget untuk Fiksi
        self.list_fiksi = QListWidget(self)
        self.list_fiksi.setGeometry(10, 10, 200, 300)

        # List widget untuk Non Fiksi
        self.list_non_fiksi = QListWidget(self)
        self.list_non_fiksi.setGeometry(220, 10, 200, 300)

        self.load_books()

    def load_books(self):
        conn = sqlite3.connect('perpusdigi.db')  # Ganti dengan nama database
        cursor = conn.cursor()

        # Memuat buku Fiksi
        cursor.execute("SELECT judul FROM buku WHERE kategori = 'Fiksi'")
        books_fiksi = cursor.fetchall()
        for book in books_fiksi:
            self.list_fiksi.addItem(book[0])

        conn.close()