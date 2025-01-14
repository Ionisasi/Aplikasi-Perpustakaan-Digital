import os
import sqlite3
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QLabel, QAbstractItemView,
    QHBoxLayout, QVBoxLayout, QLineEdit, QDialog, QDialogButtonBox,
    QPushButton, QHeaderView
)
from PySide6.QtGui import QIcon
from view.UI_DataKelola import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.headerTitle.setText("DATA ANGGOTA")
        
        self.ui.Tambah_data.setVisible(False)

        self.database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")

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
        """Populate the table with member data from the database."""
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()

                # Base query for member data from User table
                base_query = """
                    SELECT id, nama_lengkap, username, telp, jenis_kelamin, alamat, Role
                    FROM User
                """
                params = []  # Inisialisasi params

                # Add search filter if search term provided
                if search_term:
                    base_query += """
                        WHERE (nama_lengkap LIKE ? OR username LIKE ? OR 
                            telp LIKE ? OR jenis_kelamin LIKE ? OR 
                            alamat LIKE ? OR CAST(Role AS TEXT) LIKE ?)
                    """
                    search_placeholder = f"%{search_term}%"
                    params.extend([search_placeholder] * 6)

                # Tambahkan filter role jika role_search diberikan
                if role_search is not None:
                    if search_term:
                        base_query += " AND Role = ?"
                    else:
                        base_query += " WHERE Role = ?"
                    params.append(role_search)

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
            'ID', 'Nama Lengkap', 'Username', 'Telepon', 'Jenis Kelamin', 'Alamat', 'Role', 'Kelola'
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
                # Translate gender and role columns
                if col_idx == 4:  # Gender column
                    cell_data = "Laki-laki" if cell_data == 'L' else "Perempuan"
                elif col_idx == 6:  # Role column
                    cell_data = "Anggota" if cell_data == 0 else "Admin"

                item = QTableWidgetItem(str(cell_data))
                table.setItem(row_idx, col_idx, item)

            self._add_action_buttons(row_idx)

    def _add_action_buttons(self, row_idx):
        """Add edit and delete buttons to the specified row."""
        btn_widget = QWidget()
        btn_layout = QHBoxLayout(btn_widget)
        btn_layout.setContentsMargins(0, 0, 0, 0)

        # Create styled buttons
        edit_btn = self._create_button('Edit', 'Asset/Icon/Edit.png', '#4CAF50')
        delete_btn = self._create_button('Delete', 'Asset/Icon/Delete.png', '#F44336')

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
        """Open dialog to edit member data."""
        data = self._get_row_data(row)
        dialog = self._create_edit_dialog(data)

        if dialog.exec() == QDialog.Accepted:
            self._save_edited_data(dialog, data['id'])

    def _get_row_data(self, row):
        """Extract data from the specified table row."""
        table = self.ui.view_data
        return {
            'id': table.item(row, 0).text(),
            'nama_lengkap': table.item(row, 1).text(),
            'username': table.item(row, 2).text(),
            'telp': table.item(row, 3).text(),
            'jenis_kelamin': table.item(row, 4).text(),
            'alamat': table.item(row, 5).text(),
            'Role': table.item(row, 6).text()
        }

    def _create_edit_dialog(self, data):
        """Create and configure edit dialog."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Data Anggota")
        dialog.setFixedSize(300, 350)

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
        """Create input fields for the edit dialog, ensuring gender is displayed as L/P."""
        fields = {}
        layout = dialog.layout()

        editable_fields = [
            ('nama_lengkap', "Nama Lengkap:"),
            ('username', "Username:"),
            ('telp', "Telepon:"),
            ('alamat', "Alamat:"),
            ('jenis_kelamin', "Jenis Kelamin:"),
            ('Role', "Role:")
        ]

        for field_name, label in editable_fields:
            input_field = QLineEdit(dialog)
            
            # Handle 'jenis_kelamin' to display L or P as text in QLineEdit
            if field_name == 'jenis_kelamin':
                input_field.setText(str(data[field_name]))  # Only L or P
            elif field_name == 'Role':
                # Display Role as text (Anggota or Admin) in QLineEdit
                role_text = "Anggota" if data[field_name] == '0' else "Admin"  # Check for string '0' or '1'
                input_field.setText(role_text)
            else:
                input_field.setText(str(data[field_name]))
            
            layout.addWidget(QLabel(label))
            layout.addWidget(input_field)
            fields[field_name] = input_field

        return fields
    
    def _save_edited_data(self, dialog, user_id):
        """Save edited data to the database."""
        fields = dialog.findChildren(QLineEdit)
        data = {
            'nama_lengkap': fields[0].text(),
            'username': fields[1].text(),
            'telp': fields[2].text(),
            'alamat': fields[3].text(),
            'jenis_kelamin': fields[4].text(),
            'Role': fields[5].text(),
        }

        # Convert role to '0' for Anggota and '1' for Admin
        if data['Role'].lower() == "anggota":
            data['Role'] = '0'
        else:
            data['Role'] = '1'

        # Convert 'jenis_kelamin' from full text to 'L' or 'P'
        if data['jenis_kelamin'].lower() in ["laki-laki", "l"]:
            data['jenis_kelamin'] = 'L'
        elif data['jenis_kelamin'].lower() in ["perempuan", "p"]:
            data['jenis_kelamin'] = 'P'
        else:
            QMessageBox.warning(self, "Input Invalid", "Jenis Kelamin tidak valid! Harap pilih Laki-laki atau Perempuan.")
            return

        if not all(data.values()):
            QMessageBox.warning(self, "Input Invalid", "Semua kolom harus diisi!")
            return

        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE User
                    SET nama_lengkap=?, username=?, telp=?, alamat=?, jenis_kelamin=?, Role=?
                    WHERE id=?
                """, (
                    data['nama_lengkap'], data['username'], data['telp'],
                    data['alamat'], data['jenis_kelamin'], data['Role'], user_id
                ))
                conn.commit()

            QMessageBox.information(self, "Sukses", "Data berhasil diupdate.")
            self.populate_table()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")


    def delete_data(self, row):
        """Delete member data after confirmation."""
        anggota_id = self.ui.view_data.item(row, 0).text()

        if QMessageBox.question(
            self, "Hapus Data",
            f"Apakah Anda yakin ingin menghapus anggota dengan ID: {anggota_id}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                with sqlite3.connect(self.database_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM User WHERE id = ?", (anggota_id,))
                    conn.commit()

                QMessageBox.information(self, "Sukses", f"Anggota dengan ID {anggota_id} telah dihapus.")
                self.populate_table()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Database error: {e}")