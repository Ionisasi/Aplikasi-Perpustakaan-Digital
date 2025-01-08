# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KoleksiFiksi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_BukuFiksi(object):
    def setupUi(self, BukuFiksi):
        if not BukuFiksi.objectName():
            BukuFiksi.setObjectName(u"BukuFiksi")
        BukuFiksi.resize(500, 400)
        self.verticalLayout = QVBoxLayout(BukuFiksi)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerTitle = QLabel(BukuFiksi)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
        self.headerTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.headerTitle)

        self.search = QLineEdit(BukuFiksi)
        self.search.setObjectName(u"search")

        self.verticalLayout.addWidget(self.search)

        self.scrollArea = QScrollArea(BukuFiksi)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u".QWidget{\n"
"background-color: rgb(0, 33, 48);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 341))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(BukuFiksi)

        QMetaObject.connectSlotsByName(BukuFiksi)
    # setupUi

    def retranslateUi(self, BukuFiksi):
        BukuFiksi.setWindowTitle(QCoreApplication.translate("BukuFiksi", u"Fiction Book Category", None))
        self.headerTitle.setText(QCoreApplication.translate("BukuFiksi", u"FIKSI", None))
        self.search.setPlaceholderText(QCoreApplication.translate("BukuFiksi", u"Search....", None))
    # retranslateUi

