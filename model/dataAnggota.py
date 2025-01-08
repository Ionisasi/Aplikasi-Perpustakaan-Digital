import os
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHBoxLayout, QPushButton
from view.UI_DataAanggota import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget
        self.database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")
        self.populate_table()  # Panggil fungsi untuk mengisi tabel

    def populate_table(self):
        """
        Fungsi untuk mengambil data anggota dari database dan menampilkan di tabel UI.
        """
        try:
            # Koneksi ke database
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            # Query untuk mengambil data anggota
            try:
                # Modifikasi: Tambahkan try-except untuk menangkap kesalahan pada query
                cursor.execute("SELECT nama_lengkap, username, telp, jenis_kelamin, alamat, Role FROM User")
                rows = cursor.fetchall()
            except sqlite3.Error as query_error:
                # Tampilkan pesan jika ada kesalahan dalam query SQL
                QMessageBox.critical(self, "Error", f"Kesalahan pada query SQL: {query_error}")
                return  # Keluar dari fungsi jika terjadi kesalahan

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
                    if col_index == 3:  # Kolom "jenis_kelamin"
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
            # Tampilkan pesan error jika gagal koneksi database
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")

    def edit_data(self, row):
    # Ambil data dari tabel berdasarkan baris yang dipilih
        username = self.ui.tableWidget.item(row, 1).text()  # Ambil username sebagai kunci
        nama_lengkap = self.ui.tableWidget.item(row, 0).text()
        telp = self.ui.tableWidget.item(row, 2).text()
        jenis_kelamin = self.ui.tableWidget.item(row, 3).text()
        alamat = self.ui.tableWidget.item(row, 4).text()
        role = self.ui.tableWidget.item(row, 5).text()

        # Konversi jenis kelamin ke format database ('L' atau 'P')
        if jenis_kelamin == 'Laki-Laki':
            jenis_kelamin = 'L'
        elif jenis_kelamin == 'Perempuan':
            jenis_kelamin = 'P'

        # Tampilkan dialog untuk mengedit data
        result = QMessageBox.question(
            self,
            "Edit Data",
            f"Apakah Anda yakin ingin mengedit data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        # Jika pengguna memilih "Yes", lakukan update ke database
        if result == QMessageBox.Yes:
            try:
                # Koneksi ke database
                conn = sqlite3.connect(self.database_path)
                cursor = conn.cursor()

                # Query UPDATE
                query = """
                UPDATE User 
                SET nama_lengkap = ?, telp = ?, jenis_kelamin = ?, alamat = ?, Role = ?
                WHERE username = ?
                """
                cursor.execute(query, (nama_lengkap, telp, jenis_kelamin, alamat, role, username))
                conn.commit()  # Simpan perubahan
                conn.close()

                # Tampilkan pesan sukses
                QMessageBox.information(self, "Sukses", "Data berhasil diupdate!")
            except sqlite3.Error as e:
                # Tampilkan pesan error jika query gagal
                QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")

    def hapus_data(self, row):
        """
        Fungsi untuk menghapus data anggota berdasarkan baris yang dipilih di tabel.
        """
        # Ambil data dari tabel berdasarkan baris yang dipilih
        nama = self.ui.tableWidget.item(row, 0).text()

        # Tampilkan dialog konfirmasi penghapusan
        result = QMessageBox.question(
            self, 
            "Hapus Data", 
            f"Apakah Anda yakin ingin menghapus data untuk: {nama}?", 
            QMessageBox.Yes | QMessageBox.No
        )

        # Jika pengguna memilih "Yes", lakukan penghapusan
        if result == QMessageBox.Yes:
            try:
                # Koneksi ke database
                conn = sqlite3.connect(self.database_path)
                cursor = conn.cursor()

                # Query DELETE
                query = "DELETE FROM User WHERE nama_lengkap = ?"
                cursor.execute(query, (nama,))
                conn.commit()  # Simpan perubahan
                conn.close()

                # Tampilkan pesan sukses
                QMessageBox.information(self, "Sukses", f"Data untuk {nama} telah dihapus.")
                # Perbarui tabel
                self.populate_table()
            except sqlite3.Error as e:
                # Tampilkan pesan error jika query gagal
                QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")
