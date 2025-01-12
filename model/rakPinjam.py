import os
from PySide6.QtWidgets import QWidget
from view.UI_KoleksiBuku import Ui_Form as UI_rakPinjam

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

class rakPinjamPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UI_rakPinjam()  
        self.ui.setupUi(self)
        
        self.ui.headerTitle.setText("RAK PINJAM")