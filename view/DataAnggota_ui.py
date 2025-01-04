# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataAnggota.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerTitle = QLabel(Form)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
        self.headerTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.headerTitle)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.MainContent = QWidget()
        self.MainContent.setObjectName(u"MainContent")
        self.MainContent.setGeometry(QRect(0, 0, 780, 529))
        self.MainContent.setStyleSheet(u".QWidget{\n"
"background-color: rgb(0, 33, 48);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.MainContent)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LeftSide = QWidget(self.MainContent)
        self.LeftSide.setObjectName(u"LeftSide")
        self.LeftSide.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.LeftSide)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EditForm = QWidget(self.LeftSide)
        self.EditForm.setObjectName(u"EditForm")
        self.gridLayout = QGridLayout(self.EditForm)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 20, 10, 0)
        self.Email = QFrame(self.EditForm)
        self.Email.setObjectName(u"Email")
        self.Email.setMaximumSize(QSize(150, 40))
        self.horizontalLayout = QHBoxLayout(self.Email)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.EmailLabel = QLabel(self.Email)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setMinimumSize(QSize(120, 30))
        self.EmailLabel.setMaximumSize(QSize(120, 30))
        font1 = QFont()
        font1.setBold(True)
        self.EmailLabel.setFont(font1)
        self.EmailLabel.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.horizontalLayout.addWidget(self.EmailLabel)

        self.titik2_2 = QLabel(self.Email)
        self.titik2_2.setObjectName(u"titik2_2")
        self.titik2_2.setMinimumSize(QSize(10, 30))
        self.titik2_2.setMaximumSize(QSize(10, 30))
        self.titik2_2.setFont(font1)
        self.titik2_2.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;")

        self.horizontalLayout.addWidget(self.titik2_2)


        self.gridLayout.addWidget(self.Email, 1, 0, 1, 1)

        self.lakiCheckBox = QCheckBox(self.EditForm)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.lakiCheckBox)
        self.lakiCheckBox.setObjectName(u"lakiCheckBox")
        self.lakiCheckBox.setFont(font1)
        self.lakiCheckBox.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")
        self.lakiCheckBox.setCheckable(True)
        self.lakiCheckBox.setChecked(False)

        self.gridLayout.addWidget(self.lakiCheckBox, 4, 1, 1, 1)

        self.teleponInput = QLineEdit(self.EditForm)
        self.teleponInput.setObjectName(u"teleponInput")
        self.teleponInput.setMinimumSize(QSize(150, 30))
        self.teleponInput.setMaximumSize(QSize(16777215, 30))
        self.teleponInput.setFont(font1)
        self.teleponInput.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.gridLayout.addWidget(self.teleponInput, 3, 1, 1, 2)

        self.alamatInput = QTextEdit(self.EditForm)
        self.alamatInput.setObjectName(u"alamatInput")
        self.alamatInput.setMinimumSize(QSize(150, 40))
        self.alamatInput.setMaximumSize(QSize(16777215, 16777215))
        self.alamatInput.setFont(font1)
        self.alamatInput.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.gridLayout.addWidget(self.alamatInput, 5, 1, 1, 2)

        self.Alamat = QFrame(self.EditForm)
        self.Alamat.setObjectName(u"Alamat")
        self.Alamat.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(15)
        self.Alamat.setFont(font2)
        self.alamat = QHBoxLayout(self.Alamat)
        self.alamat.setObjectName(u"alamat")
        self.alamat.setContentsMargins(9, 9, 9, 9)
        self.alamatLabel = QLabel(self.Alamat)
        self.alamatLabel.setObjectName(u"alamatLabel")
        self.alamatLabel.setMinimumSize(QSize(120, 30))
        self.alamatLabel.setMaximumSize(QSize(120, 30))
        self.alamatLabel.setFont(font1)
        self.alamatLabel.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; border: none;\n"
