# Aplikasi Perpustakaan Digital

Aplikasi perpustakaan digital ini bertujuan untuk mengelola dan menampilkan buku-buku dalam koleksi perpustakaan, baik yang termasuk dalam kategori fiksi maupun non-fiksi. Pengguna dapat meminjam buku dan mengembalikannya, serta melihat detail buku yang tersedia.

Proyek ini dibuat untuk penyelesaian UAS mata kuliah praktikum pemrograman visual dengan kami sebagai **Kelompok 2**. Aplikasi ini memungkinkan pengelolaan buku-buku, peminjaman, pengembalian, serta pelacakan buku yang dipinjam. Dengan menggunakan PySide6 dan SQLite, aplikasi ini menyediakan antarmuka yang mudah digunakan dan interaktif.

---

## Fitur-Fitur Utama

1. **Koleksi Fiksi dan Non-Fiksi**  
   Pengguna dapat melihat daftar buku berdasarkan kategori fiksi dan non-fiksi, yang diambil langsung dari database.

2. **Pencarian Buku**  
   Pengguna dapat mencari buku dengan mengetikkan judul atau pengarang pada bagian pencarian yang tersedia. Fitur ini bekerja dengan filter langsung yang memudahkan pencarian buku di koleksi perpustakaan.

3. **Peminjaman Buku**  
   Pengguna dapat meminjam buku dari koleksi yang tersedia. Setelah buku dipinjam, tampilan akan memperbarui status buku yang dipinjam oleh pengguna.

4. **Pengembalian Buku**  
   Pengguna dapat mengembalikan buku yang telah dipinjam. Aplikasi akan memproses pengembalian dan menghitung denda jika ada keterlambatan.

5. **Tampilan Buku Interaktif**  
   Setiap buku dilengkapi dengan tampilan gambar sampul dan informasi penting seperti judul, pengarang, tahun terbit, dan penerbit.

---

## Beta Release

Versi **Beta 0.1.0** dari aplikasi ini telah dirilis dan mencakup file executable (`https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases`) untuk memudahkan pengujian tanpa perlu menginstal dependensi Python secara manual.

Anda dapat mengunduh executable ini langsung dari halaman **Releases** di repository GitHub. Pastikan untuk membaca dokumentasi ini sebelum menggunakan aplikasi untuk memahami fitur-fiturnya.

---

## Instalasi

### Clone Repositori

```bash
git clone https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases
```

### Install Dependencies

```bash
pip install -r https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases
```

### Jalankan Aplikasi

```bash
python https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases
```

---

## Menjalankan Aplikasi dalam Mode Executable

Untuk membuat executable sendiri, gunakan PyInstaller dengan perintah berikut:

1. Pastikan PyInstaller telah diinstal:
   ```bash
   pip install pyinstaller
   ```

2. Buat executable:
   ```bash
   pyinstaller --noconsole --onefile --add-data "https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases;." --add-data "Asset/cover-img;Asset/cover-img" --add-data "https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases;database" --add-data "view;view" --add-data "model;model" --add-data "Asset/Icon;Asset/Icon" https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases --clean
   ```

3. File executable (`https://github.com/Ionisasi/Aplikasi-Perpustakaan-Digital/releases`) akan tersedia di folder `dist`.

---

## Struktur Proyek

- **model**: Berisi logika aplikasi dan interaksi dengan database.
- **view**: UI file yang dibuat menggunakan Qt Designer, dan kemudian diubah menjadi file Python.
- **Asset**: Folder yang menyimpan aset visual seperti ikon dan gambar sampul buku.

---

## License

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE).