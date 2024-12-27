import os
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QSpacerItem
)

class Ui_Dashboard:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Perpustakaan Digital")
        MainWindow.setGeometry(100, 100, 1080, 700)
        MainWindow.setWindowIcon(QIcon("Asset/Icon/Buku.png"))

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)  # Vertical layout to accommodate the header
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Header
        header = QWidget()
        header.setFixedHeight(91)
        header.setStyleSheet("background-color: rgb(0, 255, 0);")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(10, 10, 10, 10)

        icon_label = QLabel()
        icon_label.setFixedSize(70, 70)
        icon_label.setPixmap(QPixmap("Asset/Icon/Buku.png"))
        icon_label.setScaledContents(True)

        title_label = QLabel("Perpustakaan Digital\n      Kelompok 2")
        title_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #ffffff;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)

        main_layout.addWidget(header)  # Add header to the main layout

        # Content Layout (Sidebar and Main Content)
        content_layout = QHBoxLayout()

        # Sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(291)
        sidebar.setStyleSheet("background-color: rgb(0, 33, 48);")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)

        # Profile Section
        profile_widget = QWidget()
        profile_layout = QHBoxLayout(profile_widget)

        profile_icon = QLabel()
        profile_icon.setFixedSize(70, 70)
        profile_icon.setPixmap(QPixmap("Asset/Icon/Admin1.png"))
        profile_icon.setStyleSheet("background-color: white;")
        profile_icon.setScaledContents(True)

        profile_info_layout = QVBoxLayout()

        name_label = QLabel("Ryan")
        name_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffffff;")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        position_label = QLabel("Administrator")
        position_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000; background-color: rgb(255, 255, 0);")
        position_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        profile_info_layout.addWidget(name_label)
        profile_info_layout.addWidget(position_label)

        profile_layout.addWidget(profile_icon)
        profile_layout.addLayout(profile_info_layout)

        sidebar_layout.addWidget(profile_widget)

        # Menu Items
        menu1_label = QLabel("Main Navigation")
        menu1_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #555555; background-color: rgb(0, 24, 35); padding: 5px;")
        menu1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sidebar_layout.addWidget(menu1_label)

        self.sidebar_buttons = []
        self.kelola_submenu = QWidget()
        self.kelola_submenu_layout = QVBoxLayout(self.kelola_submenu)
        self.kelola_submenu.setVisible(False)

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

        dashboard_button = create_sidebar_button("Dashboard", None, "Asset/Icon/home.png")
        koleksi_button = create_sidebar_button("Koleksi", None, "Asset/Icon/koleksi.png")
        kelola_button = create_sidebar_button("Kelola Data", None, "Asset/Icon/open-folder.png")

        log_data_button = create_sidebar_button("Log Data", None, "Asset/Icon/log-data.png")

        sidebar_layout.addWidget(dashboard_button)
        sidebar_layout.addWidget(koleksi_button)
        sidebar_layout.addWidget(kelola_button)
        sidebar_layout.addWidget(self.kelola_submenu)
        sidebar_layout.addWidget(log_data_button)

        # Submenu Buttons
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
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        data_buku_button.setIcon(QIcon("Asset/Icon/book.png"))
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
            QPushButton:hover {
                background-color: rgb(0, 50, 100);
            }
        """)
        data_anggota_button.setIcon(QIcon("Asset/Icon/user.png"))
        self.kelola_submenu_layout.addWidget(data_anggota_button)

        menu2_label = QLabel("Settings")
        menu2_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #555555; background-color: rgb(0, 24, 35); padding: 5px;")
        menu2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sidebar_layout.addWidget(menu2_label)

        logout_button = create_sidebar_button("Logout", None, "Asset/Icon/logout.png")

        sidebar_layout.addWidget(logout_button)

        sidebar_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Main Content
        content_widget = QWidget()
        content_widget_layout = QVBoxLayout(content_widget)
        content_widget_layout.setContentsMargins(10, 10, 10, 10)

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_bar.setStyleSheet("border-radius: 20px; padding: 10px;")
        search_bar.setFixedHeight(40)

        content_widget_layout.addWidget(search_bar)

        main_content = QLabel("Main Content Area")
        main_content.setStyleSheet("font-size: 24px; text-align: center;")
        main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content_widget_layout.addWidget(main_content)

        content_layout.addWidget(sidebar)
        content_layout.addWidget(content_widget)

        main_layout.addLayout(content_layout)

        MainWindow.setCentralWidget(main_widget)