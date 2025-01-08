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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.searchBar = QLineEdit(MainWindow)
        self.searchBar.setObjectName(u"searchBar")

        self.verticalLayout.addWidget(self.searchBar)

        self.BukuNonFiksi = QListWidget(MainWindow)
        self.BukuNonFiksi.setObjectName(u"BukuNonFiksi")

        self.verticalLayout.addWidget(self.BukuNonFiksi)

        self.backButton = QPushButton(MainWindow)
        self.backButton.setObjectName(u"backButton")

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fiction Book Category", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"List Buku Non Fiksi", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for a book...", None))
#if QT_CONFIG(tooltip)
        self.BukuNonFiksi.setToolTip(QCoreApplication.translate("MainWindow", u"List of fiction books", None))
#endif // QT_CONFIG(tooltip)
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

