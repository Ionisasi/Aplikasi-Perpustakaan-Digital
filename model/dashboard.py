import os
import sqlite3
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from view.UI_Dashboard import Ui_UI_Dashboard
from model.dataAnggota import DataAnggotaPage
from model.dataBuku import DataBukuPage
from model.dataPinjam import DataPinjam
from model.dataKoleksi import KoleksiBuku
from model.dataKoleksiFiksi import KoleksiFiksi
from model.dataKoleksiNonFiksi import KoleksiNonFiksi
from model.Home import homePage
from model.profile import profilePage 
from model.rakPinjam import rakPinjamPage
from utils import resource_path

database_path = resource_path("database/perpusdigi.db")
class Dashboard(QMainWindow):
    def __init__(self, role, user_id):
        super().__init__()
        self.ui = Ui_UI_Dashboard()
        self.ui.setupUi(self)
        
        # set user_id
        self.user_id = user_id

        # set role
        self.role = role
        
        # nama akun, role, dan ikon sesuai user yang login
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            cursor.execute("SELECT Nama_lengkap, Role, jenis_kelamin FROM User WHERE id = ?", (self.user_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                # Set nama akun
                if hasattr(self.ui, 'NamaAkun'):
                    self.ui.NamaAkun.setText(result[0])
                else:
                    QMessageBox.warning(self, "Warning", "Element 'NamaAkun' tidak ditemukan dalam UI.")

                # Set role
                if hasattr(self.ui, 'Role'):
                    self.ui.Role.setText("Administrator" if result[1] == 1 else "Anggota")
                    # Set style role
                    if result[1] == 0:
                        self.ui.Role.setStyleSheet((
                            "font-size: 20px; font-weight: bold; text-align: center; color: #000000;"
                            "background-color: #00FFFF;"
                        ))
                else:
                    QMessageBox.warning(self, "Warning", "Element 'Role' tidak ditemukan dalam UI.")

                # Set ikon profil berdasarkan role dan gender
                icon_path = ""
                if result[1] == 1:  # Administrator
                    icon_path = "Asset/Icon/Admin_male.png" if result[2].lower() == 'l' else "Asset/Icon/Admin_female.png"
                else:  # Anggota
                    icon_path = "Asset/Icon/anggota_male.png" if result[2].lower() == 'l' else "Asset/Icon/anggota_female.png"

                # Set ikon pada QLabel IconProfile
                if hasattr(self.ui, 'IconProfile'):
                    profile_icon = QPixmap(icon_path)
                    self.ui.IconProfile.setPixmap(profile_icon)
                    self.ui.IconProfile.setScaledContents(True)
                else:
                    QMessageBox.warning(self, "Warning", "Element 'IconProfile' tidak ditemukan dalam UI.")
            else:
                QMessageBox.critical(self, "Error", "User data not found.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")


        # setup halaman data anggota
        self.homePage = homePage(self.user_id)
        self.ui.stackedWidget.addWidget(self.homePage)
        # set halaman home sebagai halaman utama
        self.ui.stackedWidget.setCurrentWidget(self.homePage) 
        
        self.dataKoleksi = KoleksiBuku(self.user_id)
        self.ui.stackedWidget.addWidget(self.dataKoleksi)

        self.dataKoleksiFiksi = KoleksiFiksi(self.user_id)
        self.ui.stackedWidget.addWidget(self.dataKoleksiFiksi)

        self.dataKoleksiNonFiksi = KoleksiNonFiksi(self.user_id)
        self.ui.stackedWidget.addWidget(self.dataKoleksiNonFiksi)
        
        self.rakPinjam = rakPinjamPage(self.user_id)
        self.ui.stackedWidget.addWidget(self.rakPinjam)

        self.dataAnggota = DataAnggotaPage()
        self.ui.stackedWidget.addWidget(self.dataAnggota)

        self.dataBuku = DataBukuPage()
        self.ui.stackedWidget.addWidget(self.dataBuku)  
        
        self.dataPinjam = DataPinjam()
        self.ui.stackedWidget.addWidget(self.dataPinjam)
        
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
        self.ui.DataPinjam.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.dataPinjam))
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
            icon = QIcon('Asset/Icon/Buku.png')
            message_box.setWindowIcon(icon)
            message_box.setText("Anda telah logout")
            message_box.exec_()

            # Tutup jendela dashboard
            self.close()

            # Import LoginWindow dan tampilkan
            from Main import Login
            self.login = Login()
            self.login.show()