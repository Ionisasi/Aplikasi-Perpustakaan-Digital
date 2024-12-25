from PySide6.QtWidgets import QMainWindow
from view.UI_Dashboard import Ui_Dashboard
class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)