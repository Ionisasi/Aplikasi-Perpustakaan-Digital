import os
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QListWidget
from view.UI_KoleksiFiksi import Ui_BukuFiksi as UI_KoleksiFiksi

class KoleksiFiksi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UI_KoleksiFiksi()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget