import os
import sys
import sqlite3
import hashlib
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from view.UI_Login import Ui_MainWindow
from model.dashboard import Dashboard
from model.registrasi import Registrasi

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hubungkan tombol login dengan fungsi
        self.ui.loginButton.clicked.connect(self.handle_login)
        self.ui.registerButton.clicked.connect(self.handle_signup)
        
        self.role = None

    def handle_login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        if not username or not password:
            QMessageBox.critical(self, "Error", "Username dan password harus diisi!")
            return

        # Hash password dengan SHA-256 untuk validasi
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Tentukan jalur absolut ke database
        DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database", "perpusdigi.db")

        try:
            # Koneksi ke database
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()

            # Query untuk memeriksa username dan password
            query = "SELECT Role FROM User WHERE username = ? AND password = ?"
            cursor.execute(query, (username, hashed_password))
            result = cursor.fetchone()

            conn.close()

            if result is None:
                QMessageBox.critical(self, "Error", "Username atau password salah!")
                return

            self.role = result[0]

            self.close()

            self.open_dashboard()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")
    
    def open_dashboard(self):
        # Buka dashboard
        self.dashboard = Dashboard(self.role)
        self.dashboard.show()  

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