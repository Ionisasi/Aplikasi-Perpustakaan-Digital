from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QLabel, QScrollArea, QSizePolicy,
                               QVBoxLayout, QHBoxLayout, QWidget)
import os

def get_icon_path(icon_name):
    # Mendapatkan path absolut ke folder Icon
    icon_path = os.path.join(os.path.dirname(__file__), '..', 'Asset', 'Icon', icon_name)
    return os.path.abspath(icon_path)

class Ui_Form(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(780, 565)
        self.verticalLayout = QVBoxLayout(HomePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Header Title
        self.headerTitle = QLabel(HomePage)
        self.headerTitle.setObjectName(u"headerTitle")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.headerTitle.setFont(font)
        self.headerTitle.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 24, 35);")
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.headerTitle)

        # Gambar
        self.label = QLabel(HomePage)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(get_icon_path("Glow.png")))
        self.label.setScaledContents(True)  # Agar gambar dapat disesuaikan ukurannya
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        # Label Rekomendasi
        self.label_2 = QLabel(HomePage)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)

        # Scroll Area
        self.scrollArea = QScrollArea(HomePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Layout untuk konten scroll area
        self.scrollAreaLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")

        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(HomePage)
        QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"HomePage", None))
        self.headerTitle.setText(QCoreApplication.translate("HomePage", u"BERANDA", None))
        self.label_2.setText(QCoreApplication.translate("HomePage", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">REKOMENDASI BUKU</span></p></body></html>", None))
