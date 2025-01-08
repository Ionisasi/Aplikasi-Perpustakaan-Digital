# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataBuku_1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblHeaderTitle = QLabel(MainWindow)
        self.lblHeaderTitle.setObjectName(u"lblHeaderTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblHeaderTitle.setFont(font)
        self.lblHeaderTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
        self.lblHeaderTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.lblHeaderTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblHeaderTitle)

        self.mainScrollArea = QScrollArea(MainWindow)
        self.mainScrollArea.setObjectName(u"mainScrollArea")
        self.mainScrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mainScrollArea.setStyleSheet(u"")
        self.mainScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.mainScrollArea.setWidgetResizable(True)
        self.contentWidget = QWidget()
        self.contentWidget.setObjectName(u"contentWidget")
        self.contentWidget.setGeometry(QRect(0, 0, 780, 521))
        self.contentWidget.setStyleSheet(u".QWidget{\n"
                                         "background-color: rgb(0, 33, 48);\n"
                                         "}")
        self.verticalLayout_3 = QVBoxLayout(self.contentWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headerWidget = QWidget(self.contentWidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setMaximumSize(QSize(800, 100))
        self.horizontalLayout = QHBoxLayout(self.headerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAddData = QPushButton(self.headerWidget)
        self.btnAddData.setObjectName(u"btnAddData")
        self.btnAddData.setMaximumSize(QSize(150, 500))
        font1 = QFont()
        font1.setBold(True)
        self.btnAddData.setFont(font1)
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.btnAddData.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnAddData)

        self.lblSearch = QLabel(self.headerWidget)
        self.lblSearch.setObjectName(u"lblSearch")
        self.lblSearch.setFont(font1)
        self.lblSearch.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblSearch)

        self.txtSearch = QLineEdit(self.headerWidget)
        self.txtSearch.setObjectName(u"txtSearch")
        self.txtSearch.setMaximumSize(QSize(200, 16777215))
        self.txtSearch.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.txtSearch)

        self.verticalLayout_3.addWidget(self.headerWidget)

        self.tableWidgetContainer = QWidget(self.contentWidget)
        self.tableWidgetContainer.setObjectName(u"tableWidgetContainer")
        self.tableWidgetContainer.setMaximumSize(QSize(800, 480))
        self.horizontalLayout_2 = QHBoxLayout(self.tableWidgetContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.tblData = QTableWidget(self.tableWidgetContainer)
        self.tblData.setObjectName(u"tblData")
        self.tblData.setRowCount(3)
        self.tblData.setColumnCount(1)
        self.tblData.setHorizontalHeaderLabels(["Kelola"])

        # Tambahkan tombol "Edit" dan "Hapus" di kolom "Kelola"
        for row in range(self.tblData.rowCount()):
            # Buat widget untuk menampung tombol
            btn_widget = QWidget()
            btn_layout = QHBoxLayout(btn_widget)
            btn_layout.setContentsMargins(0, 0, 0, 0)

            # Tambahkan tombol Edit dan Hapus
            btnEdit = QPushButton("Edit")
            btnDelete = QPushButton("Hapus")

            # Hubungkan tombol dengan fungsi
            btnEdit.clicked.connect(lambda checked, r=row: print(f"Edit row {r}"))
            btnDelete.clicked.connect(lambda checked, r=row: print(f"Delete row {r}"))

            # Tambahkan tombol ke layout
            btn_layout.addWidget(btnEdit)
            btn_layout.addWidget(btnDelete)

            # Set widget tombol ke kolom "Kelola"
            self.tblData.setCellWidget(row, 0, btn_widget)

        self.horizontalLayout_2.addWidget(self.tblData)

        self.verticalLayout_3.addWidget(self.tableWidgetContainer)

        self.mainScrollArea.setWidget(self.contentWidget)

        self.verticalLayout.addWidget(self.mainScrollArea)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Buku", None))
        self.lblHeaderTitle.setText(QCoreApplication.translate("MainWindow", u"DATA ANGGOTA", None))
        self.btnAddData.setText(QCoreApplication.translate("MainWindow", u"Tambah Data", None))
        self.lblSearch.setText(QCoreApplication.translate("MainWindow", u"Search :", None))

    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())