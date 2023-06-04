# Kriptografi

Kriptografi adalah sebuah aplikasi yang dapat digunakan untuk melakukan berbagai operasi kriptografi, seperti enkripsi, dekripsi, dan manajemen database. Aplikasi ini dikembangkan menggunakan bahasa pemrograman Python dan framework Streamlit, serta menggunakan modul MySQL Connector dan Cryptodome.

## Fitur

- Import Data: Dapat mengimpor data untuk dienkripsi atau didekripsi dari file teks.
- Enkripsi: Dapat melakukan enkripsi teks menggunakan algoritma kriptografi AES (Advanced Encryption Standard).
- Dekripsi: Dapat melakukan dekripsi teks yang telah dienkripsi menggunakan algoritma AES.
- Manajemen Database: Dapat melakukan verifikasi login menggunakan database MySQL, serta mengakses dan mengelola data dalam database.

## Penggunaan

1. Install dependensi dengan menjalankan perintah berikut:

   ```shell
   pip install -r requirements.txt

2. Pastikan User telah memiliki server MySQL yang berjalan dan sesuaikan parameter koneksi database pada kode program (host, user, password, database).

3. Jalankan aplikasi dengan perintah berikut:
   ```shell
   streamlit run kriptografi.py

4. Aplikasi akan berjalan di web browser lokal. User akan diminta untuk login sebelum dapat menggunakan fitur-fitur aplikasi. Jika berhasil login, User akan melihat menu dengan pilihan fitur-fitur yang tersedia. Pilihlah salah satu fitur untuk memulai.
