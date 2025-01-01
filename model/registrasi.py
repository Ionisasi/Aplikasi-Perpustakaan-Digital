import sqlite3
import os
import hashlib
from PySide6.QtWidgets import QWidget, QMessageBox
from view.UI_RegistrasiAnggota import Ui_Form

class Registrasi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connect_button()

    def connect_button(self):
        self.ui.daftarButton.clicked.connect(self.sign_up)

    def sign_up(self):
        # Ambil data dari input
        self.nama = self.ui.namaInput.text()
        self.email = self.ui.emailInput.text()
        self.password = self.ui.passwordInput.text()
        self.alamat = self.ui.alamatInput.toPlainText()
        self.telepon = self.ui.teleponInput.text()
        self.jenis_kelamin = "L" if self.ui.lakiCheckBox.isChecked() else "P"

        # Validasi: pastikan field yang wajib tidak kosong
        if not self.nama or not self.email or not self.password or not self.telepon or not self.jenis_kelamin:
            QMessageBox.critical(self, "Error", "Semua field kecuali alamat harus diisi!")
            return

        # Hash password menggunakan SHA-256
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

        # Tentukan jalur absolut ke database
        database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

        try:
            # Koneksi ke database
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Query untuk menambahkan data
            query = """
            INSERT INTO anggota (nama, email, password, telp, jenis_kelamin, alamat)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (self.nama, self.email, hashed_password, self.telepon, self.jenis_kelamin, self.alamat))

            # Simpan perubahan dan tutup koneksi
            conn.commit()
            conn.close()

            # Tampilkan pesan sukses
            QMessageBox.information(self, "Sukses", "Registrasi berhasil!")
            self.close()  # Menutup form registrasi

        except sqlite3.Error as e:
            # Tampilkan pesan error jika gagal
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")
