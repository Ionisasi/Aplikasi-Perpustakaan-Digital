import sqlite3
import os
import hashlib
import re
from PySide6.QtWidgets import QWidget, QMessageBox
from view.UI_RegistrasiAnggota import Ui_Form
from utils import resource_path

class Registrasi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connect_button()

    def connect_button(self):
        # Menghubungkan tombol
        self.ui.daftarButton.clicked.connect(self.sign_up)
    
    def sign_up(self):
        # Ambil data dari input
        self.nama_lengkap = self.ui.namaInput.text()
        self.username = self.ui.usernameInput.text()
        self.password = self.ui.passwordInput.text()
        self.alamat = self.ui.alamatInput.toPlainText()
        self.telepon = self.ui.teleponInput.text()
        self.jenis_kelamin = "L" if self.ui.lakiCheckBox.isChecked() else "P"
        self.role = 0  # Default role untuk anggota biasa

        # Validasi semua field kecuali alamat harus diisi oleh user
        if not self.nama_lengkap or not self.username or not self.password or not self.telepon or not self.jenis_kelamin:
            QMessageBox.critical(self, "Error", "Semua field kecuali alamat harus diisi!")
            return
        
        # Validasi total digit nomor telepon
        def is_valid_phone(phone):
            return phone.isdigit() and len(phone) >= 10
        
        if not is_valid_phone(self.telepon):
            QMessageBox.critical(self, "Error", "Nomor telepon tidak valid!")
            return

        # Hash password menggunakan SHA-256
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

        database_path = resource_path("database/perpusdigi.db")
        
        try:
            # Koneksi ke database
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Query untuk memeriksa username yang sama
            check_query = "SELECT COUNT(*) FROM User WHERE username = ?"
            cursor.execute(check_query, (self.username,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.critical(self, "Error", "Username sudah terdaftar!")
                conn.close()
                return

            # Query untuk menambahkan data
            query = """
            INSERT INTO User (nama_lengkap, username, password, telp, jenis_kelamin, alamat, Role)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (self.nama_lengkap, self.username, hashed_password, self.telepon, self.jenis_kelamin, self.alamat, self.role))

            # Simpan perubahan dan tutup koneksi
            conn.commit()
            conn.close()

            # Tampilkan pesan sukses
            QMessageBox.information(self, "Sukses", "Registrasi berhasil!")
            self.close()  # Menutup form registrasi

        except sqlite3.Error as e:
            # Tampilkan pesan error jika gagal
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")