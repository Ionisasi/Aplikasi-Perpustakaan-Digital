from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_Dashboard

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        # connect buttons
        self.ui.logout_button.clicked.connect(self.logout)

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
