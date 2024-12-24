# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(800, 600)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHeader = QLabel(self.centralwidget)
        self.labelHeader.setObjectName(u"labelHeader")
        self.labelHeader.setStyleSheet(u"font-size: 24px; font-weight: bold; text-align: center; color: #0275d8;")
        self.labelHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelHeader)

        self.summaryGroup = QGroupBox(self.centralwidget)
        self.summaryGroup.setObjectName(u"summaryGroup")
        self.horizontalLayout_1 = QHBoxLayout(self.summaryGroup)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.totalBooksLabel = QLabel(self.summaryGroup)
        self.totalBooksLabel.setObjectName(u"totalBooksLabel")
        self.totalBooksLabel.setStyleSheet(u"font-size: 16px; color: #02C2D8;")

        self.horizontalLayout_1.addWidget(self.totalBooksLabel)

        self.borrowedBooksLabel = QLabel(self.summaryGroup)
        self.borrowedBooksLabel.setObjectName(u"borrowedBooksLabel")
        self.borrowedBooksLabel.setStyleSheet(u"font-size: 16px; color: #02C2D8\n"
"")

        self.horizontalLayout_1.addWidget(self.borrowedBooksLabel)


        self.verticalLayout.addWidget(self.summaryGroup)

        self.navigationGroup = QGroupBox(self.centralwidget)
        self.navigationGroup.setObjectName(u"navigationGroup")
        self.horizontalLayout_2 = QHBoxLayout(self.navigationGroup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bookListButton = QPushButton(self.navigationGroup)
        self.bookListButton.setObjectName(u"bookListButton")

        self.horizontalLayout_2.addWidget(self.bookListButton)

        self.searchBooksButton = QPushButton(self.navigationGroup)
        self.searchBooksButton.setObjectName(u"searchBooksButton")

        self.horizontalLayout_2.addWidget(self.searchBooksButton)

        self.borrowedBooksButton = QPushButton(self.navigationGroup)
        self.borrowedBooksButton.setObjectName(u"borrowedBooksButton")

        self.horizontalLayout_2.addWidget(self.borrowedBooksButton)

        self.addBookButton = QPushButton(self.navigationGroup)
        self.addBookButton.setObjectName(u"addBookButton")

        self.horizontalLayout_2.addWidget(self.addBookButton)


        self.verticalLayout.addWidget(self.navigationGroup)

        self.activitiesGroup = QGroupBox(self.centralwidget)
        self.activitiesGroup.setObjectName(u"activitiesGroup")
        self.verticalLayout_2 = QVBoxLayout(self.activitiesGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.activitiesTable = QTableWidget(self.activitiesGroup)
        if (self.activitiesTable.columnCount() < 2):
            self.activitiesTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.activitiesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.activitiesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.activitiesTable.setObjectName(u"activitiesTable")

        self.verticalLayout_2.addWidget(self.activitiesTable)


        self.verticalLayout.addWidget(self.activitiesGroup)

        Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Digital Library Dashboard", None))
        self.labelHeader.setText(QCoreApplication.translate("Dashboard", u"Dashboard - Aplikasi Perpustakaan Digital", None))
        self.summaryGroup.setTitle(QCoreApplication.translate("Dashboard", u"Ringkasan", None))
        self.totalBooksLabel.setText(QCoreApplication.translate("Dashboard", u"Total Buku: 0", None))
        self.borrowedBooksLabel.setText(QCoreApplication.translate("Dashboard", u"Buku Yang Dipinjam: 0", None))
        self.navigationGroup.setTitle(QCoreApplication.translate("Dashboard", u"Quick Navigation", None))
        self.bookListButton.setText(QCoreApplication.translate("Dashboard", u"Daftar Buku", None))
        self.searchBooksButton.setText(QCoreApplication.translate("Dashboard", u"Cari Buku", None))
        self.borrowedBooksButton.setText(QCoreApplication.translate("Dashboard", u"Peminjaman Buku", None))
        self.addBookButton.setText(QCoreApplication.translate("Dashboard", u"Tambah Buku Baru", None))
        self.activitiesGroup.setTitle(QCoreApplication.translate("Dashboard", u"Aktivitas Terbaru", None))
        ___qtablewidgetitem = self.activitiesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Aktivitas", None));
        ___qtablewidgetitem1 = self.activitiesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Timestamp", None));
    # retranslateUi

