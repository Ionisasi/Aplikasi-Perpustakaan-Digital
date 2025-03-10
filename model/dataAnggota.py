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
from utils import resource_path

def get_icon_path(icon_name):
        return resource_path(f"Asset/Icon/{icon_name}")
    
class DataAnggotaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()
        self.ui.setupUi(self)
        self.database_path = resource_path("database/perpusdigi.db")
        
        self.ui.Tambah_data.setVisible(False)
        
        # Atur debouncing pencarian
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.on_search)

        # Hubungkan handler event
        self.ui.Search_action.textChanged.connect(self.start_search_timer)
        
        # Populasi tabel awal
        self.populate_table()

    def showEvent(self, event):
        # Memanggil pembaruan tabel setiap kali halaman ditampilkan
        self.populate_table()
        super().showEvent(event)

    def start_search_timer(self):
        # Ulangi timer jika pengguna terus mengetik
        self.search_timer.start(300)

    def on_search(self):
        # Menghentikan timer dan memulai pencarian
        self.current_page = 0
        search_term = self.ui.Search_action.text().strip()

        # Cek apakah search term untuk Role
        if search_term.lower() == "administrator":
            role_search = 1
        elif search_term.lower() == "anggota":
            role_search = 2
        else:
            role_search = None

        # Mengisi tabel dengan data yang sudah difilter
        self.populate_table(search_term, role_search)

    def populate_table(self, search_term="", role_search=None):
        # Mengisi tabel dengan data pengguna yang sesuai
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()

                # Query dasar untuk data pengguna
                base_query = """
                    SELECT nama_lengkap, username, telp, jenis_kelamin, alamat, Role 
                    FROM User
                """
                params = []  # Inisialisasi params

                # Tambahkan filter pencarian jika search term diberikan
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
        # Mengatur tampilan tabel
        table = self.ui.view_data
        table.setColumnCount(7)  # Sertakan kolom untuk tombol kelola
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setHorizontalHeaderLabels([
            'Nama', 'Username', 'Telepon', 'Jenis Kelamin', 'Alamat', 'Role', 'Kelola'
        ])
        
        # Konfigurasikan tampilan header
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStretchLastSection(True)

    def _populate_table_data(self, rows):
        # Mengisi tabel dengan data pengguna
        table = self.ui.view_data
        table.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                # Format data untuk jenis kelamin dan role
                if col_idx == 3:  # Kolom jenis kelamin
                    cell_data = 'Laki-Laki' if cell_data == 'L' else 'Perempuan'
                elif col_idx == 5:  # Kolom role
                    cell_data = 'Administrator' if cell_data == 1 else 'Anggota'

                item = QTableWidgetItem(str(cell_data))
                table.setItem(row_idx, col_idx, item)

            self._add_action_buttons(row_idx)

    def _add_action_buttons(self, row_idx):
        # Tambahkan tombol kelola untuk setiap baris
        btn_widget = QWidget()
        btn_layout = QHBoxLayout(btn_widget)
        btn_layout.setContentsMargins(0, 0, 0, 0)

        # Buat tombol edit dan hapus
        edit_btn = self._create_button('Edit', get_icon_path('Edit.png'), '#4CAF50')
        delete_btn = self._create_button('Delete', get_icon_path('Delete.png'), '#F44336')

        # Hubungkan tombol
        edit_btn.clicked.connect(lambda checked, r=row_idx: self.edit_data(r))
        delete_btn.clicked.connect(lambda checked, r=row_idx: self.hapus_data(r))

        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(delete_btn)
        self.ui.view_data.setCellWidget(row_idx, 6, btn_widget)

    def _create_button(self, name, icon_path, base_color):
        # Buat tombol dengan ikon dan warna yang diberikan
        btn = QPushButton()
        btn.setIcon(QIcon(icon_path))
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {base_color};
                color: white;
                border-radius: 5px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {self._darken_color(base_color, 10)};
            }}
            QPushButton:pressed {{
                background-color: {self._darken_color(base_color, 20)};
            }}
        """)
        return btn

    @staticmethod
    def _darken_color(hex_color, percent):
        # Gelapkan warna dengan persentase yang diberikan
        return hex_color

    def edit_data(self, row):
        # Mengambil data dari baris tabel
        data = self._get_row_data(row)
        dialog = self._create_edit_dialog(data)

        if dialog.exec() == QDialog.Accepted:
            self._save_edited_data(dialog, data['username'])

    def _get_row_data(self, row):
        # Ekstrak data dari baris tabel
        table = self.ui.view_data
        return {
            'username': table.item(row, 1).text(),
            'nama_lengkap': table.item(row, 0).text(),
            'telp': table.item(row, 2).text(),
            'jenis_kelamin': 'L' if table.item(row, 3).text() == 'Laki-Laki' else 'P',
            'alamat': table.item(row, 4).text(),
            'role': table.item(row, 5).text()
        }

    def _create_edit_dialog(self, data):
        # Membuat dialog untuk mengedit data
        dialog = QDialog(self)
        dialog.setWindowTitle("Edit Data Anggota")
        dialog.setFixedSize(300, 350)
        # Terapkan styling ke dialog
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
        # Membuat field input untuk dialog edit
        fields = {}
        layout = dialog.layout()

        # Field username (read-only)
        username_input = QLineEdit(dialog)
        username_input.setText(data['username'])
        username_input.setReadOnly(True)
        layout.addWidget(QLabel("Username (Tidak dapat diubah):"))
        layout.addWidget(username_input)
        fields['username'] = username_input

        # Field input yang dapat diubah
        editable_fields = [
            ('nama_lengkap', "Nama Lengkap:"),
            ('telp', "Telepon:"),
            ('jenis_kelamin', "Jenis Kelamin (L/P):"),
            ('alamat', "Alamat:"),
            ('role', "Role:")
        ]

        for field_name, label in editable_fields:
            input_field = QLineEdit(dialog)
            input_field.setText(str(data[field_name]))
            layout.addWidget(QLabel(label))
            layout.addWidget(input_field)
            fields[field_name] = input_field

        return fields

    def _save_edited_data(self, dialog, username):
        # Simpan data yang diedit ke database
        fields = dialog.findChildren(QLineEdit)
        data = {field.objectName(): field.text() for field in fields}

        if not all(data.values()):
            QMessageBox.warning(self, "Input Invalid", "Semua kolom harus diisi!")
            return

        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()
                cursor.execute(""" 
                    UPDATE User 
                    SET nama_lengkap=?, telp=?, jenis_kelamin=?, alamat=?, Role=? 
                    WHERE username=?
                """, (
                    data['nama_lengkap'], data['telp'], data['jenis_kelamin'], 
                    data['alamat'], data['role'], username
                ))
                conn.commit()

            QMessageBox.information(self, "Sukses", "Data berhasil diupdate.")
            self.populate_table()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def hapus_data(self, row):
        # Hapus data dari database
        nama = self.ui.view_data.item(row, 0).text()
        
        if QMessageBox.question(
            self, "Hapus Data", 
            f"Apakah Anda yakin ingin menghapus data untuk: {nama}?", 
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                with sqlite3.connect(self.database_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM User WHERE nama_lengkap = ?", (nama,))
                    conn.commit()

                QMessageBox.information(self, "Sukses", f"Data untuk {nama} telah dihapus.")
                self.populate_table()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Database error: {e}")