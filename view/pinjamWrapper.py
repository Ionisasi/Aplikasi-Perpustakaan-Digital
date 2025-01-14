# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinjamWrapper.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 300)
        Form.setStyleSheet(u"QPushButton {\n"
"				background-color: rgb(0, 255, 0);\n"
"                font-size: 20px;\n"
"                font-weight: bold;\n"
"                color: #ffffff;\n"
"                text-align: left;\n"
"                padding-left: 20px;\n"
"                border: none;\n"
"        }\n"
"        QPushButton:checked {\n"
"                background-color: rgb(0, 100, 200);\n"
"                color: #ffffff;\n"
"        }\n"
"        QPushButton:hover {\n"
"                background-color: rgb(0, 50, 100);\n"
"        }")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.coverImg = QLabel(Form)
        self.coverImg.setObjectName(u"coverImg")
        self.coverImg.setPixmap(QPixmap(u"../Asset/cover-img/_Pi0YRcQESAC.png"))
        self.coverImg.setScaledContents(False)
        self.coverImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.coverImg)

        self.judulBuku = QLabel(Form)
        self.judulBuku.setObjectName(u"judulBuku")
        self.judulBuku.setMaximumSize(QSize(150, 16777215))
        self.judulBuku.setStyleSheet(u"font-size: 12px; font-weight: bold; text-align: center; color: #ffffff;")
        self.judulBuku.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.judulBuku.setWordWrap(True)

        self.verticalLayout.addWidget(self.judulBuku)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 3, 1)

        self.LblBorrowDate = QLabel(Form)
        self.LblBorrowDate.setObjectName(u"LblBorrowDate")
        self.LblBorrowDate.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: center; color: #ffffff;")

        self.gridLayout.addWidget(self.LblBorrowDate, 0, 1, 1, 1)

        self.tanggalPeminjaman = QDateEdit(Form)
        self.tanggalPeminjaman.setObjectName(u"tanggalPeminjaman")

        self.gridLayout.addWidget(self.tanggalPeminjaman, 0, 2, 1, 1)

        self.LblDeadLine = QLabel(Form)
        self.LblDeadLine.setObjectName(u"LblDeadLine")
        self.LblDeadLine.setStyleSheet(u"font-size: 15px; font-weight: bold; text-align: center; color: #ffffff;")

        self.gridLayout.addWidget(self.LblDeadLine, 1, 1, 1, 1)

        self.tanggalDeadline = QDateEdit(Form)
        self.tanggalDeadline.setObjectName(u"tanggalDeadline")

        self.gridLayout.addWidget(self.tanggalDeadline, 1, 2, 1, 1)

        self.KembalikanBtn = QPushButton(Form)
        self.KembalikanBtn.setObjectName(u"KembalikanBtn")
        self.KembalikanBtn.setStyleSheet(u"font-size: 20px; font-weight: bold; text-align: left; color: #ffffff;text-align: center;\n"
"border:transparent;")

        self.gridLayout.addWidget(self.KembalikanBtn, 2, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.coverImg.setText("")
        self.judulBuku.setText(QCoreApplication.translate("Form", u"Judul Buku", None))
        self.LblBorrowDate.setText(QCoreApplication.translate("Form", u"Tanggal Peminjaman", None))
        self.LblDeadLine.setText(QCoreApplication.translate("Form", u"Tenggat Pengembalian", None))
        self.KembalikanBtn.setText(QCoreApplication.translate("Form", u"Kembalikan", None))
    # retranslateUi

