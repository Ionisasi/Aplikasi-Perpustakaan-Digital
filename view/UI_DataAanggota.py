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
        self.widget_2 = QWidget(self.MainContent)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(800, 100))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 16777215))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setPlaceholderText("Nama")
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                color: Blue;  /* Warna teks */
                font-weight: bold;
            }
            QLineEdit::placeholder {
                color: white;  /* Warna placeholder */
            }
        """)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget = QWidget(self.MainContent)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(800, 480))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        # QTable
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Kelola"])
        
        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_3.addWidget(self.widget)

        self.scrollArea.setWidget(self.MainContent)

        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.headerTitle.setText(QCoreApplication.translate("Form", u"DATA ANGGOTA", None))
        self.label.setText(QCoreApplication.translate("Form", u"Search :", None))
    # retranslateUi
