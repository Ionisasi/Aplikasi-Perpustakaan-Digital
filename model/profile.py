import sys
import os
from view.UI_Profile import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

# Tambahkan parent directory ke system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

class profilePage(QWidget):
    def __init__(self):
        super().__init__()
        # Inisialisasi UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Aplikasi Profile")
        
        # Hubungkan tombol dengan fungsi
        self.ui.daftarButton.clicked.connect(self.simpan_perubahan)

    def simpan_perubahan(self):
        try:
            # Ambil data dari input
            nama = self.ui.namaInput.text()
            email = self.ui.emailInput.text()
            password = self.ui.passwordInput.text()
            telepon = self.ui.teleponInput.text()
            alamat = self.ui.alamatInput.toPlainText()

            # Tampilkan data di console
            print("Nama:", nama)
            print("Email:", email)
            print("Password:", password)
            print("Telepon:", telepon)
            print("Alamat:", alamat)

            # Update header title
            self.ui.headerTitle.setText("Data Berhasil Disimpan!")
            
            # Tampilkan pesan sukses
            QMessageBox.information(self, "Sukses", 
                f"Data berhasil disimpan:\n\n"
                f"Nama: {nama}\n"
                f"Email: {email}\n"
                f"Telepon: {telepon}\n"
                f"Alamat: {alamat}")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {str(e)}")