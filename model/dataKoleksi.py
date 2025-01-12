import sqlite3
import os
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox
from PySide6.QtGui import QPixmap

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")
class KoleksiBuku(QWidget):
    def __init__(self, kategori, ui_class):
        super().__init__()
        self.kategori = kategori  # Kategori buku (Fiksi/Non Fiksi)
        self.ui = ui_class()  
        self.ui.setupUi(self)  # Setup UI dari widget
        
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
                
    def fetch_books(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, judul, cover FROM buku WHERE kategori = ?", (self.kategori,))
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
        cursor.execute("SELECT judul, tahun_terbit, pengarang, penerbit, kategori, jumlah FROM buku WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()

        if book:
            title, year, author, publisher, category, quantity = book
            info = f"Title: {title}\nYear: {year}\nAuthor: {author}\nPublisher: {publisher}\nCategory: {category}\nQuantity: {quantity}"
            QMessageBox.information(self, "Book Information", info)
