import os
import sqlite3
from view.UI_Profile import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from utils import resource_path

database_path = resource_path("database/perpusdigi.db")

class profilePage(QWidget):
    def __init__(self, user_id):
        super().__init__()
        # Inisialisasi UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Aplikasi Profile")
        
        # Simpan user_id untuk identifikasi pengguna
        self.user_id = user_id
        
        # Muat data profil pengguna saat halaman dibuka
        self.load_user_profile()

        # Hubungkan tombol dengan fungsi
        self.ui.saveButton.clicked.connect(self.simpan_perubahan)

    def load_user_profile(self):
        """Muat profil pengguna dari database berdasarkan user_id."""
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Ambil data pengguna
            query = "SELECT nama_lengkap, username, telp, alamat, jenis_kelamin FROM User WHERE id = ?"
            cursor.execute(query, (self.user_id,))
            result = cursor.fetchone()

            if result:
                # Isi input dengan data pengguna
                self.ui.namaInput.setText(result[0])
                self.ui.userInput.setText(result[1])  # Menggunakan username
                self.ui.teleponInput.setText(result[2])
                self.ui.alamatInput.setPlainText(result[3])
                
                # Set jenis kelamin berdasarkan data
                if result[4] == 'L':
                    self.ui.lakiCBox.setChecked(True)
                elif result[4] == 'P':
                    self.ui.perempuanCBox.setChecked(True)
            else:
                QMessageBox.warning(self, "Error", "Data pengguna tidak ditemukan!")

            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")

    def simpan_perubahan(self):
        """Simpan perubahan profil pengguna ke database."""
        try:
            # Ambil data dari input
            nama = self.ui.namaInput.text()
            username = self.ui.userInput.text()  # Menggunakan username
            telepon = self.ui.teleponInput.text()
            alamat = self.ui.alamatInput.toPlainText()

            # Validasi input
            if not nama or not username:
                QMessageBox.critical(self, "Error", "Nama dan username harus diisi!")
                return

            # Ambil jenis kelamin berdasarkan status radio button
            jenis_kelamin = None
            if self.ui.lakiCBox.isChecked():
                jenis_kelamin = 'L'
            elif self.ui.perempuanCBox.isChecked():
                jenis_kelamin = 'P'
            
            if jenis_kelamin is None:
                QMessageBox.critical(self, "Error", "Jenis kelamin harus dipilih!")
                return

            # Koneksi ke database
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Perbarui data pengguna
            query = """
            UPDATE User
            SET nama_lengkap = ?, username = ?, telp = ?, alamat = ?, jenis_kelamin = ?
            WHERE id = ?
            """
            cursor.execute(query, (nama, username, telepon, alamat, jenis_kelamin, self.user_id))
            conn.commit()
            conn.close()
            
            # Tampilkan pesan sukses
            QMessageBox.information(self, "Sukses", 
                f"Data berhasil disimpan:\n\n"
                f"Nama: {nama}\n"
                f"Username: {username}\n"
                f"Telepon: {telepon}\n"
                f"Alamat: {alamat}\n"
                f"Jenis Kelamin: {'Laki-laki' if jenis_kelamin == 'L' else 'Perempuan'}")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {str(e)}")
