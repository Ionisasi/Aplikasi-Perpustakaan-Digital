# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 565)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.headerTitle = QLabel(Form)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 255, 0);")
        self.headerTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.headerTitle)

        self.IsiFrame = QFrame(Form)
        self.IsiFrame.setObjectName(u"IsiFrame")
        self.IsiFrame.setStyleSheet(u".QFrame {\n"
"background-color: rgb(0, 33, 48);\n"
"}\n"
"QLineEdit, QTextEdit{\n"
"background-color: rgb(46, 47, 48);\n"
"}\n"
"QFrame{\n"
"font-weight: bold; color: #ffffff;}\n"
"QCheckBox::indicator:unchecked{background-color : rgb(46, 47, 48);}")
        self.gridLayout = QGridLayout(self.IsiFrame)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.emailLabel = QLabel(self.IsiFrame)
        self.emailLabel.setObjectName(u"emailLabel")

        self.gridLayout.addWidget(self.emailLabel, 3, 0, 1, 1)

        self.PerempuanCheckBox = QCheckBox(self.IsiFrame)
        self.PerempuanCheckBox.setObjectName(u"PerempuanCheckBox")
        self.PerempuanCheckBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PerempuanCheckBox.sizePolicy().hasHeightForWidth())
        self.PerempuanCheckBox.setSizePolicy(sizePolicy)
        self.PerempuanCheckBox.setMaximumSize(QSize(16777215, 16777211))
        self.PerempuanCheckBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.PerempuanCheckBox, 8, 3, 1, 1)

        self.teleponInput = QLineEdit(self.IsiFrame)
        self.teleponInput.setObjectName(u"teleponInput")

        self.gridLayout.addWidget(self.teleponInput, 6, 2, 1, 2)

        self.passwordInput = QLineEdit(self.IsiFrame)
        self.passwordInput.setObjectName(u"passwordInput")

        self.gridLayout.addWidget(self.passwordInput, 4, 2, 1, 2)

        self.passwordLabel = QLabel(self.IsiFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 4, 0, 1, 1)

        self.alamatLabel = QLabel(self.IsiFrame)
        self.alamatLabel.setObjectName(u"alamatLabel")
        self.alamatLabel.setMaximumSize(QSize(100, 100))
        self.alamatLabel.setTabletTracking(False)
        self.alamatLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.alamatLabel, 9, 0, 1, 1)

        self.teleponLabel = QLabel(self.IsiFrame)
        self.teleponLabel.setObjectName(u"teleponLabel")

        self.gridLayout.addWidget(self.teleponLabel, 6, 0, 1, 1)

        self.jeniskelaminLabel = QLabel(self.IsiFrame)
        self.jeniskelaminLabel.setObjectName(u"jeniskelaminLabel")

        self.gridLayout.addWidget(self.jeniskelaminLabel, 8, 0, 1, 1)

        self.alamatInput = QTextEdit(self.IsiFrame)
        self.alamatInput.setObjectName(u"alamatInput")
        self.alamatInput.setEnabled(False)
        self.alamatInput.setMaximumSize(QSize(16777215, 75))

        self.gridLayout.addWidget(self.alamatInput, 9, 2, 1, 2)

        self.lakiCheckBox = QCheckBox(self.IsiFrame)
        self.lakiCheckBox.setObjectName(u"lakiCheckBox")
        self.lakiCheckBox.setEnabled(False)
        self.lakiCheckBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lakiCheckBox, 8, 2, 1, 1)

        self.namaLabel = QLabel(self.IsiFrame)
        self.namaLabel.setObjectName(u"namaLabel")

        self.gridLayout.addWidget(self.namaLabel, 1, 0, 1, 1)

        self.namaInput = QLineEdit(self.IsiFrame)
        self.namaInput.setObjectName(u"namaInput")
        self.namaInput.setEnabled(False)

        self.gridLayout.addWidget(self.namaInput, 1, 2, 1, 2)

        self.emailInput = QLineEdit(self.IsiFrame)
        self.emailInput.setObjectName(u"emailInput")

        self.gridLayout.addWidget(self.emailInput, 3, 2, 1, 2)


        self.verticalLayout_2.addWidget(self.IsiFrame)

        self.daftarFrame = QFrame(Form)
        self.daftarFrame.setObjectName(u"daftarFrame")
        self.daftarFrame.setStyleSheet(u".QFrame {\n"
"background-color: rgb(0, 33, 48);\n"
"}\n"
"                QPushButton {\n"
"					background-color: rgb(0, 80, 115);\n"
"                    font-size: 20px;\n"
"                    font-weight: bold;\n"
"                    color: #ffffff;\n"
"                    padding-left: 20px;\n"
"                    border: none;\n"
"                    height: 50px;\n"
"                }\n"
"                QPushButton:checked {\n"
"                    background-color: rgb(0, 100, 200);\n"
"                    color: #ffffff;\n"
"                }\n"
"                QPushButton:hover {\n"
"                    background-color: rgb(0, 50, 100);\n"
"                }")
        self.daftarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.daftarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.daftarFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 20)
        self.daftarButton = QPushButton(self.daftarFrame)
        self.daftarButton.setObjectName(u"daftarButton")

        self.verticalLayout.addWidget(self.daftarButton)


        self.verticalLayout_2.addWidget(self.daftarFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.headerTitle.setText(QCoreApplication.translate("Form", u"PROFILE", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.PerempuanCheckBox.setText(QCoreApplication.translate("Form", u"Perempuan", None))
        self.passwordInput.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password          ", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat               ", None))
        self.teleponLabel.setText(QCoreApplication.translate("Form", u"Telepon             ", None))
        self.jeniskelaminLabel.setText(QCoreApplication.translate("Form", u"Jenis Kelamin   ", None))
        self.lakiCheckBox.setText(QCoreApplication.translate("Form", u"Laki-laki", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama Lengkap ", None))
        self.daftarButton.setText(QCoreApplication.translate("Form", u"SIMPAN PERUBAHAN", None))
    # retranslateUi

