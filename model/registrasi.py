from PySide6.QtWidgets import QWidget, QMessageBox
from view.UI_RegistrasiAnggota import Ui_Form

class Registrasi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.daftarButton.clicked.connect(self.sign_up)
    
    def sign_up(self):
        # self.nama = self.ui.namaInput.text()
        # self.email = self.ui.emailInput.text()
        # self.password = self.ui.passwordInput.text()
        # self.alamat = self.ui.alamatInput.toPlainText()
        # self.telepon = self.ui.teleponInput.text()
        # self.jenis_kelamin = "Laki-laki" if self.ui.lakiCheckBox.isChecked() else "Perempuan"
        
        # peringatan jika ada field yang kosong
        # if not self.nama or not self.email or not self.password:
        #     QMessageBox.critical(self, "Error", "Nama, Email, dan Password harus diisi!")
        #     return
        
        self.close() # sementara hanya menutup form registrasi