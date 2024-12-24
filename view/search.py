# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setObjectName(u"searchBar")

        self.searchLayout.addWidget(self.searchBar)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")

        self.searchLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.searchLayout)

        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.categoryDropdown = QComboBox(self.centralwidget)
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.setObjectName(u"categoryDropdown")

        self.filterLayout.addWidget(self.categoryDropdown)

        self.sortDropdown = QComboBox(self.centralwidget)
        self.sortDropdown.addItem("")
        self.sortDropdown.addItem("")
        self.sortDropdown.addItem("")
        self.sortDropdown.addItem("")
        self.sortDropdown.setObjectName(u"sortDropdown")

        self.filterLayout.addWidget(self.sortDropdown)


        self.verticalLayout.addLayout(self.filterLayout)

        self.resultsTable = QTableWidget(self.centralwidget)
        if (self.resultsTable.columnCount() < 4):
            self.resultsTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.resultsTable.setObjectName(u"resultsTable")

        self.verticalLayout.addWidget(self.resultsTable)

        self.detailsButton = QPushButton(self.centralwidget)
        self.detailsButton.setObjectName(u"detailsButton")

        self.verticalLayout.addWidget(self.detailsButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cari Buku", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Masukkan judul atau nama penulis...", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        self.categoryDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua", None))
        self.categoryDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Fiksi", None))
        self.categoryDropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Non-Fiksi", None))
        self.categoryDropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Sains", None))
        self.categoryDropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Sejarah", None))

        self.sortDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Populer", None))
        self.sortDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Terbaru", None))
        self.sortDropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.sortDropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Z-A", None))

        ___qtablewidgetitem = self.resultsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Judul", None));
        ___qtablewidgetitem1 = self.resultsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Penulis", None));
        ___qtablewidgetitem2 = self.resultsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kategori", None));
        ___qtablewidgetitem3 = self.resultsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tahun Terbit", None));
        self.detailsButton.setText(QCoreApplication.translate("MainWindow", u"Lihat Detail", None))
    # retranslateUi

