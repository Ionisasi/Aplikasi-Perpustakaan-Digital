import os
import sqlite3
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QLabel, QAbstractItemView,
    QHBoxLayout, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox,
    QPushButton, QHeaderView
)
from PySide6.QtGui import QIcon
from view.UI_DataKelola import Ui_Form as Ui_DataAnggota

class DataPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()
        self.ui.setupUi(self)
        self.ui.Tambah_data.setVisible(False)
        self.ui.headerTitle.setText("DATA PINJAM")
        self.database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

