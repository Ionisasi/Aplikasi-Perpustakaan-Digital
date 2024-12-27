import os
import sys
import sqlite3
import hashlib
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from view.UI_Perpustakaan import Ui_MainWindow
from model.dashboard import Dashboard
from model.registrasi import Registrasi

# Path ke database
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database", "perpusdigi.db")

# Fungsi untuk menangani login
def login_action(email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Koneksi ke database
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Query untuk memeriksa email dan password
        query = "SELECT * FROM anggota WHERE email = ? AND password = ?"
        cursor.execute(query, (email, hashed_password))
        result = cursor.fetchone()
        conn.close()

        if result:
            return True, "Login sukses! Selamat Datang."
        else:
            return False, "Email atau password salah. Silakan coba lagi."
    except sqlite3.Error as e:
        return False, f"Terjadi kesalahan pada database: {e}"

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
            
            # Buka jendela Dashboard
            self.dashboard = Dashboard()
            self.dashboard.show()
            
            # Tutup jendela login
            self.close()
        else:
            QMessageBox.critical(self, "Error", message)

    def handle_signup(self):
        # Buka jendela registrasi
        self.register = Registrasi()
        self.register.show()

if __name__ == "__main__":
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