from PySide6.QtWidgets import QMainWindow
from view.UIdashboard import Ui_Dashboard  # Import hasil konversi dari Dashboard.ui

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)