"")

        self.alamat.addWidget(self.alamatLabel)

        self.titik2_5 = QLabel(self.Alamat)
        self.titik2_5.setObjectName(u"titik2_5")
        self.titik2_5.setMinimumSize(QSize(10, 30))
        self.titik2_5.setMaximumSize(QSize(10, 30))
        self.titik2_5.setFont(font1)
        self.titik2_5.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;")

        self.alamat.addWidget(self.titik2_5)


        self.gridLayout.addWidget(self.Alamat, 5, 0, 1, 1)

        self.emailInput = QLineEdit(self.EditForm)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(150, 30))
        self.emailInput.setMaximumSize(QSize(16777215, 30))
        self.emailInput.setFont(font1)
        self.emailInput.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.gridLayout.addWidget(self.emailInput, 1, 1, 1, 2)

        self.jenisKelamin = QFrame(self.EditForm)
        self.jenisKelamin.setObjectName(u"jenisKelamin")
        self.jenisKelamin.setMaximumSize(QSize(150, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.jenisKelamin)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.jkLabel = QLabel(self.jenisKelamin)
        self.jkLabel.setObjectName(u"jkLabel")
        self.jkLabel.setMinimumSize(QSize(120, 30))
        self.jkLabel.setMaximumSize(QSize(120, 30))
        self.jkLabel.setFont(font1)
        self.jkLabel.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; border: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.jkLabel)

        self.titik2_3 = QLabel(self.jenisKelamin)
        self.titik2_3.setObjectName(u"titik2_3")
        self.titik2_3.setMinimumSize(QSize(10, 30))
        self.titik2_3.setMaximumSize(QSize(10, 30))
        self.titik2_3.setFont(font1)
        self.titik2_3.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;")

        self.horizontalLayout_4.addWidget(self.titik2_3)


        self.gridLayout.addWidget(self.jenisKelamin, 4, 0, 1, 1)

        self.Nama = QFrame(self.EditForm)
        self.Nama.setObjectName(u"Nama")
        self.Nama.setMaximumSize(QSize(150, 16777215))
        self.NamaFrame = QHBoxLayout(self.Nama)
        self.NamaFrame.setObjectName(u"NamaFrame")
        self.NamaLabel = QLabel(self.Nama)
        self.NamaLabel.setObjectName(u"NamaLabel")
        self.NamaLabel.setMinimumSize(QSize(120, 30))
        self.NamaLabel.setMaximumSize(QSize(120, 30))
        self.NamaLabel.setFont(font1)
        self.NamaLabel.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.NamaFrame.addWidget(self.NamaLabel)

        self.titik2 = QLabel(self.Nama)
        self.titik2.setObjectName(u"titik2")
        self.titik2.setMinimumSize(QSize(10, 30))
        self.titik2.setMaximumSize(QSize(10, 30))
        self.titik2.setFont(font1)
        self.titik2.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;")

        self.NamaFrame.addWidget(self.titik2)


        self.gridLayout.addWidget(self.Nama, 0, 0, 1, 1)

        self.namaInput = QLineEdit(self.EditForm)
        self.namaInput.setObjectName(u"namaInput")
        self.namaInput.setMinimumSize(QSize(150, 30))
        self.namaInput.setMaximumSize(QSize(16777215, 30))
        self.namaInput.setFont(font1)
        self.namaInput.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")
        self.namaInput.setFrame(True)

        self.gridLayout.addWidget(self.namaInput, 0, 1, 1, 2)

        self.Telepon = QFrame(self.EditForm)
        self.Telepon.setObjectName(u"Telepon")
        self.Telepon.setMaximumSize(QSize(150, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.Telepon)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.telpLabel = QLabel(self.Telepon)
        self.telpLabel.setObjectName(u"telpLabel")
        self.telpLabel.setMinimumSize(QSize(120, 30))
        self.telpLabel.setMaximumSize(QSize(120, 30))
        self.telpLabel.setFont(font1)
        self.telpLabel.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.horizontalLayout_2.addWidget(self.telpLabel)

        self.titik2_4 = QLabel(self.Telepon)
        self.titik2_4.setObjectName(u"titik2_4")
        self.titik2_4.setMinimumSize(QSize(10, 30))
        self.titik2_4.setMaximumSize(QSize(10, 30))
        self.titik2_4.setFont(font1)
        self.titik2_4.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;")

        self.horizontalLayout_2.addWidget(self.titik2_4)


        self.gridLayout.addWidget(self.Telepon, 3, 0, 1, 1)

        self.PerempuanCheckBox = QCheckBox(self.EditForm)
        self.buttonGroup.addButton(self.PerempuanCheckBox)
        self.PerempuanCheckBox.setObjectName(u"PerempuanCheckBox")
        self.PerempuanCheckBox.setFont(font1)
        self.PerempuanCheckBox.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff; \n"
"")

        self.gridLayout.addWidget(self.PerempuanCheckBox, 4, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.EditForm)

        self.editBtn = QWidget(self.LeftSide)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(0, 150))
        self.editBtn.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 50, 100);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.editBtn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.searchBtn = QPushButton(self.editBtn)
        self.editBtnGroup = QButtonGroup(Form)
        self.editBtnGroup.setObjectName(u"editBtnGroup")
        self.editBtnGroup.addButton(self.searchBtn)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(0, 40))
        self.searchBtn.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: rgb(0, 255, 255); padding-left: 20px;border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u"../Asset/Icon/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setIconSize(QSize(20, 20))
        self.searchBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.searchBtn)

        self.ubahBtn = QPushButton(self.editBtn)
        self.editBtnGroup.addButton(self.ubahBtn)
        self.ubahBtn.setObjectName(u"ubahBtn")
        self.ubahBtn.setMinimumSize(QSize(0, 40))
        self.ubahBtn.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: rgb(26, 255, 0); padding-left: 20px;border: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../Asset/Icon/change.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ubahBtn.setIcon(icon1)
        self.ubahBtn.setIconSize(QSize(20, 20))
        self.ubahBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.ubahBtn)

        self.deleteBtn = QPushButton(self.editBtn)
        self.editBtnGroup.addButton(self.deleteBtn)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMinimumSize(QSize(0, 40))
        self.deleteBtn.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: rgb(255, 0, 0); padding-left: 20px;border: none;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../Asset/Icon/Delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteBtn.setIcon(icon2)
        self.deleteBtn.setIconSize(QSize(20, 20))
        self.deleteBtn.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.deleteBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.deselectBtn = QPushButton(self.editBtn)
        self.editBtnGroup.addButton(self.deselectBtn)
        self.deselectBtn.setObjectName(u"deselectBtn")
        self.deselectBtn.setMinimumSize(QSize(0, 50))
        self.deselectBtn.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: center; color: rgb(255, 255, 0); padding-left: 20px; border: none;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../Asset/Icon/Deselect.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deselectBtn.setIcon(icon3)
        self.deselectBtn.setIconSize(QSize(20, 20))
        self.deselectBtn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.deselectBtn)


        self.verticalLayout_2.addWidget(self.editBtn)


        self.horizontalLayout_3.addWidget(self.LeftSide)

        self.AnggotaTable = QTableWidget(self.MainContent)
        if (self.AnggotaTable.columnCount() < 5):
            self.AnggotaTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.AnggotaTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.AnggotaTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.AnggotaTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.AnggotaTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.AnggotaTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.AnggotaTable.setObjectName(u"AnggotaTable")
        self.AnggotaTable.setMinimumSize(QSize(410, 0))
        self.AnggotaTable.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.AnggotaTable.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: left; color: #ffffff;\n"
