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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Koleksi(object):
    def setupUi(self, BukuFiksi):
        if not BukuFiksi.objectName():
            BukuFiksi.setObjectName(u"BukuFiksi")
        BukuFiksi.resize(500, 400)
        self.verticalLayout = QVBoxLayout(BukuFiksi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(BukuFiksi)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.searchBtn = QLineEdit(BukuFiksi)
        self.searchBtn.setObjectName(u"searchBtn")

        self.verticalLayout.addWidget(self.searchBtn)

        self.BukuFiksi = QListWidget(BukuFiksi)
        self.BukuFiksi.setObjectName(u"BukuFiksi")

        self.verticalLayout.addWidget(self.BukuFiksi)

        self.PushButton = QPushButton(BukuFiksi)
        self.PushButton.setObjectName(u"PushButton")

        self.verticalLayout.addWidget(self.PushButton)


        self.retranslateUi(BukuFiksi)

        QMetaObject.connectSlotsByName(BukuFiksi)
    # setupUi

    def retranslateUi(self, BukuFiksi):
        BukuFiksi.setWindowTitle(QCoreApplication.translate("BukuFiksi", u"Koleksi Buku Fiksi", None))
        self.label.setText(QCoreApplication.translate("BukuFiksi", u"List Buku Fiksi", None))
        self.searchBtn.setPlaceholderText(QCoreApplication.translate("BukuFiksi", u"Search for a book...", None))
#if QT_CONFIG(tooltip)
        self.BukuFiksi.setToolTip(QCoreApplication.translate("BukuFiksi", u"List of fiction books", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton.setText(QCoreApplication.translate("BukuFiksi", u"Back", None))
    # retranslateUi

