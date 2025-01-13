import os
import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox
from view.UI_Dashboard import Ui_UI_Dashboard
from model.dataAnggota import DataAnggotaPage
from model.dataBuku import DataBukuPage
from model.dataKoleksi import KoleksiBuku
from model.dataKoleksiFiksi import KoleksiFiksi
from model.dataKoleksiNonFiksi import KoleksiNonFiksi
from model.Home import homePage
from model.profile import profilePage 
from model.rakPinjam import rakPinjamPage

database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")
class Dashboard(QMainWindow):
    def __init__(self, role, user_id):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)
        
        # set user_id
        self.user_id = user_id

        # set role
        self.role = role
        
        # nama akun dan role sesuai user yang login
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            cursor.execute("SELECT Nama_lengkap, Role FROM User WHERE id = ?", (self.user_id,))
            result = cursor.fetchone()
            conn.close()
            self.ui.NamaAkun.setText(result[0])
            self.ui.Role.setText("Administrator" if result[1] == 1 else "Anggota")
            
            # set style role
            if result[1] == 0:
                self.ui.Role.setStyleSheet((u"font-size: 20px; font-weight: bold; text-align: center; color: #000000;\n"
"background-color: #00FFFF;"))
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")
            
        # setup halaman data anggota
        self.homePage = homePage()
        self.ui.stackedWidget.addWidget(self.homePage)
        # set halaman home sebagai halaman utama
        self.ui.stackedWidget.setCurrentWidget(self.homePage) 
        
        self.dataKoleksi = KoleksiBuku()
        self.ui.stackedWidget.addWidget(self.dataKoleksi)

        self.dataKoleksiFiksi = KoleksiFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiFiksi)

        self.dataKoleksiNonFiksi = KoleksiNonFiksi()
        self.ui.stackedWidget.addWidget(self.dataKoleksiNonFiksi)
        
        self.rakPinjam = rakPinjamPage()
        self.ui.stackedWidget.addWidget(self.rakPinjam)

        self.dataAnggota = DataAnggotaPage()
        self.ui.stackedWidget.addWidget(self.dataAnggota)

        self.dataBuku = DataBukuPage()
        self.ui.stackedWidget.addWidget(self.dataBuku)
        
        self.profilePage = profilePage(self.user_id)
        self.ui.stackedWidget.addWidget(self.profilePage)

        # connect buttons
        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.homePage))
        self.ui.Koleksi.clicked.connect(lambda checked: self.toggle_submenu(self.ui.KoleksiSubMenu) if checked else None)
        self.ui.Koleksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataKoleksi))
        self.ui.Fiksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiFiksi))
        self.ui.NonFiksi.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataKoleksiNonFiksi))
        self.ui.Pinjam.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.rakPinjam))
        self.ui.Data.clicked.connect(lambda checked: self.toggle_submenu(self.ui.DataSubMenu) if checked else None)
        self.ui.DataBuku.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataBuku))   
        self.ui.DataAnggota.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataAnggota))
        self.ui.Profile.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.profilePage))
        self.ui.Logout.clicked.connect(self.logout)
        
        # control ui admin dan anggota
        if self.role == 0:  # Anggota
            self.hide_admin_features()
        # if self.role == 1:  # Admin
        #     self.hide_pinjam()

    def hide_admin_features(self):
        # menyembunyikan fitur admin
        self.ui.Data.setVisible(False)
    
    def hide_pinjam(self):
        # menyembunyikan fitur pinjam
        self.ui.Pinjam.setVisible(False)
    
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