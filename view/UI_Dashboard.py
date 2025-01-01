import os
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QSpacerItem,
    QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QSpacerItem, QButtonGroup
)

class Ui_Dashboard:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Perpustakaan Digital")
        MainWindow.setGeometry(100, 100, 1080, 700)
        MainWindow.setWindowIcon(QIcon("Asset/Icon/Buku.png"))

        # Main widget and layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)  # Vertical layout to accommodate the header
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Header
        self.header = QWidget()
        self.header.setFixedHeight(91)
        self.header.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 10, 10, 10)


        self.icon_label = QLabel()
        self.icon_label.setObjectName("iconLabel")
        self.icon_label.setFixedSize(70, 70)
        self.icon_label.setPixmap(QPixmap("Asset/Icon/Buku.png"))
        self.icon_label.setScaledContents(True)
        
        self.title_label = QLabel("Perpustakaan Digital\n      Kelompok 2")
        self.title_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #ffffff;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.header_layout.addWidget(self.icon_label)
        self.header_layout.addWidget(self.title_label)

        self.main_layout.addWidget(self.header)  # Add header to the main layout

        # Content Layout (Sidebar and Main Content)
        self.content_layout = QHBoxLayout()

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(291)
        self.sidebar.setStyleSheet("background-color: rgb(0, 33, 48);")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 20, 10, 20)

        # Profile Section
        self.profile_widget = QWidget()
        self.profile_layout = QHBoxLayout(self.profile_widget)


        self.profile_icon = QLabel()
        self.profile_icon.setObjectName("profileIcon")
        self.profile_icon.setFixedSize(70, 70)
        self.profile_icon.setPixmap(QPixmap("Asset/Icon/Admin1.png"))
        self.profile_icon.setStyleSheet("background-color: white;")
        self.profile_icon.setScaledContents(True)

        self.profile_info_layout = QVBoxLayout()

        self.name_label = QLabel("Ryan")
        self.name_label.setObjectName("nameLabel")
        self.name_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffffff;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.position_label = QLabel("Administrator")
        self.position_label.setObjectName("positionLabel")
        self.position_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000; background-color: rgb(255, 255, 0);")
        self.position_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.profile_info_layout.addWidget(self.name_label)
        self.profile_info_layout.addWidget(self.position_label)

        self.profile_layout.addWidget(self.profile_icon)
        self.profile_layout.addLayout(self.profile_info_layout)

        self.sidebar_layout.addWidget(self.profile_widget)

        # Menu Items
        self.menu1_label = QLabel("Main Navigation")
        self.menu1_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #555555; background-color: rgb(0, 24, 35); padding: 5px;")
        self.menu1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebar_layout.addWidget(self.menu1_label)

        self.sidebar_buttons = []
        self.kelola_submenu = QWidget()
        self.kelola_submenu_layout = QVBoxLayout(self.kelola_submenu)
        self.kelola_submenu.setVisible(False)

        self.koleksi_submenu = QWidget()
        self.koleksi_submenu_layout = QVBoxLayout(self.koleksi_submenu)
        self.koleksi_submenu.setVisible(False)

        def create_sidebar_button(text, theme_icon=None, fallback_icon=None):
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    font-weight: bold;
                    color: #ffffff;
                    text-align: left;
                    padding-left: 20px;
                    border: none;
                    height: 50px;
                }
                QPushButton:hover {
                    background-color: rgb(0, 50, 100);
                }
            """)
            if theme_icon:
                icon = QIcon.fromTheme(theme_icon)
                if not icon.isNull():
                    button.setIcon(icon)
                elif fallback_icon:
                    button.setIcon(QIcon(fallback_icon))
            elif fallback_icon:
                button.setIcon(QIcon(fallback_icon))

            self.sidebar_buttons.append(button)
            return button


        self.dashboard_button = create_sidebar_button("Dashboard", None, "Asset/Icon/home.png")
        self.dashboard_button.setObjectName("dashboardButton")
        self.koleksi_button = create_sidebar_button("Koleksi", None, "Asset/Icon/koleksi.png")
        self.koleksi_button.setObjectName("koleksiButton")
        self.kelola_button = create_sidebar_button("Kelola Data", None, "Asset/Icon/open-folder.png")
        self.kelola_button.setObjectName("kelolaButton")

        self.log_data_button = create_sidebar_button("Log Data", None, "Asset/Icon/log-data.png")
        self.log_data_button.setObjectName("logDataButton")

        self.sidebar_layout.addWidget(self.dashboard_button)
        self.sidebar_layout.addWidget(self.koleksi_button)
        self.sidebar_layout.addWidget(self.koleksi_submenu)
        self.sidebar_layout.addWidget(self.kelola_button)
        self.sidebar_layout.addWidget(self.kelola_submenu)
        self.sidebar_layout.addWidget(self.log_data_button)
        
        # Submenu Buttons (using the same style as sidebar buttons)
        data_buku_button = QPushButton("Data Buku")
        data_buku_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:checked {
                background-color: rgb(0, 100, 200);
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        data_buku_button.setIcon(QIcon("Icon/book.png"))
        self.kelola_submenu_layout.addWidget(data_buku_button)

        data_anggota_button = QPushButton("Data Anggota")
        data_anggota_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:checked {
                background-color: rgb(0, 100, 200);
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        data_anggota_button.setIcon(QIcon("Icon/user.png"))
        self.kelola_submenu_layout.addWidget(data_anggota_button)
        
        # Submenu Buttons - Koleksi
        fiksi_button = QPushButton("Fiksi")
        fiksi_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        fiksi_button.setIcon(QIcon("Icon/book-open.png"))
        self.koleksi_submenu_layout.addWidget(fiksi_button)

        nonfiksi_button = QPushButton("Nonfiksi")
        nonfiksi_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        nonfiksi_button.setIcon(QIcon("Icon/book-open.png"))
        self.koleksi_submenu_layout.addWidget(nonfiksi_button)

        # Submenu Buttons
        self.data_buku_button = QPushButton("Data Buku")
        self.data_buku_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        self.data_buku_button.setIcon(QIcon("Asset/Icon/book.png"))
        self.kelola_submenu_layout.addWidget(self.data_buku_button)

        data_anggota_button = QPushButton("Data Anggota")
        data_anggota_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                padding-left: 40px;
                color: #ffffff;
                border: none;
                height: 40px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        data_anggota_button.setIcon(QIcon("Asset/Icon/user.png"))
        self.kelola_submenu_layout.addWidget(data_anggota_button)

        self.menu2_label = QLabel("Settings")
        self.menu2_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #555555; background-color: rgb(0, 24, 35); padding: 5px;")
        self.menu2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebar_layout.addWidget(self.menu2_label)

        self.logout_button = create_sidebar_button("Logout", None, "Asset/Icon/logout.png")

        self.sidebar_layout.addWidget(self.logout_button)

        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        self.button_group.addButton(self.dashboard_button)
        self.button_group.addButton(self.koleksi_button)
        self.button_group.addButton(self.kelola_button)
        self.button_group.addButton(self.log_data_button)

        self.sidebar_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Main Content
        self.content_widget = QWidget()
        self.content_widget_layout = QVBoxLayout(self.content_widget)
        self.content_widget_layout.setContentsMargins(10, 10, 10, 10)

        self.search_bar = QLineEdit()
        self.search_bar.setObjectName("searchBar")
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet("border-radius: 20px; padding: 10px;")
        self.search_bar.setFixedHeight(40)

        self.content_widget_layout.addWidget(self.search_bar)

        self.main_content = QLabel("Main Content Area")
        self.main_content.setObjectName("mainContentLabel")
        self.main_content.setStyleSheet("font-size: 24px; text-align: center;")
        self.main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_widget_layout.addWidget(self.main_content)

        self.content_layout.addWidget(self.sidebar)
        self.content_layout.addWidget(self.content_widget)

        self.main_layout.addLayout(self.content_layout)

        MainWindow.setCentralWidget(self.main_widget)