import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QSpacerItem
)
from PySide6.QtGui import QPixmap, QIcon

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Perpustakaan Digital")
        self.setGeometry(100, 100, 1080, 700)
        self.setWindowIcon(QIcon("Buku.png"))

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
        icon_label.setPixmap(QPixmap("Buku.png"))
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
        profile_icon.setPixmap(QPixmap("Admin1.png"))
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

        def create_sidebar_button(text, theme_icon=None, fallback_icon=None):
            button = QPushButton(text)
            button.setCheckable(True)
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
                QPushButton:checked {
                    background-color: rgb(0, 100, 200);
                    color: #ffffff;
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

            button.clicked.connect(lambda: self.on_sidebar_button_click(button))
            self.sidebar_buttons.append(button)
            return button

        dashboard_button = create_sidebar_button("Dashboard", "go-home", "icons/dashboard.png")
        koleksi_button = create_sidebar_button("Koleksi", None, "icons8-book-64.png")
        kelola_button = create_sidebar_button("Kelola Data", "folder-open", "icons/folder-open.png")
        log_data_button = create_sidebar_button("Log Data", "accessories-dictionary", "icons/log-data.png")

        sidebar_layout.addWidget(dashboard_button)
        sidebar_layout.addWidget(koleksi_button)
        sidebar_layout.addWidget(kelola_button)
        sidebar_layout.addWidget(log_data_button)

        menu2_label = QLabel("Settings")
        menu2_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #555555; background-color: rgb(0, 24, 35); padding: 5px;")
        menu2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sidebar_layout.addWidget(menu2_label)

        logout_button = create_sidebar_button("Logout", None, "icons8-logout-50.png")

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

        self.setCentralWidget(main_widget)

    def on_sidebar_button_click(self, clicked_button):
        for button in self.sidebar_buttons:
            if button != clicked_button:
                button.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = Dashboard()
    window.show()

    app.exec()
