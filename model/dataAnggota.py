import os
import sqlite3
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, 
    QLabel, QAbstractItemView, QHBoxLayout, QVBoxLayout, QLineEdit, QDialog, 
    QDialogButtonBox, QPushButton
    )
from view.UI_DataAanggota import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()
        self.ui.setupUi(self)
        self.database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")
        
        # Tambahkan QTimer untuk debouncing pencarian
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.on_search)

        # Variabel untuk pagination
        self.page_size = 50
        self.current_page = 0

        # Event handler
        self.ui.lineEdit.textChanged.connect(self.start_search_timer)

        self.populate_table()

    def start_search_timer(self):
        """Memulai timer untuk debouncing pencarian."""
        self.search_timer.start(300)  # Tunda pencarian selama 300 ms
    def populate_table(self, search_term=""):
        """
        Fungsi untuk mengambil data anggota dari database dan menampilkan di tabel UI.
        Pencarian berdasarkan nama anggota jika search_term diberikan.
        """
        try:
            # Koneksi ke database
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            # Query untuk mengambil data anggota dengan pagination
            query = "SELECT nama_lengkap, username, telp, jenis_kelamin, alamat, Role FROM User"
            params = []

            if search_term:
                query += " WHERE nama_lengkap LIKE ?"
                params.append(f"%{search_term}%")

            query += " LIMIT ? OFFSET ?"
            params.extend([self.page_size, self.current_page * self.page_size])

            cursor.execute(query, params)
            rows = cursor.fetchall()

            # Set jumlah baris pada tabel
            self.ui.tableWidget.setRowCount(len(rows))  # Set jumlah baris
            self.ui.tableWidget.setColumnCount(7)  # Tambah 1 kolom untuk tombol
            self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # Set header tabel
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ['Nama', 'Username', 'Telepon', 'Jenis Kelamin', 'Alamat', 'Role', 'Kelola']
            )

            # Isi tabel dengan data dari database
            for row_index, row in enumerate(rows):
                for col_index, cell_data in enumerate(row):
                    # Ubah jenis kelamin menjadi 'Laki-Laki' atau 'Perempuan'
                    if col_index == 3:  # Kolom "jenis_kelamin"
                        cell_data = 'Laki-Laki' if cell_data == 'L' else 'Perempuan'

                    item = QTableWidgetItem(str(cell_data))
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
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")
    def on_search(self):
        """Event handler untuk pencarian berdasarkan nama."""
        self.current_page = 0  # Reset ke halaman pertama saat pencarian baru
        search_term = self.ui.lineEdit.text().strip()
        self.populate_table(search_term)

    def edit_data(self, row):
        # Ambil data dari tabel berdasarkan baris yang dipilih
        username = self.ui.tableWidget.item(row, 1).text()  # Ambil username sebagai kunci
        nama_lengkap = self.ui.tableWidget.item(row, 0).text()
        telp = self.ui.tableWidget.item(row, 2).text()
        jenis_kelamin = self.ui.tableWidget.item(row, 3).text()
        alamat = self.ui.tableWidget.item(row, 4).text()
        role = self.ui.tableWidget.item(row, 5).text()

        # Konversi jenis kelamin untuk format database ('L' atau 'P')
        jenis_kelamin = 'L' if jenis_kelamin == 'Laki-Laki' else 'P'

        # Dialog untuk mengedit data
        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Data Anggota")
        dialog.setFixedSize(300, 350)

        layout = QVBoxLayout(dialog)

        # Input fields
        username_input = QLineEdit(dialog)
        username_input.setText(username)
        username_input.setReadOnly(True)  # Tidak dapat diedit, sebagai kunci utama

        nama_input = QLineEdit(dialog)
        nama_input.setText(nama_lengkap)

        telp_input = QLineEdit(dialog)
        telp_input.setText(telp)

        jk_input = QLineEdit(dialog)
        jk_input.setText(jenis_kelamin)

        alamat_input = QLineEdit(dialog)
        alamat_input.setText(alamat)

        role_input = QLineEdit(dialog)
        role_input.setText(role)

        # Tambahkan widget ke layout
        layout.addWidget(QLabel("Username (Tidak dapat diubah):"))
        layout.addWidget(username_input)
        layout.addWidget(QLabel("Nama Lengkap:"))
        layout.addWidget(nama_input)
        layout.addWidget(QLabel("Telepon:"))
        layout.addWidget(telp_input)
        layout.addWidget(QLabel("Jenis Kelamin (L/P):"))
        layout.addWidget(jk_input)
        layout.addWidget(QLabel("Alamat:"))
        layout.addWidget(alamat_input)
        layout.addWidget(QLabel("Role:"))
        layout.addWidget(role_input)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        # Jika pengguna mengonfirmasi perubahan
        if dialog.exec() == QDialog.Accepted:
            # Ambil data yang diubah
            nama_lengkap = nama_input.text()
            telp = telp_input.text()
            jenis_kelamin = jk_input.text()
            alamat = alamat_input.text()
            role = role_input.text()

            # Validasi input
            if not nama_lengkap or not telp or not jenis_kelamin or not alamat or not role:
                QMessageBox.warning(self, "Input Invalid", "Semua kolom harus diisi!")
                return

            # Update data di database
            try:
                conn = sqlite3.connect(self.database_path)
                cursor = conn.cursor()

                query = """
                UPDATE User 
                SET nama_lengkap = ?, telp = ?, jenis_kelamin = ?, alamat = ?, Role = ?
                WHERE username = ?
                """
                cursor.execute(query, (nama_lengkap, telp, jenis_kelamin, alamat, role, username))
                conn.commit()
                conn.close()

                # Tampilkan pesan sukses
                QMessageBox.information(self, "Sukses", "Data berhasil diupdate.")

                # Perbarui tabel
                self.populate_table()
            except sqlite3.Error as e:
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
