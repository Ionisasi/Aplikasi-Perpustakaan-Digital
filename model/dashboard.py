from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_Dashboard

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        # connect buttons
        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.kelola_button.clicked.connect(self.toggle_kelola_submenu)
        self.ui.koleksi_button.clicked.connect(self.toggle_koleksi_submenu)

        # Mengatur eksklusivitas tombol
        for button in self.ui.sidebar_buttons:
            button.clicked.connect(lambda checked, btn=button: self.on_sidebar_button_click(btn))
    
    def toggle_kelola_submenu(self):
        self.ui.kelola_submenu.setVisible(not self.ui.kelola_submenu.isVisible())

    def toggle_koleksi_submenu(self):
        self.ui.koleksi_submenu.setVisible(not self.ui.koleksi_submenu.isVisible())

    def on_sidebar_button_click(self, clicked_button):
        for button in self.ui.sidebar_buttons:
            if button != clicked_button:
                button.setChecked(False)
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
