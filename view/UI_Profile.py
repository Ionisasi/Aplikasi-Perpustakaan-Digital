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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 565)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerTitle = QLabel(Form)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
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
"font-weight: bold; color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{background-color : rgb(46, 47, 48);}")
        self.gridLayout = QGridLayout(self.IsiFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(20, 20, 20, 30)
        self.namaLabel = QLabel(self.IsiFrame)
        self.namaLabel.setObjectName(u"namaLabel")

        self.gridLayout.addWidget(self.namaLabel, 0, 0, 1, 1)

        self.emailLabel = QLabel(self.IsiFrame)
        self.emailLabel.setObjectName(u"emailLabel")

        self.gridLayout.addWidget(self.emailLabel, 1, 0, 1, 1)

        self.passwordLabel = QLabel(self.IsiFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)

        self.teleponLabel = QLabel(self.IsiFrame)
        self.teleponLabel.setObjectName(u"teleponLabel")

        self.gridLayout.addWidget(self.teleponLabel, 3, 0, 1, 1)

        self.jeniskelaminLabel = QLabel(self.IsiFrame)
        self.jeniskelaminLabel.setObjectName(u"jeniskelaminLabel")

        self.gridLayout.addWidget(self.jeniskelaminLabel, 4, 0, 1, 1)

        self.lakiCBox = QCheckBox(self.IsiFrame)
        self.genderGrupBtn = QButtonGroup(Form)
        self.genderGrupBtn.setObjectName(u"genderGrupBtn")
        self.genderGrupBtn.addButton(self.lakiCBox)
        self.lakiCBox.setObjectName(u"lakiCBox")

        self.gridLayout.addWidget(self.lakiCBox, 4, 1, 1, 1)

        self.perempuanCBox = QCheckBox(self.IsiFrame)
        self.genderGrupBtn.addButton(self.perempuanCBox)
        self.perempuanCBox.setObjectName(u"perempuanCBox")

        self.gridLayout.addWidget(self.perempuanCBox, 4, 2, 1, 1)

        self.alamatLabel = QLabel(self.IsiFrame)
        self.alamatLabel.setObjectName(u"alamatLabel")
        self.alamatLabel.setMaximumSize(QSize(100, 100))
        self.alamatLabel.setTabletTracking(False)
        self.alamatLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.alamatLabel, 5, 0, 1, 1)

        self.alamatInput = QTextEdit(self.IsiFrame)
        self.alamatInput.setObjectName(u"alamatInput")
        self.alamatInput.setMinimumSize(QSize(0, 40))
        self.alamatInput.setMaximumSize(QSize(16777215, 80))

        self.gridLayout.addWidget(self.alamatInput, 5, 1, 1, 2)

        self.namaInput = QLineEdit(self.IsiFrame)
        self.namaInput.setObjectName(u"namaInput")
        self.namaInput.setFrame(True)

        self.gridLayout.addWidget(self.namaInput, 0, 1, 1, 2)

        self.userInput = QLineEdit(self.IsiFrame)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setFrame(True)

        self.gridLayout.addWidget(self.userInput, 1, 1, 1, 2)

        self.passwordInput = QLineEdit(self.IsiFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setReadOnly(True)
        self.passwordInput.setFrame(True)

        self.gridLayout.addWidget(self.passwordInput, 2, 1, 1, 2)

        self.teleponInput = QLineEdit(self.IsiFrame)
        self.teleponInput.setObjectName(u"teleponInput")
        self.teleponInput.setFrame(True)

        self.gridLayout.addWidget(self.teleponInput, 3, 1, 1, 2)


        self.verticalLayout_2.addWidget(self.IsiFrame)

        self.saveFrame = QFrame(Form)
        self.saveFrame.setObjectName(u"saveFrame")
        self.saveFrame.setStyleSheet(u".QFrame {\n"
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
"                QPushButton:hover {\n"
"                    background-color: rgb(0, 50, 100);\n"
"                }")
        self.saveFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.saveFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.saveFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 20)
        self.saveButton = QPushButton(self.saveFrame)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)


        self.verticalLayout_2.addWidget(self.saveFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.headerTitle.setText(QCoreApplication.translate("Form", u"PROFILE", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama Lengkap ", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password          ", None))
        self.teleponLabel.setText(QCoreApplication.translate("Form", u"Telepon             ", None))
        self.jeniskelaminLabel.setText(QCoreApplication.translate("Form", u"Jenis Kelamin   ", None))
        self.lakiCBox.setText(QCoreApplication.translate("Form", u"Laki-laki", None))
        self.perempuanCBox.setText(QCoreApplication.translate("Form", u"Perempuan", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat               ", None))
        self.passwordInput.setText("")
        self.saveButton.setText(QCoreApplication.translate("Form", u"SIMPAN PERUBAHAN", None))
    # retranslateUi

