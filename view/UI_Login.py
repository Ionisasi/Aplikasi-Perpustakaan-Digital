# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Perpustakaan.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import os
from utils import resource_path

def get_icon_path(icon_name):
        return resource_path(f"Asset/Icon/{icon_name}")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u".QWidget{\n"
"background-color: rgb(0, 33, 48);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(get_icon_path("Buku.png")))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMaximumSize(QSize(300, 300))
        self.titleLabel.setStyleSheet(u"font-size: 27px; font-weight: bold; color: #0275d8;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.titleLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.usernameInput = QLineEdit(self.centralwidget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setStyleSheet(u"padding: 10px; font-size: 14px; border: 2px solid #ccc; border-radius: 5px;")

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setStyleSheet(u"padding: 10px; font-size: 14px; border: 2px solid #ccc; border-radius: 5px;")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setStyleSheet(u"background-color: #5cb85c; color: white; padding: 10px; border: none; border-radius: 4px; font-size: 16px; font-weight: bold;")

        self.verticalLayout.addWidget(self.loginButton)

        self.registerButton = QPushButton(self.centralwidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setStyleSheet(u"background-color: #0275d8; color: white; padding: 10px; border: none; border-radius: 4px; font-size: 16px; font-weight: bold;")

        self.verticalLayout.addWidget(self.registerButton)

        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setVisible(False)
        self.logoutButton.setStyleSheet(u"background-color: #d9534f; color: white; padding: 10px; border: none; border-radius: 4px; font-size: 16px; font-weight: bold;")

        self.verticalLayout.addWidget(self.logoutButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        w_icon = get_icon_path('Buku.png')
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Perpustakaan Digital", None))
        MainWindow.setWindowIcon(w_icon)
        self.label.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Perpustakaan Digital", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

