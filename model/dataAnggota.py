import os
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from view.UI_DataAnggota import Ui_Form as Ui_DataAnggota

class DataAnggotaPage(QWidget):  # Pastikan ini subclass QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAnggota()  # Inisialisasi objek UI
        self.ui.setupUi(self)  # Setup UI pada widget

        self.populate_table()  # Panggil fungsi untuk mengisi tabel
        self.ui.AnggotaTable.selectionModel().selectionChanged.connect(self.on_table_row_selected)  # Menghubungkan pilihan baris dengan fungsi

        # Hubungkan tombol dengan fungsi
        self.ui.ubahBtn.clicked.connect(self.ubah_data)
        self.ui.searchBtn.clicked.connect(self.search_data)
        self.ui.deselectBtn.clicked.connect(self.clearSelection)  # Menghubungkan clearSelection dengan tombol

    def populate_table(self):
        # Fungsi untuk mengisi tabel
        database_path = os.path.join(os.path.dirname(__file__), "../database/perpusdigi.db")  # Path ke database
        try:
            # Koneksi ke database
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()

            # Query untuk mengambil data anggota
            cursor.execute("SELECT nama, email, telp, jenis_kelamin, alamat FROM anggota")
            rows = cursor.fetchall()

            # Set jumlah baris pada tabel
            self.ui.AnggotaTable.setRowCount(len(rows))  # Set jumlah baris
            self.ui.AnggotaTable.setColumnCount(5)  # 5 kolom untuk setiap field (nama, email, telp, jenis_kelamin, alamat)

            # Set header tabel
            self.ui.AnggotaTable.setHorizontalHeaderLabels(['Nama', 'Email', 'Telp', 'Jenis Kelamin', 'Alamat'])

            # Isi tabel dengan data dari database
            for row_index, row in enumerate(rows):
                for col_index, cell_data in enumerate(row):
                    # Ubah jenis kelamin menjadi 'Laki-Laki' atau 'Perempuan'
                    if col_index == 3:
                        if cell_data == 'L':
                            cell_data = 'Laki-Laki'
                        elif cell_data == 'P':
                            cell_data = 'Perempuan'

                    item = QTableWidgetItem(str(cell_data))  # Buat item dari data
                    self.ui.AnggotaTable.setItem(row_index, col_index, item)

            conn.close()

        except sqlite3.Error as e:
            # Tampilkan pesan error jika gagal
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan pada database: {e}")

    def on_table_row_selected(self, selected, deselected):
        # Ambil baris yang dipilih
        selected_row = self.ui.AnggotaTable.currentRow()

        # Cek apakah baris yang dipilih valid
        if selected_row >= 0:
            # Ambil data dari baris yang dipilih
            nama = self.ui.AnggotaTable.item(selected_row, 0).text()  # Nama
            email = self.ui.AnggotaTable.item(selected_row, 1).text()  # Email
            telp = self.ui.AnggotaTable.item(selected_row, 2).text()  # Telp
            jenis_kelamin = self.ui.AnggotaTable.item(selected_row, 3).text()  # Jenis Kelamin
            alamat = self.ui.AnggotaTable.item(selected_row, 4).text()  # Alamat

            # Set data ke form
            self.ui.namaInput.setText(nama)
            self.ui.emailInput.setText(email)
            self.ui.teleponInput.setText(telp)
            self.ui.alamatInput.setText(alamat)

            # Set jenis kelamin ke form
            if jenis_kelamin == 'Laki-Laki':
                self.ui.lakiCheckBox.setChecked(True)
                self.ui.PerempuanCheckBox.setChecked(False)
            elif jenis_kelamin == 'Perempuan':
                self.ui.lakiCheckBox.setChecked(False)
                self.ui.PerempuanCheckBox.setChecked(True)

    def ubah_data(self):
        # Fitur ini masih dalam pengembangan
        QMessageBox.information(self, "Pemberitahuan", "Fitur ini masih dalam pengembangan")

    def search_data(self):
        # Ambil nilai dari QLineEdit pencarian
        nama = self.ui.namaInput.text().lower()
        email = self.ui.emailInput.text().lower()
        telp = self.ui.teleponInput.text().lower()

        row_found = False  # variabel untuk menandakan apakah ada baris yang ditemukan

        # Jika tidak ada nilai pencarian yang dimasukkan, jangan lakukan pencarian
        if not nama and not email and not telp:
            QMessageBox.information(self, "Pencarian", "Silakan masukkan data untuk pencarian.")
            return

        # Loop untuk mencari baris yang sesuai
        for row in range(self.ui.AnggotaTable.rowCount()):
            # Ambil nilai untuk setiap kolom yang relevan
            nama_item = self.ui.AnggotaTable.item(row, 0).text().lower()  # Kolom Nama
            email_item = self.ui.AnggotaTable.item(row, 1).text().lower()  # Kolom Email
            telp_item = self.ui.AnggotaTable.item(row, 2).text().lower()  # Kolom Telp

            # Cek apakah input pencarian sesuai dengan kolom yang diinginkan
            match_found = True 
            if nama and nama not in nama_item:  # Jika nama diisi, cek kecocokan
                match_found = False
            if email and email not in email_item:  # Jika email diisi, cek kecocokan
                match_found = False
            if telp and telp not in telp_item:  # Jika telp diisi, cek kecocokan
                match_found = False

            # Jika semua kondisi cocok, pilih baris dan keluar dari loop
            if match_found:
                self.ui.AnggotaTable.selectRow(row)  # Pilih baris yang cocok
                row_found = True
                break  # Jika ditemukan, berhenti mencari

        # Jika tidak ada baris yang ditemukan, tampilkan pesan
        if not row_found:
            QMessageBox.information(self, "Pencarian", "Data tidak ditemukan.")


    def clearSelection(self):
        # Hapus seleksi pada tabel
        self.ui.AnggotaTable.clearSelection()

        # Kosongkan semua field input
        self.ui.namaInput.clear()
        self.ui.emailInput.clear()
        self.ui.teleponInput.clear()
        self.ui.alamatInput.clear()

        # Set checkbox ke tidak tercentang
        self.ui.lakiCheckBox.setChecked(False)
        self.ui.PerempuanCheckBox.setChecked(False)

        # Hapus fokus dari tabel
        self.ui.AnggotaTable.clearFocus()