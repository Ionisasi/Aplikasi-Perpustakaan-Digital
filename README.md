# Aplikasi Perpustakaan Digital

Aplikasi perpustakaan digital ini bertujuan untuk mengelola dan menampilkan buku-buku dalam koleksi perpustakaan, baik yang termasuk dalam kategori fiksi maupun non-fiksi. Pengguna dapat meminjam buku dan mengembalikannya, serta melihat detail buku yang tersedia.

Proyek ini dibuat untuk penyelesaian UAS mata kuliah praktikum pemrograman visual dengan kami sebagai kelompok 2. Aplikasi ini memungkinkan pengelolaan buku-buku, peminjaman, pengembalian, serta pelacakan buku yang dipinjam. Dengan menggunakan PySide6 dan SQLite, aplikasi ini menyediakan antarmuka yang mudah digunakan dan interaktif.

### Fitur-Fitur Utama

1. **Koleksi Fiksi dan Non-Fiksi**  
   Pengguna dapat melihat daftar buku berdasarkan kategori fiksi dan non-fiksi, yang diambil langsung dari database.

2. **Pencarian Buku**  
   Pengguna dapat mencari buku dengan mengetikkan judul atau pengarang pada bagian pencarian yang tersedia. Fitur ini bekerja dengan filter langsung yang memudahkan pencarian buku di koleksi perpustakaan.

3. **Peminjaman Buku**  
   Pengguna dapat meminjam buku dari koleksi yang tersedia. Setelah buku dipinjam, tampilan akan memperbarui status buku yang dipinjam oleh pengguna.

4. **Pengembalian Buku**  
   Pengguna dapat mengembalikan buku yang telah dipinjam. Aplikasi akan memproses pengembalian dan menghitung denda jika ada keterlambatan.

5. **Tampilan Buku Interaktif**  
   Setiap buku dilengkapi dengan tampilan gambar sampul dan informasi penting seperti judul, pengarang, ,tahun terbitm dan penerbit.


## Struktur Database

Database SQLite digunakan untuk menyimpan data perpustakaan. Struktur tabel yang digunakan adalah sebagai berikut:

### Tabel `User`
- `id`: ID pengguna (primary key).
- `nama_lengkap`: Nama lengkap pengguna.
- `username`: Username pengguna.
- `password`: Password pengguna.
- `telp`: Nomor telepon pengguna.
- `jenis_kelamin`: Jenis kelamin pengguna (`L` atau `P`).
- `alamat`: Alamat pengguna.
- `Role`: Peran pengguna (misal: admin, anggota).

### Tabel `buku`
- `id`: ID buku (primary key).
- `judul`: Judul buku.
- `tahun_terbit`: Tahun terbit buku.
- `pengarang`: Pengarang buku.
- `penerbit`: Penerbit buku.
- `kategori`: Kategori buku (`Fiksi` atau `Non Fiksi`).
- `cover`: Path ke gambar sampul buku.
- `jumlah`: Jumlah salinan buku yang tersedia.
- `volume_id`: ID volume buku.

### Tabel `peminjaman`
- `id`: ID peminjaman (primary key).
- `tanggal_pinjam`: Tanggal peminjaman.
- `tanggal_kembali`: Tanggal tenggat pengembalian buku.
- `anggota_id`: ID anggota yang meminjam (foreign key dari `User.id`).

### Tabel `peminjaman_detail`
- `peminjaman_id`: ID peminjaman (foreign key).
- `buku_id`: ID buku (foreign key).
- **Composite Primary Key**: (`peminjaman_id`, `buku_id`).

### Tabel `pengembalian`
- `id`: ID pengembalian (primary key).
- `tanggal_pengembalian`: Tanggal pengembalian buku.
- `denda`: Denda jika pengembalian terlambat.
- `peminjaman_id`: ID peminjaman (foreign key).
- `anggota_id`: ID anggota yang mengembalikan buku (foreign key).

### Tabel `pengembalian_detail`
- `pengembalian_id`: ID pengembalian (foreign key).
- `buku_id`: ID buku yang dikembalikan (foreign key).
- **Composite Primary Key**: (`pengembalian_id`, `buku_id`).

## Struktur Proyek

- **model**: Berisi logika aplikasi dan interaksi dengan database.
- **view**: UI file yang dibuat menggunakan Qt Designer, dan kemudian diubah menjadi file Python.
- **Asset**: Folder yang menyimpan aset visual seperti ikon dan gambar sampul buku.

## Instalasi

1. Clone repositori ini:
    ```bash
    git clone https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Jalankan aplikasi:
    ```bash
    python main.py
    ```

## Menjalankan Aplikasi dalam Mode Executable (Menggunakan PyInstaller)

Untuk membuat aplikasi menjadi file executable, Anda dapat menggunakan PyInstaller. Berikut adalah perintah yang digunakan untuk membundel aplikasi menjadi satu file:

Pastikan anda sudah menginstal pyinstaller, jika belum jalankan perintah ini di cmd pada folder tempat anda mengclone repository ini.
```bash
pip install pyinstaller
```
Jadikan executable:
```bash
pyinstaller --noconsole --onefile --add-data "utils.py;." --add-data "Asset/cover-img;Asset/cover-img" --add-data "database/perpusdigi.db;database" --add-data "view;view" --add-data "model;model" --add-data "Asset/Icon;Asset/Icon" main.py --clean
```

## License

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE).