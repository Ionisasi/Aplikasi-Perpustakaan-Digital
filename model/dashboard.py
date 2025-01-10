from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_UI_Dashboard
from model.dataAnggota import DataAnggotaPage
from model.dataBuku import DataBukuPage
from model.dataKoleksiFiksi import KoleksiFiksi
from model.dataKoleksiNonFiksi import KoleksiNonFiksi

class Dashboard(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)

        # set role
        self.role = role
        
        # setup halaman data anggota
        self.dataAnggota = DataAnggotaPage()
        self.ui.stackedWidget.addWidget(self.dataAnggota)
        
        self.dataBuku = DataBukuPage()
        self.ui.stackedWidget.addWidget(self.dataBuku)
        
        self.dataKoleksiFiksi = KoleksiFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiFiksi)
        
        self.dataKoleksiNonFiksi = KoleksiNonFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiNonFiksi)

        # connect buttons
        self.ui.Logout.clicked.connect(self.logout)
        self.ui.Data.clicked.connect(lambda checked: self.toggle_submenu(self.ui.DataSubMenu) if checked else None)
        self.ui.Koleksi.clicked.connect(lambda checked: self.toggle_submenu(self.ui.KoleksiSubMenu) if checked else None)
        self.ui.DataAnggota.clicked.connect(self.show_data_anggota)
        self.ui.DataBuku.clicked.connect(self.show_data_buku)
        self.ui.Fiksi.clicked.connect(self.show_fiksi)
        self.ui.NonFiksi.clicked.connect(self.show_nonfiksi)
        
        # control ui admin dan anggota
        if self.role == 0:  # Anggota
            self.hide_admin_features()
    
    def hide_admin_features(self):
        # menyembunyikan fitur admin
        self.ui.Data.setVisible(False)

    def toggle_submenu(self, submenu):
        # menampilkan atau menyembunyikan submenu
        submenu.setVisible(not submenu.isVisible())
    
    def show_data_anggota(self):
        # menampilkan halaman data anggota
        self.ui.stackedWidget.setCurrentWidget(self.dataAnggota)
    
    def show_data_buku(self):
        # menampilkan halaman data buku
        self.ui.stackedWidget.setCurrentWidget(self.dataBuku)
    
    def show_fiksi(self):
        # menampilkan halaman koleksi buku fiksi
        self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiFiksi)
        
    def show_nonfiksi(self):
        # menampilkan halaman koleksi buku nonfiksi
        self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiNonFiksi)

    def logout(self):
        # Konfirmasi sebelum logout
        reply = QMessageBox.question(
            self,
            "Konfirmasi Logout",
            "Apakah Anda yakin ingin logout?",
            QMessageBox.Yes | QMessageBox.No,
            
        )

        if reply == QMessageBox.Yes:
            # Menampilkan pesan logout
            message_box = QMessageBox()
            message_box.setText("Anda telah logout")
            message_box.exec_()

            # Tutup jendela dashboard
            self.close()

            # Import LoginWindow dan tampilkan
            from Main import Login
            self.login = Login()
            self.login.show()