"")
        self.AnggotaTable.setFrameShape(QFrame.Shape.NoFrame)
        self.AnggotaTable.setFrameShadow(QFrame.Shadow.Plain)
        self.AnggotaTable.setAutoScroll(True)
        self.AnggotaTable.setAutoScrollMargin(15)
        self.AnggotaTable.setTabKeyNavigation(True)
        self.AnggotaTable.setAlternatingRowColors(False)
        self.AnggotaTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.AnggotaTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.AnggotaTable.setShowGrid(True)
        self.AnggotaTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.AnggotaTable.setRowCount(0)
        self.AnggotaTable.horizontalHeader().setVisible(True)
        self.AnggotaTable.horizontalHeader().setCascadingSectionResizes(True)
        self.AnggotaTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.AnggotaTable.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.AnggotaTable)

        self.horizontalLayout_3.setStretch(0, 1)
        self.scrollArea.setWidget(self.MainContent)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.headerTitle.setText(QCoreApplication.translate("Form", u"DATA ANGGOTA", None))
        self.EmailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.titik2_2.setText(QCoreApplication.translate("Form", u":", None))
        self.lakiCheckBox.setText(QCoreApplication.translate("Form", u"Laki-laki", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.titik2_5.setText(QCoreApplication.translate("Form", u":", None))
        self.jkLabel.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.titik2_3.setText(QCoreApplication.translate("Form", u":", None))
        self.NamaLabel.setText(QCoreApplication.translate("Form", u"Nama Lengkap", None))
        self.titik2.setText(QCoreApplication.translate("Form", u":", None))
        self.namaInput.setText("")
        self.telpLabel.setText(QCoreApplication.translate("Form", u"Telepon", None))
        self.titik2_4.setText(QCoreApplication.translate("Form", u":", None))
        self.PerempuanCheckBox.setText(QCoreApplication.translate("Form", u"Perempuan", None))
        self.searchBtn.setText(QCoreApplication.translate("Form", u"Cari", None))
        self.ubahBtn.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.deleteBtn.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.deselectBtn.setText(QCoreApplication.translate("Form", u"Batalkan Pilihan", None))
        ___qtablewidgetitem = self.AnggotaTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem1 = self.AnggotaTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem2 = self.AnggotaTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"No. Telepon", None));
        ___qtablewidgetitem3 = self.AnggotaTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem4 = self.AnggotaTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Alamat", None));
    # retranslateUi

