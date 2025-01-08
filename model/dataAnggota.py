import os
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHBoxLayout, QPushButton
from view.UI_DataAanggota import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget

        self.populate_table()  # Panggil fungsi untuk mengisi tabel

    def populate_table(self):
        # Fungsi untuk mengisi tabel
        database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")  # Path ke database
        try:
            # Koneksi ke database
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Query untuk mengambil data anggota
            cursor.execute("SELECT nama_lengkap, username, telp, jenis_kelamin, alamat, Role FROM User")
            rows = cursor.fetchall()

            # Set jumlah baris pada tabel
            self.ui.tableWidget.setRowCount(len(rows))  # Set jumlah baris
            self.ui.tableWidget.setColumnCount(7)  # Tambah 1 kolom untuk tombol

            # Set header tabel
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ['Nama', 'Username', 'Telepon', 'Jenis Kelamin', 'Alamat', 'Role', 'Kelola']
            )

            # Isi tabel dengan data dari database
            for row_index, row in enumerate(rows):
                for col_index, cell_data in enumerate(row):
                    # Ubah jenis kelamin menjadi 'Laki-Laki' atau 'Perempuan'
                    if col_index == 3:
                        if cell_data == 'L':
                            cell_data = 'Laki-Laki'
                        elif cell_data == 'P':
                            cell_data = 'Perempuan'

                    item = QTableWidgetItem(str(cell_data))  # Buat item dari data
                    self.ui.tableWidget.setItem(row_index, col_index, item)

                # Tambahkan tombol "Edit" dan "Hapus" di kolom "Kelola"
                btn_widget = QWidget()
                btn_layout = QHBoxLayout(btn_widget)
                btn_layout.setContentsMargins(0, 0, 0, 0)

                # Tambahkan tombol Edit dan Hapus
                edit_btn = QPushButton("Edit")
                delete_btn = QPushButton("Hapus")

                # Hubungkan tombol dengan fungsi
                edit_btn.clicked.connect(lambda checked, r=row_index: self.edit_data(r))
                delete_btn.clicked.connect(lambda checked, r=row_index: self.hapus_data(r))

                # Tambahkan tombol ke layout
                btn_layout.addWidget(edit_btn)
                btn_layout.addWidget(delete_btn)

                # Set widget tombol ke kolom "Kelola"
                self.ui.tableWidget.setCellWidget(row_index, 6, btn_widget)

            conn.close()

        except sqlite3.Error as e:
            # Tampilkan pesan error jika gagal
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")

    def edit_data(self, row):
        nama = self.ui.tableWidget.item(row, 0).text()  # Ambil data dari kolom pertama
        QMessageBox.information(self, "Edit Data", f"Edit data untuk: {nama}")

    def hapus_data(self, row):
        nama = self.ui.tableWidget.item(row, 0).text()  # Ambil data dari kolom pertama
        result = QMessageBox.question(
            self, "Hapus Data", f"Apakah Anda yakin ingin menghapus data untuk: {nama}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if result == QMessageBox.Yes:
            # Logika hapus data di database
            QMessageBox.information(self, "Hapus Data", f"Data untuk {nama} telah dihapus.")

