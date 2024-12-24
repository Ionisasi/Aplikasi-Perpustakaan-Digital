import os
import sys
import hashlib
import json
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from view.Perpustakaan import Ui_MainWindow  # Hasil konversi dari Perpustakaan.ui

# Path untuk menyimpan data pengguna kemudian di konfirmasi
DATA_AKUN = os.path.join(os.path.dirname(__file__), "database", "users.json")
os.makedirs(os.path.join(os.path.dirname(__file__), "database"), exist_ok=True)

# Fungsi untuk memuat data pengguna
def load_users():
    if os.path.exists(DATA_AKUN):
        with open(DATA_AKUN, "r") as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data pengguna
def save_users(users):
    with open(DATA_AKUN, "w") as file:
        json.dump(users, file, indent=4)

# Fungsi untuk menangani login
def login_action(email, password):
    users = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if email in users and users[email]["password"] == hashed_password:
        return True, "Login sukses! Selamat Datang."
    elif email not in users:
        return False, "Email tidak ditemukan. Silakan daftar terlebih dahulu."
    else:
        return False, "Password salah. Silakan coba lagi."

# Fungsi untuk menangani registrasi
def register_action(email, password):
    users = load_users()
    if email in users:
        return False, "Email sudah terdaftar. Silakan login."

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[email] = {"password": hashed_password}
    save_users(users)
    return True, "Registrasi berhasil! Anda sekarang dapat login."

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hubungkan tombol login dengan fungsi
        self.ui.loginButton.clicked.connect(self.handle_login)
        self.ui.registerButton.clicked.connect(self.handle_signup)

    def handle_login(self):
        email = self.ui.usernameInput.text().strip()  # Mengambil input dari QLineEdit untuk username
        password = self.ui.passwordInput.text().strip()  # Mengambil input dari QLineEdit untuk password

        success, message = login_action(email, password)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)

    def handle_signup(self):
        email = self.ui.usernameInput.text().strip()  # Mengambil input dari QLineEdit untuk username
        password = self.ui.passwordInput.text().strip()  # Mengambil input dari QLineEdit untuk password

        if not email or not password:
            QMessageBox.warning(self, "Error", "Email dan password tidak boleh kosong!")
            return

        success, message = register_action(email, password)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    # Konfigurasi aplikasi
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Tema gelap
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    app.setPalette(palette)

    # Menjalankan aplikasi
    window = Login()
    window.show()
    sys.exit(app.exec())