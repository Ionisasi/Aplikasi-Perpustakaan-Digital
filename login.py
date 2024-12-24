import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from _compiled_connector import login_action, register_action
from view.Perpustakaan import Ui_MainWindow  # Hasil konversi dari Perpustakaan.ui

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hubungkan tombol login dengan fungsi
        self.ui.loginButton.clicked.connect(self.handle_login)
        self.ui.registerButton.clicked.connect(self.handle_signup)

    def handle_login(self):
        username = self.ui.usernameInput.text().strip()  # Mengambil input dari QLineEdit untuk username
        password = self.ui.passwordInput.text().strip()  # Mengambil input dari QLineEdit untuk password

        success, message = login_action(username, password)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)

    def handle_signup(self):
        username = self.ui.usernameInput.text().strip()  # Mengambil input dari QLineEdit untuk Username
        password = self.ui.passwordInput.text().strip()  # Mengambil input dari QLineEdit untuk password

        if not username or not password:
            QMessageBox.warning(self, "Error", "Username dan Password tidak boleh kosong!")
            return

        success, message = register_action(username, password)
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
    window = MainApp()
    window.show()
    sys.exit(app.exec())
