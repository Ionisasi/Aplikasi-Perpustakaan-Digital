import os
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from view.UI_DataBuku import Ui_Form as Ui_DataBuku

class DataBukuPage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataBuku()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget