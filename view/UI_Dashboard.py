# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import os
def get_icon_path(icon_name):
    # Mendapatkan path absolut ke folder Icon
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'Asset', 'Icon', icon_name)
    return os.path.abspath(icon_path)
class Ui_UI_Dashboard(object):
    def setupUi(self, UI_Dashboard):
        if not UI_Dashboard.objectName():
            UI_Dashboard.setObjectName(u"UI_Dashboard")
        UI_Dashboard.resize(1080, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UI_Dashboard.sizePolicy().hasHeightForWidth())
        UI_Dashboard.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(UI_Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u".QWidget{\n"
"background-color: rgb(0, 33, 48);\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLabel = QWidget(self.centralwidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        sizePolicy.setHeightForWidth(self.HeaderLabel.sizePolicy().hasHeightForWidth())
        self.HeaderLabel.setSizePolicy(sizePolicy)
        self.HeaderLabel.setMaximumSize(QSize(16777215, 100))
        self.HeaderLabel.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.horizontalLayout = QHBoxLayout(self.HeaderLabel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_label = QLabel(self.HeaderLabel)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMaximumSize(QSize(70, 70))
        self.icon_label.setPixmap(QPixmap(get_icon_path("Buku.png")))
        self.icon_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_label)

        self.title_label = QLabel(self.HeaderLabel)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"font-size: 26px; font-weight: bold; text-align: center; color: #ffffff;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.title_label)


        self.gridLayout.addWidget(self.HeaderLabel, 0, 0, 1, 3)

        self.profileWidget = QWidget(self.centralwidget)
        self.profileWidget.setObjectName(u"profileWidget")
        self.profileWidget.setEnabled(True)
        self.profileWidget.setMinimumSize(QSize(0, 70))
        self.profileWidget.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.profileWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.IconProfile = QLabel(self.profileWidget)
        self.IconProfile.setObjectName(u"IconProfile")
        self.IconProfile.setMaximumSize(QSize(70, 70))
        self.IconProfile.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.IconProfile.setPixmap(QPixmap(get_icon_path("Admin1.png")))
        self.IconProfile.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.IconProfile)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.NamaAkun = QLabel(self.profileWidget)
        self.NamaAkun.setObjectName(u"NamaAkun")
        self.NamaAkun.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: center; color: #ffffff;")
        self.NamaAkun.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.NamaAkun)

        self.Role = QLabel(self.profileWidget)
        self.Role.setObjectName(u"Role")
        self.Role.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: center; color: #000000;\n"
"background-color: rgb(255, 255, 0);")
        self.Role.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.Role)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.profileWidget, 1, 0, 2, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.sidebar = QWidget()
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 298, 518))
        self.sidebar.setMinimumSize(QSize(280, 0))
        self.sidebar.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar.setStyleSheet(u"background-color: rgb(0, 33, 48);")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu1 = QLabel(self.sidebar)
        self.Menu1.setObjectName(u"Menu1")
        self.Menu1.setMinimumSize(QSize(0, 40))
        self.Menu1.setMaximumSize(QSize(16777215, 40))
        self.Menu1.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: center; color: #555555;\n"
"background-color: rgb(0, 24, 35);")
        self.Menu1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Menu1)

        self.home = QPushButton(self.sidebar)
        self.buttonGroup = QButtonGroup(UI_Dashboard)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.home)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(0, 40))
        self.home.setMaximumSize(QSize(16777215, 40))
        self.home.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border:tranparanted\n"
