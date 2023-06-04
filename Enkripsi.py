import streamlit as st
import mysql.connector
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from io import BytesIO
import hashlib

# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Informatika-20",
        database="kriptografi"
    )
    return conn

# Fungsi untuk mengenkripsi teks menggunakan AES
def encrypt_text(text, key):
    key = hashlib.sha256(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text, AES.block_size))
    return encrypted_text

# Fungsi untuk mengenkripsi gambar menggunakan BASE64 dan AES
def encrypt_image(file_data, key):
    encrypted_data = encrypt_text(file_data, key)
    encoded_data = base64.b64encode(encrypted_data).decode('ascii')
    return encoded_data

# Fungsi untuk menyimpan data gambar terenkripsi ke tabel encrypted_files dalam database MySQL
def insert_encrypted_file(filename, encrypted_data, key, nama):
    conn = create_connection()
    cursor = conn.cursor()
    # Ganti ekstensi file menjadi .txt
    new_filename = nama.rsplit(".", 1)[0] + ".txt"
    query = "INSERT INTO file_enkripsi (filename, file_terenkripsi, kunci_enkripsi) VALUES (%s, %s, %s)"
    cursor.execute(query, (new_filename, encrypted_data, key))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan daftar nama file gambar yang telah diimpor
def get_image_filenames():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT filename FROM image_files"
    cursor.execute(query)
    filenames = [row[0] for row in cursor.fetchall()]
    conn.close()
    return filenames

# Fungsi untuk mendapatkan data gambar dari tabel image_files berdasarkan nama file
def get_image_data(filename):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT data FROM image_files WHERE filename = %s"
    cursor.execute(query, (filename,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Fungsi untuk halaman enkripsi
def encryption_page():
    st.title("Enkripsi Gambar")

    source_option = "Pilih dari Database"

    if source_option == "Pilih dari Database":
        # Mendapatkan daftar file gambar dari tabel image_files
        image_filenames = get_image_filenames()

        # Menampilkan daftar file gambar dalam bentuk selectbox
        selected_filename = st.selectbox("Pilih File Gambar", image_filenames)

        if selected_filename:
            # Mendapatkan data gambar dari tabel image_files
            image_data = get_image_data(selected_filename)

            if image_data:
                image_data = BytesIO(image_data)  # Konversi ke BytesIO
                st.image(image_data, use_column_width=True, caption=f"{selected_filename}")

                st.header("Masukkan Kunci Enkripsi")
                nama = st.text_input("Input Nama File:")
                key = st.text_input("Input Kunci Enkripsi:")

                if st.button("Enkripsi"):
                    key = key.encode('utf-8')  # Convert key to bytes
                    encoded_data = encrypt_image(image_data.getvalue(), key)
                    st.text_area("Encoded Text", value=encoded_data)

                    # Memasukkan data terenkripsi ke database
                    insert_encrypted_file(selected_filename, encoded_data, key, nama)

                    # Simpan gambar terenkripsi ke file teks
                    new_filename = nama + ".txt"
                    with open(new_filename, "w") as file:
                        file.write(encoded_data)

                    # Tambahkan tombol download
                    st.download_button("Download Encoded Text", data=encoded_data, file_name=new_filename)

                    st.success(f"Enkripsi berhasil. Gambar terenkripsi disimpan sebagai {new_filename} dan data tersimpan di database.")