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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #0275d8;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.usernameInput = QLineEdit(self.centralwidget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setStyleSheet(u"padding: 8px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;")

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setStyleSheet(u"padding: 8px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;")
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
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login, Logout & Register", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Perpustakaan Digital", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

