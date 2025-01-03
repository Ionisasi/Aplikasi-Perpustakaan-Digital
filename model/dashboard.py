from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_UI_Dashboard

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)

        # connect buttons
        self.ui.Logout.clicked.connect(self.logout)
        self.ui.Data.clicked.connect(self.toggle_kelola_submenu)
        self.ui.Koleksi.clicked.connect(self.toggle_koleksi_submenu)
    
    def toggle_kelola_submenu(self):
        self.ui.DataSubMenu.setVisible(not self.ui.DataSubMenu.isVisible())

    def toggle_koleksi_submenu(self):
        self.ui.KoleksiSubMenu.setVisible(not self.ui.KoleksiSubMenu.isVisible())
        
    def logout(self):
        # Displaying a message box on logout
        message_box = QMessageBox()
        message_box.setText("Anda telah logout")
        message_box.exec_()
        
        # Close the dashboard window
        self.close()
        
        # Import LoginWindow locally to avoid circular import
        from login import Login  # Local import to avoid circular import
        self.login = Login()
        self.login.show()