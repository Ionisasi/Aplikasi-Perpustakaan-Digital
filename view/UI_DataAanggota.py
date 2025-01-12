# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataBuku.ui'
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
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerTitle = QLabel(Form)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
        self.headerTitle.setTextFormat(Qt.TextFormat.AutoText)
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.headerTitle)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.MainContent = QWidget()
        self.MainContent.setObjectName(u"MainContent")
        self.MainContent.setGeometry(QRect(0, 0, 780, 521))
        self.MainContent.setStyleSheet(u".QWidget{\n"
"background-color: rgb(0, 33, 48);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.MainContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Action_widget = QWidget(self.MainContent)
        self.Action_widget.setObjectName(u"Action_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Action_widget.sizePolicy().hasHeightForWidth())
        self.Action_widget.setSizePolicy(sizePolicy1)
        self.Action_widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.Action_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Tambah_data = QPushButton(self.Action_widget)
        self.Tambah_data.setObjectName(u"Tambah_data")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Tambah_data.sizePolicy().hasHeightForWidth())
        self.Tambah_data.setSizePolicy(sizePolicy2)
        self.Tambah_data.setMaximumSize(QSize(150, 150))
        font1 = QFont()
        font1.setBold(True)
        self.Tambah_data.setFont(font1)
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.Tambah_data.setIcon(icon)

        self.horizontalLayout.addWidget(self.Tambah_data)

        self.Search_label = QLabel(self.Action_widget)
        self.Search_label.setObjectName(u"Search_label")
        self.Search_label.setFont(font1)
        self.Search_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Search_label)

        self.Search_action = QLineEdit(self.Action_widget)
        self.Search_action.setObjectName(u"Search_action")
        self.Search_action.setMaximumSize(QSize(200, 16777215))
        self.Search_action.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Search_action)


        self.verticalLayout_3.addWidget(self.Action_widget)

        #Table Area
        self.Table_area = QWidget(self.MainContent)
        self.Table_area.setObjectName(u"Table_area")
        sizePolicy1.setHeightForWidth(self.Table_area.sizePolicy().hasHeightForWidth())
        self.Table_area.setSizePolicy(sizePolicy1)
        self.Table_area.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.Table_area)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.view_data = QTableWidget(self.Table_area)
        self.view_data.setStyleSheet("background-color: rgb(0, 24, 35);")
        self.view_data.setObjectName(u"view_data")
        self.view_data.setRowCount(0)
        self.view_data.setColumnCount(1)
        self.view_data.setHorizontalHeaderLabels(["Kelola"])
        

        self.horizontalLayout_2.addWidget(self.view_data)


        self.verticalLayout_3.addWidget(self.Table_area)

        self.scrollArea.setWidget(self.MainContent)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.headerTitle.setText(QCoreApplication.translate("Form", u"DATA ANGGOTA", None))
        self.Tambah_data.setText(QCoreApplication.translate("Form", u"Tambah Data", None))
        self.Search_label.setText(QCoreApplication.translate("Form", u"Search :", None))
    # retranslateUi

