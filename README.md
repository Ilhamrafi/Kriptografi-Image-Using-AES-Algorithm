# Kriptografi

Kriptografi adalah sebuah aplikasi yang dapat digunakan untuk melakukan berbagai operasi kriptografi, seperti enkripsi, dekripsi, dan manajemen database. Aplikasi ini dikembangkan menggunakan bahasa pemrograman Python dan framework Streamlit, serta menggunakan modul MySQL Connector dan Cryptodome.

## Fitur

- Import Data: Anda dapat mengimpor data untuk dienkripsi atau didekripsi dari file teks.
- Enkripsi: Anda dapat melakukan enkripsi teks menggunakan algoritma kriptografi AES (Advanced Encryption Standard).
- Dekripsi: Anda dapat melakukan dekripsi teks yang telah dienkripsi menggunakan algoritma AES.
- Manajemen Database: Anda dapat melakukan verifikasi login menggunakan database MySQL, serta mengakses dan mengelola data dalam database.

## Penggunaan

1. Install dependensi dengan menjalankan perintah berikut:

   ```shell
   pip install -r requirements.txt

2. Pastikan Anda telah memiliki server MySQL yang berjalan dan sesuaikan parameter koneksi database pada kode program (host, user, password, database).

3. Jalankan aplikasi dengan perintah berikut:
   ```shell
   streamlit run kriptografi.py

4. Aplikasi akan berjalan di web browser lokal. Anda akan diminta untuk login sebelum dapat menggunakan fitur-fitur aplikasi. Jika berhasil login, Anda akan melihat menu dengan pilihan fitur-fitur yang tersedia. Pilihlah salah satu fitur untuk memulai.
