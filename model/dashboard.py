from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_UI_Dashboard
from model.dataAnggota import DataAnggotaPage

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)
        
        self.dataAnggota = DataAnggotaPage()
        self.ui.stackedWidget.addWidget(self.dataAnggota)

        # connect buttons
        self.ui.Logout.clicked.connect(self.logout)
        self.ui.Data.clicked.connect(lambda checked: self.toggle_submenu(self.ui.DataSubMenu) if checked else None)
        self.ui.Koleksi.clicked.connect(lambda checked: self.toggle_submenu(self.ui.KoleksiSubMenu) if checked else None)
        self.ui.DataAnggota.clicked.connect(self.show_data_anggota)

    def toggle_submenu(self, submenu):
        # menampilkan atau menyembunyikan submenu
        submenu.setVisible(not submenu.isVisible())
    
    def show_data_anggota(self):
        # menampilkan halaman data anggota
        self.ui.stackedWidget.setCurrentWidget(self.dataAnggota)

    def logout(self):
        # Masih sementara, belum ada konfirmasi logout
        message_box = QMessageBox()
        message_box.setText("Anda telah logout")
        message_box.exec_()
        
        # Close the dashboard window
        self.close()
        
        # Import LoginWindow dan tampilkan
        from Main import Login
        self.login = Login()
        self.login.show()