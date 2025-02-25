import os
import sqlite3
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QLabel, QAbstractItemView,
    QHBoxLayout, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox,
    QPushButton, QHeaderView
)
from PySide6.QtGui import QIcon
from view.UI_DataKelola import Ui_Form as Ui_DataBuku
from utils import resource_path

def get_icon_path(icon_name):
        return resource_path(f"Asset/Icon/{icon_name}")

class DataBukuPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataBuku()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.headerTitle.setText("DATA BUKU")
        
        self.ui.Tambah_data.setVisible(False)

        self.database_path = resource_path("database/perpusdigi.db")

        # Setup search debouncing
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.on_search)
        
        # Connect event handlers
        self.ui.Search_action.textChanged.connect(self.start_search_timer)

        # Initial table population
        self.populate_table()

    def start_search_timer(self):
        """Start debounce timer for search functionality."""
        self.search_timer.start(300)

    def on_search(self):
        """Handle search event."""
        search_term = self.ui.Search_action.text().strip()
        self.populate_table(search_term)

    def populate_table(self, search_term=""):
        """Populate the table with book data from database."""
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()

                # Base query for book data
                base_query = """
                    SELECT id, judul, tahun_terbit, pengarang, penerbit, kategori, jumlah
                    FROM buku
                """
                params = []

                # Add search filter if search term provided
                if search_term:
                    base_query += """
                        WHERE judul LIKE ? OR pengarang LIKE ? OR penerbit LIKE ? OR kategori LIKE ?
                    """
                    search_placeholder = f"%{search_term}%"
                    params.extend([search_placeholder] * 4)

                cursor.execute(base_query, params)
                rows = cursor.fetchall()

                self._setup_table()
                self._populate_table_data(rows)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def _setup_table(self):
        """Configure table settings."""
        table = self.ui.view_data
        table.setColumnCount(8)  # Include column for manage buttons
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setHorizontalHeaderLabels([
            'ID', 'Judul', 'Tahun Terbit', 'Pengarang', 'Penerbit', 'Kategori', 'Jumlah', 'Kelola'
        ])

        # Configure header appearance
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)

        # Hide ID column (index 0)
        table.setColumnHidden(0, True)


    def _populate_table_data(self, rows):
        """Fill table with data rows."""
        table = self.ui.view_data
        table.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                table.setItem(row_idx, col_idx, item)

            self._add_action_buttons(row_idx)

    def _add_action_buttons(self, row_idx):
        """Add edit and delete buttons to the specified row."""
        btn_widget = QWidget()
        btn_layout = QHBoxLayout(btn_widget)
        btn_layout.setContentsMargins(0, 0, 0, 0)

        # Create styled buttons
        edit_btn = self._create_button('Edit', get_icon_path('Edit.png'), '#4CAF50')
        delete_btn = self._create_button('Delete', get_icon_path('Delete.png'), '#F44336')

        # Connect button signals
        edit_btn.clicked.connect(lambda checked, r=row_idx: self.edit_data(r))
        delete_btn.clicked.connect(lambda checked, r=row_idx: self.delete_data(r))

        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(delete_btn)
        self.ui.view_data.setCellWidget(row_idx, 7, btn_widget)

    def _create_button(self, name, icon_path, base_color):
        """Create a styled button with icon."""
        btn = QPushButton()
        btn.setIcon(QIcon(icon_path))
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {base_color};
                color: white;
                border-radius: 5px;
                padding: 5px;
            }}
        """)
        return btn

    def edit_data(self, row):
        """Open dialog to edit book data."""
        data = self._get_row_data(row)
        dialog = self._create_edit_dialog(data)

        if dialog.exec() == QDialog.Accepted:
            self._save_edited_data(dialog, data['id'])

    def _get_row_data(self, row):
        """Extract data from the specified table row."""
        table = self.ui.view_data
        return {
            'id': table.item(row, 0).text(),
            'judul': table.item(row, 1).text(),
            'tahun_terbit': table.item(row, 2).text(),
            'pengarang': table.item(row, 3).text(),
            'penerbit': table.item(row, 4).text(),
            'kategori': table.item(row, 5).text(),
            'jumlah': table.item(row, 6).text()
        }

    def _create_edit_dialog(self, data):
        """Create and configure edit dialog."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Data Buku")
        dialog.setFixedSize(500, 500)

        # Apply styling to the dialog
        dialog.setStyleSheet("""
            QWidget {
                background-color: rgb(0, 33, 48);
                color: white;
                font-weight: bold;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #ffffff;
                padding-left: 20px;
            }
            QLineEdit {
                background-color: rgb(30, 30, 30);
                color: white;
                padding-left: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        layout = QVBoxLayout(dialog)
        fields = self._create_edit_fields(dialog, data)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        return dialog

    def _create_edit_fields(self, dialog, data):
        """Create input fields for edit dialog."""
        fields = {}
        layout = dialog.layout()

        editable_fields = [
            ('judul', "Judul:"),
            ('tahun_terbit', "Tahun Terbit:"),
            ('pengarang', "Pengarang:"),
            ('penerbit', "Penerbit:"),
            ('kategori', "Kategori:"),
            ('jumlah', "Jumlah:")
        ]

        for field_name, label in editable_fields:
            input_field = QLineEdit(dialog)
            input_field.setText(str(data[field_name]))
            layout.addWidget(QLabel(label))
            layout.addWidget(input_field)
            fields[field_name] = input_field

        return fields

    def _save_edited_data(self, dialog, book_id):
        """Save edited data to database."""
        fields = dialog.findChildren(QLineEdit)
        data = {
            'judul': fields[0].text(),
            'tahun_terbit': fields[1].text(),
            'pengarang': fields[2].text(),
            'penerbit': fields[3].text(),
            'kategori': fields[4].text(),
            'jumlah': fields[5].text(),
        }

        if not all(data.values()):
            QMessageBox.warning(self, "Input Invalid", "Semua kolom harus diisi!")
            return

        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE buku
                    SET judul=?, tahun_terbit=?, pengarang=?, penerbit=?, kategori=?, jumlah=?
                    WHERE id=?
                """, (
                    data['judul'], data['tahun_terbit'], data['pengarang'],
                    data['penerbit'], data['kategori'], data['jumlah'], book_id
                ))
                conn.commit()

            QMessageBox.information(self, "Sukses", "Data berhasil diupdate.")
            self.populate_table()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")


    def delete_data(self, row):
        """Delete book data after confirmation."""
        book_id = self.ui.view_data.item(row, 0).text()

        if QMessageBox.question(
            self, "Hapus Data",
            f"Apakah Anda yakin ingin menghapus buku dengan ID: {book_id}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                with sqlite3.connect(self.database_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM buku WHERE id = ?", (book_id,))
                    conn.commit()

                QMessageBox.information(self, "Sukses", f"Buku dengan ID {book_id} telah dihapus.")
                self.populate_table()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Database error: {e}")
