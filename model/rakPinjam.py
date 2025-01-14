import os
import sqlite3
from PySide6.QtCore import QDate, Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PySide6.QtGui import QPixmap
from view.UI_KoleksiBuku import Ui_Form as UI_rakPinjam  # UI Utama

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class rakPinjamPage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_rakPinjam()  # UI Utama
        self.ui.setupUi(self)
        self.user_id = user_id  # Simpan ID pengguna
        self.ui.headerTitle.setText("RAK PINJAM")
        self.ui.search.setVisible(False)

        # Melacak buku yang telah ditampilkan
        self.books_displayed = {}

        # Atur tata letak untuk buku
        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.ui.scrollAreaWidgetContents.setLayout(QVBoxLayout())

        self.book_layout = self.ui.scrollAreaWidgetContents.layout()

        # Atur timer untuk menyegarkan tampilan buku setiap 5 detik
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tampilkan_buku_dipinjam)
        self.timer.start(5000)  # Segarkan setiap 5 detik

        # Tampilkan awal buku yang dipinjam
        self.tampilkan_buku_dipinjam()

    def tampilkan_buku_dipinjam(self):
        # Ambil buku dari database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        query = """
        SELECT b.id, b.judul, b.cover, p.tanggal_pinjam, p.tanggal_kembali
        FROM peminjaman_detail pd
        JOIN peminjaman p ON pd.peminjaman_id = p.id
        JOIN buku b ON pd.buku_id = b.id
        LEFT JOIN pengembalian_detail pgd ON pd.buku_id = pgd.buku_id
        LEFT JOIN pengembalian pg ON pgd.pengembalian_id = pg.id
        WHERE p.anggota_id = ? AND pg.id IS NULL;
        """
        try:
            cursor.execute(query, (self.user_id,))
            results = cursor.fetchall()

            # Kamus untuk menyimpan jumlah setiap buku yang dipinjam
            borrowed_books = {}

            for book_id, title, cover_path, tanggal_pinjam, tanggal_kembali in results:
                # Hitung berapa kali buku ini dipinjam
                if book_id not in borrowed_books:
                    borrowed_books[book_id] = {
                        "title": title,
                        "cover": cover_path,
                        "tanggal_pinjam": tanggal_pinjam,
                        "tanggal_kembali": tanggal_kembali,
                        "count": 0
                    }
                borrowed_books[book_id]["count"] += 1  # Tingkatkan jumlah peminjaman

            # Tambah buku ke tampilan berdasarkan jumlah peminjaman yang dihitung
            for book_id, book_info in borrowed_books.items():
                if book_id not in self.books_displayed:
                    self.add_book_to_display(book_id, book_info)

        except sqlite3.Error as e:
            print(f"Kesalahan database: {e}")
        finally:
            conn.close()

    def add_book_to_display(self, book_id, book_info):
        # Tambahkan buku hanya jika belum ditampilkan
        if book_id in self.books_displayed:
            return

        # Tambahkan buku ke tata letak tampilan
        book_widget = self.create_book_widget(
            book_id,
            book_info["title"],
            book_info["cover"],
            book_info["tanggal_pinjam"],
            book_info["tanggal_kembali"],
            book_info["count"]
        )
        self.book_layout.addWidget(book_widget)
        self.books_displayed[book_id] = book_widget  # Lacak buku yang ditampilkan berdasarkan ID

    def create_book_widget(self, book_id, title, cover_path, tanggal_pinjam, tanggal_kembali, borrow_count):
        widget = QWidget()

        # Gunakan Ui_Form dari pinjamWrapper untuk mengatur widget buku individu
        from view.pinjamWrapper import Ui_Form
        book_ui = Ui_Form()
        book_ui.setupUi(widget)

        # Atur elemen dalam widget buku individu
        book_ui.coverImg.setPixmap(QPixmap(cover_path) if os.path.exists(cover_path) else QPixmap())
        book_ui.judulBuku.setText(title)
        book_ui.tanggalPeminjaman.setDate(
            QDate.fromString(tanggal_pinjam, "yyyy-MM-dd") if tanggal_pinjam else QDate.currentDate()
        )
        book_ui.tanggalDeadline.setDate(
            QDate.fromString(tanggal_kembali, "yyyy-MM-dd") if tanggal_kembali else QDate.currentDate().addDays(7)
        )

        # Atur jumlah pinjaman dalam widget buku individu
        book_ui.JumlahPinjamOutput.setText(str(borrow_count))  # Tampilkan jumlah yang benar

        book_ui.KembalikanBtn.clicked.connect(lambda: self.return_book(book_id, widget))

        return widget
    
    def return_book(self, book_id, widget):
        # Ambil peminjaman_id dan tanggal pengembalian yang sesuai untuk buku
        conn = sqlite3.connect(database_path)
        conn.execute("PRAGMA foreign_keys = OFF;")  # Nonaktifkan sementara pemeriksaan kunci asing
        cursor = conn.cursor()

        try:
            # Periksa apakah buku merupakan bagian dari catatan peminjaman yang sedang berlangsung (belum dikembalikan)
            query = """
            SELECT p.id, p.tanggal_pinjam, p.tanggal_kembali
            FROM peminjaman p
            JOIN peminjaman_detail pd ON p.id = pd.peminjaman_id
            WHERE pd.buku_id = ? AND p.anggota_id = ?;
            """
            cursor.execute(query, (book_id, self.user_id))
            peminjaman = cursor.fetchone()

            if peminjaman is None:
                QMessageBox.warning(self, "Error", "Buku ini tidak dalam status peminjaman.")
                return

            peminjaman_id, tanggal_pinjam, tanggal_kembali = peminjaman

            # Hitung tanggal saat ini dan periksa pengembalian terlambat (tenggat)
            today = QDate.currentDate()
            denda = 0
            if tanggal_kembali is not None:
                tenggat_kembali = QDate.fromString(tanggal_kembali, "yyyy-MM-dd")
                if today > tenggat_kembali:
                    denda = (today.toPyDate() - tenggat_kembali.toPyDate()).days * 1000  # Denda 1000 per hari keterlambatan

            # Tambah entri pengembalian ke tabel pengembalian
            query = """
            INSERT INTO pengembalian (tanggal_pengembalian, denda, peminjaman_id, anggota_id)
            VALUES (?, ?, ?, ?);
            """
            cursor.execute(query, (today.toString("yyyy-MM-dd"), denda, peminjaman_id, self.user_id))
            pengembalian_id = cursor.lastrowid  # Dapatkan pengembalian_id yang baru dimasukkan

            # Tambahkan entri ke pengembalian_detail
            query = """
            INSERT INTO pengembalian_detail (pengembalian_id, buku_id)
            VALUES (?, ?);
            """
            cursor.execute(query, (pengembalian_id, book_id))

            # Perbarui jumlah buku setelah pengembalian
            query = """
            UPDATE buku
            SET jumlah = jumlah + 1
            WHERE id = ?;
            """
            cursor.execute(query, (book_id,))

            # Komit perubahan
            conn.commit()

            # Hapus widget buku dari tampilan
            self.book_layout.removeWidget(widget)
            widget.deleteLater()

            QMessageBox.information(self, "Sukses", "Buku berhasil dikembalikan dan data peminjaman dihapus.")

        except sqlite3.Error as e:
            conn.rollback()  # Kembalikan pada kesalahan
            print(f"Kesalahan database: {e}")
            QMessageBox.critical(self, "Error", "Terjadi kesalahan dalam pengembalian buku.")
        finally:
            conn.close()