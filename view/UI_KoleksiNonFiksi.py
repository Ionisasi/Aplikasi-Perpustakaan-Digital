# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KoleksiNonFiksi.ui'
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
    def setupUi(self, BukuNonFiksi):
        if not BukuNonFiksi.objectName():
            BukuNonFiksi.setObjectName(u"BukuNonFiksi")
        BukuNonFiksi.resize(500, 400)
        self.verticalLayout = QVBoxLayout(BukuNonFiksi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(BukuNonFiksi)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.searchBtn = QLineEdit(BukuNonFiksi)
        self.searchBtn.setObjectName(u"searchBtn")

        self.verticalLayout.addWidget(self.searchBtn)

        self.BukuNonFiksi = QListWidget(BukuNonFiksi)
        self.BukuNonFiksi.setObjectName(u"BukuNonFiksi")

        self.verticalLayout.addWidget(self.BukuNonFiksi)

        self.PushButton = QPushButton(BukuNonFiksi)
        self.PushButton.setObjectName(u"PushButton")

        self.verticalLayout.addWidget(self.PushButton)


        self.retranslateUi(BukuNonFiksi)

        QMetaObject.connectSlotsByName(BukuNonFiksi)
    # setupUi

    def retranslateUi(self, BukuNonFiksi):
        BukuNonFiksi.setWindowTitle(QCoreApplication.translate("BukuNonFiksi", u"Koleksi Buku Non Fiksi", None))
        self.label.setText(QCoreApplication.translate("BukuNonFiksi", u"List Buku Non Fiksi", None))
        self.searchBtn.setPlaceholderText(QCoreApplication.translate("BukuNonFiksi", u"Search for a book...", None))
#if QT_CONFIG(tooltip)
        self.BukuNonFiksi.setToolTip(QCoreApplication.translate("BukuNonFiksi", u"List of fiction books", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton.setText(QCoreApplication.translate("BukuNonFiksi", u"Back", None))
    # retranslateUi

