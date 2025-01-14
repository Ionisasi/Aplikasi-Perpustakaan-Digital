import os
import sqlite3
from PySide6.QtCore import QTimer, QDate
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QLabel, QAbstractItemView,
    QHBoxLayout, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox,
    QPushButton, QHeaderView
)
from PySide6.QtGui import QIcon
from view.UI_DataKelola import Ui_Form as Ui_dataPinjam
from utils import resource_path

class DataPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dataPinjam()
        self.ui.setupUi(self)
        self.ui.Tambah_data.setVisible(False)
        self.ui.headerTitle.setText("DATA PINJAM")
        self.database_path = database_path = resource_path("database/perpusdigi.db")
        
        # Setup search debouncing
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.on_search)

        # Connect event handlers
        self.ui.Search_action.textChanged.connect(self.start_search_timer)
        
        # Initial table population
        self.populate_table()

    def showEvent(self, event):
        # Memanggil pembaruan tabel setiap kali halaman ditampilkan
        self.populate_table()
        super().showEvent(event)

    def start_search_timer(self):
        # ulangi timer jika user terus mengetik
        self.search_timer.start(300)

    def on_search(self):
        # menghentikan timer dan memulai pencarian
        search_term = self.ui.Search_action.text().strip()
        self.populate_table(search_term)

    def populate_table(self, search_term=""):
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()

                # Query untuk semua peminjaman (baik yang sedang berlangsung maupun yang selesai)
                query = """
                    SELECT 
                        u.nama_lengkap,
                        b.judul,
                        p.tanggal_pinjam,
                        p.tanggal_kembali,
                        pg.tanggal_pengembalian,
                        COALESCE(pg.denda, 0) AS denda,
                        CASE 
                            WHEN pg.tanggal_pengembalian IS NULL THEN 'Belum Kembali'
                            ELSE 'Sudah Kembali'
                        END AS status
                    FROM peminjaman p
                    LEFT JOIN peminjaman_detail pd ON p.id = pd.peminjaman_id
                    LEFT JOIN buku b ON pd.buku_id = b.id
                    LEFT JOIN User u ON p.anggota_id = u.id
                    LEFT JOIN pengembalian pg ON p.id = pg.peminjaman_id
                """

                if search_term:
                    # Menambahkan filter pencarian
                    search_placeholder = f"%{search_term}%"
                    query += " WHERE u.nama_lengkap LIKE ? OR b.judul LIKE ?"
                    params = [search_placeholder, search_placeholder]
                else:
                    params = []

                # Eksekusi query
                cursor.execute(query, params)
                rows = cursor.fetchall()

                # Setel tabel dan masukkan data
                self._setup_table()
                self._populate_table_data(rows)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def _setup_table(self):
        # Mengatur tampilan tabel
        table = self.ui.view_data
        table.setColumnCount(7)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setHorizontalHeaderLabels([
            'Nama Anggota', 'Judul Buku', 'Tanggal Pinjam', 'Tenggat Kembali', 
            'Tanggal Pengembalian', 'Denda', 'Status'
        ])
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)

    def _populate_table_data(self, rows):
        # Mengisi tabel dengan data peminjaman dan pengembalian
        table = self.ui.view_data
        table.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                if col_idx == 3 or col_idx == 4:
                    # Format tanggal (tanggal kembali atau pengembalian)
                    if cell_data is None:
                        cell_data = 'Belum Kembali' if col_idx == 4 else 'Tidak Ada Tenggat'
                elif col_idx == 5:
                    # Format denda
                    cell_data = f"Rp {cell_data:,}" if cell_data != 'Tidak Ada Denda' else cell_data

                # Masukkan data ke dalam tabel
                item = QTableWidgetItem(str(cell_data))
                table.setItem(row_idx, col_idx, item)

    def _add_status_column(self, row_idx):
        # Menambahkan kolom status yang menunjukkan pengembalian
        table = self.ui.view_data
        status_item = QTableWidgetItem("Sudah Kembali" if table.item(row_idx, 4).text() != 'Belum Kembali' else "Belum Kembali")
        table.setItem(row_idx, 6, status_item)