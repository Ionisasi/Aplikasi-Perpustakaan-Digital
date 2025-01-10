import os
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from view.UI_HomePage import Ui_Form as Ui_HomePage

class homePage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget