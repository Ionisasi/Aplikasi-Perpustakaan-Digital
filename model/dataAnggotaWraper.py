from PySide6.QtWidgets import QWidget, QMessageBox
from view.UI_DataAnggota import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget
        
        self.ui.ubahBtn.clicked.connect(self.ubah_data)
    def ubah_data(self):
        # test
        QMessageBox.information(self, "Pemberitahuan", "Fitur ini masih dalam pengembangan")
