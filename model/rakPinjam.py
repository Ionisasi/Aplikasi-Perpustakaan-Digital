import os
import sqlite3
from PySide6.QtCore import QDate, Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from view.UI_KoleksiBuku import Ui_Form as UI_rakPinjam  # Main UI

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class rakPinjamPage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_rakPinjam()  # Main UI
        self.ui.setupUi(self)
        self.user_id = user_id  # Store the user ID
        self.ui.headerTitle.setText("RAK PINJAM")
        self.ui.search.setVisible(False)

        # Track displayed books
        self.books_displayed = {}

        # Setup layout for books
        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        self.book_layout = self.ui.scrollAreaWidgetContents.layout()

        # Set up a timer to refresh the book display every 5 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tampilkan_buku_dipinjam)
        self.timer.start(5000)  # Refresh every 5 seconds

        # Initial display of borrowed books
        self.tampilkan_buku_dipinjam()

    def tampilkan_buku_dipinjam(self):
        # Fetch books from the database
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

            # Dictionary to store count of each borrowed book
            borrowed_books = {}

            for book_id, title, cover_path, tanggal_pinjam, tanggal_kembali in results:
                # Count how many times this book was borrowed
                if book_id not in borrowed_books:
                    borrowed_books[book_id] = {
                        "title": title,
                        "cover": cover_path,
                        "tanggal_pinjam": tanggal_pinjam,
                        "tanggal_kembali": tanggal_kembali,
                        "count": 0
                    }
                borrowed_books[book_id]["count"] += 1  # Increment the borrow count

            # Add books to display based on the counted borrow occurrences
            for book_id, book_info in borrowed_books.items():
                if book_id not in self.books_displayed:
                    self.add_book_to_display(book_id, book_info)

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def add_book_to_display(self, book_id, book_info):
        # Only add the book if it hasn't been displayed yet
        if book_id in self.books_displayed:
            return

        # Add the book to the display layout
        book_widget = self.create_book_widget(
            book_id,
            book_info["title"],
            book_info["cover"],
            book_info["tanggal_pinjam"],
            book_info["tanggal_kembali"],
            book_info["count"]
        )
        self.book_layout.addWidget(book_widget)
        self.books_displayed[book_id] = book_widget  # Track displayed book by ID

    def create_book_widget(self, book_id, title, cover_path, tanggal_pinjam, tanggal_kembali, borrow_count):
        widget = QWidget()

        # Use Ui_Form from pinjamWrapper for setting up the individual book widget
        from view.pinjamWrapper import Ui_Form
        book_ui = Ui_Form()
        book_ui.setupUi(widget)

        # Set up the elements in the individual book widget
        book_ui.coverImg.setPixmap(QPixmap(cover_path) if os.path.exists(cover_path) else QPixmap())
        book_ui.judulBuku.setText(title)
        book_ui.tanggalPeminjaman.setDate(
            QDate.fromString(tanggal_pinjam, "yyyy-MM-dd") if tanggal_pinjam else QDate.currentDate()
        )
        book_ui.tanggalDeadline.setDate(
            QDate.fromString(tanggal_kembali, "yyyy-MM-dd") if tanggal_kembali else QDate.currentDate().addDays(7)
        )

        # Set the borrowed count in the individual book widget
        book_ui.JumlahPinjamOutput.setText(str(borrow_count))  # Show the correct count

        book_ui.KembalikanBtn.clicked.connect(lambda: self.return_book(book_id, widget))

        return widget

    def return_book(self, book_id, widget):
        pass
