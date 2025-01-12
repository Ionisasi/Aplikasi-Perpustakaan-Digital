from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_UI_Dashboard
from model.dataAnggota import DataAnggotaPage
from model.dataBuku import DataBukuPage
from model.dataKoleksiFiksi import KoleksiFiksi
from model.dataKoleksiNonFiksi import KoleksiNonFiksi
from model.Home import homePage
from model.profile import profilePage 


class Dashboard(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)

        # set role
        self.role = role

        # setup halaman data anggota
        self.homePage = homePage()
        self.ui.stackedWidget.addWidget(self.homePage)

        self.dataKoleksiFiksi = KoleksiFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiFiksi)

        self.dataKoleksiNonFiksi = KoleksiNonFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiNonFiksi)

        self.dataAnggota = DataAnggotaPage()
        self.ui.stackedWidget.addWidget(self.dataAnggota)

        self.dataBuku = DataBukuPage()
        self.ui.stackedWidget.addWidget(self.dataBuku)

        self.dataKoleksiFiksi = KoleksiFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiFiksi)
        
        self.dataKoleksiNonFiksi = KoleksiNonFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiNonFiksi)
        
        self.profilePage = profilePage()
        self.ui.stackedWidget.addWidget(self.profilePage)

        # connect buttons
        self.ui.Logout.clicked.connect(self.logout)
        self.ui.Data.clicked.connect(lambda checked: self.toggle_submenu(self.ui.DataSubMenu) if checked else None)
        self.ui.Koleksi.clicked.connect(lambda checked: self.toggle_submenu(self.ui.KoleksiSubMenu) if checked else None)
        self.ui.DataAnggota.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataAnggota))
        self.ui.DataBuku.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataBuku))   
        self.ui.Fiksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiFiksi))
        self.ui.NonFiksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiNonFiksi))
        self.ui.Profile.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.profilePage))
        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.homePage))
        
        # control ui admin dan anggota
        if self.role == 0:  # Anggota
            self.hide_admin_features()

    def hide_admin_features(self):
        # menyembunyikan fitur admin
        self.ui.Data.setVisible(False)
    
    def show_homepage(self):
        # menampilkan halaman koleksi buku nonfiksi
        self.ui.stackedWidget.setCurrentWidget(self.homePage)

    def toggle_submenu(self, submenu):
        # menampilkan atau menyembunyikan submenu
        submenu.setVisible(not submenu.isVisible())

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