"")
        icon = QIcon()
        icon.addFile(get_icon_path("home.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home.setIcon(icon)
        self.home.setCheckable(True)
        self.home.setChecked(True)

        self.verticalLayout.addWidget(self.home)

        self.Koleksi = QPushButton(self.sidebar)
        self.buttonGroup.addButton(self.Koleksi)
        self.Koleksi.setObjectName(u"Koleksi")
        self.Koleksi.setMinimumSize(QSize(0, 40))
        self.Koleksi.setMaximumSize(QSize(16777215, 40))
        self.Koleksi.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(get_icon_path("koleksi.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Koleksi.setIcon(icon1)
        self.Koleksi.setCheckable(True)

        self.verticalLayout.addWidget(self.Koleksi)

        self.KoleksiSubMenu = QWidget(self.sidebar)
        self.KoleksiSubMenu.setObjectName(u"KoleksiSubMenu")
        self.KoleksiSubMenu.setMaximumSize(QSize(16777215, 90))
        self.verticalLayout_4 = QVBoxLayout(self.KoleksiSubMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 0, 0, 0)
        self.Fiksi = QPushButton(self.KoleksiSubMenu)
        self.buttonGroup.addButton(self.Fiksi)
        self.Fiksi.setObjectName(u"Fiksi")
        self.Fiksi.setMinimumSize(QSize(0, 40))
        self.Fiksi.setMaximumSize(QSize(16777215, 40))
        self.Fiksi.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        icon2 = QIcon()
        icon2.addFile(get_icon_path("book.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Fiksi.setIcon(icon2)
        self.Fiksi.setCheckable(True)

        self.verticalLayout_4.addWidget(self.Fiksi)

        self.NonFiksi = QPushButton(self.KoleksiSubMenu)
        self.buttonGroup.addButton(self.NonFiksi)
        self.NonFiksi.setObjectName(u"NonFiksi")
        self.NonFiksi.setMinimumSize(QSize(0, 40))
        self.NonFiksi.setMaximumSize(QSize(16777215, 40))
        self.NonFiksi.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        self.NonFiksi.setIcon(icon2)
        self.NonFiksi.setCheckable(True)

        self.verticalLayout_4.addWidget(self.NonFiksi)


        self.verticalLayout.addWidget(self.KoleksiSubMenu)

        pinjam_icon = QIcon(get_icon_path('bookshelf.png'))
        self.Pinjam = QPushButton(self.sidebar)
        self.Pinjam.setObjectName(u"Pinjam")
        self.buttonGroup.addButton(self.Pinjam)
        self.Pinjam.setMinimumSize(QSize(0, 40))
        self.Pinjam.setMaximumSize(QSize(16777215, 40))
        self.Pinjam.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border:tranparanted\n"
"")
        self.Pinjam.setIcon(pinjam_icon)
        self.Pinjam.setCheckable(True)

        self.verticalLayout.addWidget(self.Pinjam)

        self.Data = QPushButton(self.sidebar)
        self.buttonGroup.addButton(self.Data)
        self.Data.setObjectName(u"Data")
        self.Data.setMinimumSize(QSize(0, 40))
        self.Data.setMaximumSize(QSize(16777215, 40))
        self.Data.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        icon3 = QIcon()
        icon3.addFile(get_icon_path("open-folder.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Data.setIcon(icon3)
        self.Data.setCheckable(True)

        self.verticalLayout.addWidget(self.Data)

        self.DataSubMenu = QWidget(self.sidebar)
        self.DataSubMenu.setObjectName(u"DataSubMenu")
        self.DataSubMenu.setMaximumSize(QSize(16777215, 135))
        self.verticalLayout_5 = QVBoxLayout(self.DataSubMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 0, 0, 0)
        self.DataBuku = QPushButton(self.DataSubMenu)
        self.buttonGroup.addButton(self.DataBuku)
        self.DataBuku.setObjectName(u"DataBuku")
        self.DataBuku.setMinimumSize(QSize(0, 40))
        self.DataBuku.setMaximumSize(QSize(16777215, 40))
        self.DataBuku.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        self.DataBuku.setIcon(icon2)
        self.DataBuku.setCheckable(True)

        self.verticalLayout_5.addWidget(self.DataBuku)

        self.DataAnggota = QPushButton(self.DataSubMenu)
        self.buttonGroup.addButton(self.DataAnggota)
        self.DataAnggota.setObjectName(u"DataAnggota")
        self.DataAnggota.setMinimumSize(QSize(0, 40))
        self.DataAnggota.setMaximumSize(QSize(16777215, 40))
        self.DataAnggota.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        icon4 = QIcon()
        icon4.addFile(get_icon_path("user.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DataAnggota.setIcon(icon4)
        self.DataAnggota.setCheckable(True)

        self.verticalLayout_5.addWidget(self.DataAnggota)
        
        self.DataPinjam = QPushButton(self.DataSubMenu)
        self.buttonGroup.addButton(self.DataPinjam)
        self.DataPinjam.setObjectName(u"DataBuku")
        self.DataPinjam.setMinimumSize(QSize(0, 40))
        self.DataPinjam.setMaximumSize(QSize(16777215, 40))
        self.DataPinjam.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        self.DataPinjam.setIcon(icon2)
        self.DataPinjam.setCheckable(True)

        self.verticalLayout_5.addWidget(self.DataPinjam)


        self.verticalLayout.addWidget(self.DataSubMenu)

        self.Menu2 = QLabel(self.sidebar)
        self.Menu2.setObjectName(u"Menu2")
        self.Menu2.setMinimumSize(QSize(0, 40))
        self.Menu2.setMaximumSize(QSize(16777215, 40))
        self.Menu2.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: center; color: #555555;\n"
"background-color: rgb(0, 24, 35);")
        self.Menu2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Menu2)

        self.Profile = QPushButton(self.sidebar)
        self.buttonGroup.addButton(self.Profile)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setMinimumSize(QSize(0, 40))
        self.Profile.setMaximumSize(QSize(16777215, 40))
        self.Profile.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        self.Profile.setIcon(icon4)
        self.Profile.setCheckable(True)

        self.verticalLayout.addWidget(self.Profile)

        self.Logout = QPushButton(self.sidebar)
        self.buttonGroup.addButton(self.Logout)
        self.Logout.setObjectName(u"Logout")
        self.Logout.setMinimumSize(QSize(0, 40))
        self.Logout.setMaximumSize(QSize(16777215, 40))
        self.Logout.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;padding-left: 20px;border: none;\n"
"")
        icon5 = QIcon()
        icon5.addFile(get_icon_path("logout.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Logout.setIcon(icon5)
        self.Logout.setCheckable(True)

        self.verticalLayout.addWidget(self.Logout)

        self.scrollArea.setWidget(self.sidebar)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.stackedWidget.addWidget(self.page3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.stackedWidget.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.stackedWidget.addWidget(self.page6)
        self.page7 = QWidget()
        self.page7.setObjectName(u"page7")
        self.stackedWidget.addWidget(self.page7)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 3, 1)
        
        self.KoleksiSubMenu.setVisible(False)
        self.DataSubMenu.setVisible(False)
        
        # style for ButtonGroup
        styleButtonGroup = """
        QPushButton {
                font-size: 20px;
                font-weight: bold;
                color: #ffffff;
                text-align: left;
                padding-left: 20px;
                border: none;
        }
        QPushButton:checked {
                background-color: rgb(0, 100, 200);
                color: #ffffff;
        }
        QPushButton:hover {
                background-color: rgb(0, 50, 100);
        }
        """

        # Menerapkan QSS pada tombol di grup
        for button in self.buttonGroup.buttons():
                button.setStyleSheet(styleButtonGroup)

        UI_Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(UI_Dashboard)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(UI_Dashboard)
    # setupUi

    def retranslateUi(self, UI_Dashboard):
        w_icon = QIcon('Asset/Icon/Buku.png')
        UI_Dashboard.setWindowTitle(QCoreApplication.translate("UI_Dashboard", u"Perpustakaan Digital", None))
        UI_Dashboard.setWindowIcon(w_icon)
        self.icon_label.setText("")
        self.title_label.setText(QCoreApplication.translate("UI_Dashboard", u"Perpustakaan Digital\n"
"      Kelompok 2", None))
        self.IconProfile.setText("")
        self.NamaAkun.setText(QCoreApplication.translate("UI_Dashboard", u"Ryan", None))
        self.Role.setText(QCoreApplication.translate("UI_Dashboard", u"Administrator", None))
        self.Menu1.setText(QCoreApplication.translate("UI_Dashboard", u"Main Navigation", None))
        self.home.setText(QCoreApplication.translate("UI_Dashboard", u"Home", None))
        self.Koleksi.setText(QCoreApplication.translate("UI_Dashboard", u"Koleksi", None))
        self.Fiksi.setText(QCoreApplication.translate("UI_Dashboard", u"Fiksi", None))
        self.NonFiksi.setText(QCoreApplication.translate("UI_Dashboard", u"Non Fiksi", None))
        self.Pinjam.setText(QCoreApplication.translate("UI_Dashboard", u"Rak Pinjam", None))
        self.Data.setText(QCoreApplication.translate("UI_Dashboard", u"Kelola Data", None))
        self.DataBuku.setText(QCoreApplication.translate("UI_Dashboard", u"Data Buku", None))
        self.DataAnggota.setText(QCoreApplication.translate("UI_Dashboard", u"Data Anggota", None))
        self.DataPinjam.setText(QCoreApplication.translate("UI_Dashboard", u"Data Pinjaman", None))
        self.Menu2.setText(QCoreApplication.translate("UI_Dashboard", u"Settings", None))
        self.Profile.setText(QCoreApplication.translate("UI_Dashboard", u"Profile", None))
        self.Logout.setText(QCoreApplication.translate("UI_Dashboard", u"Logout", None))
    # retranslateUi

