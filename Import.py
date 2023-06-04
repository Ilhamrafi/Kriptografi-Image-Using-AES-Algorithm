import streamlit as st
import mysql.connector

# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Informatika-20",
        database="kriptografi"
    )
    return conn

# Fungsi untuk menyimpan data gambar ke tabel image_files dalam database MySQL
def insert_image(filename, format, data):
    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO image_files (filename, format, data) VALUES (%s, %s, %s)"
    cursor.execute(query, (filename, format, data))
    conn.commit()
    conn.close()

# Fungsi untuk halaman utama
def import_page():
    st.title("Sistem Kriptografi Gambar Menggunakan Algoritma AES 128")
    st.header("Import Gambar")

    file = st.file_uploader("Unggah file gambar", type=["jpg", "png", "jpeg"], key="image_file_uploader",
                            help="Only .jpg, .png, .jpeg files allowed", accept_multiple_files=False)
    filename = st.text_input("Nama File", max_chars=100)
    format_file = ""

    if file is not None:
        format_file = "." + file.name.split(".")[-1].lower()

    if format_file:
        st.write(f"Format File: {format_file}")

    if file is not None and filename and format_file:
        file_data = file.read()
        st.image(file_data, use_column_width=True, caption=filename + format_file)

        if st.button("Simpan ke Database"):
            insert_image(filename + format_file, format_file, file_data)
            st.success(f"Gambar {filename + format_file} berhasil disimpan ke database!")
        else:
            st.warning("Mohon lengkapi nama file dan pastikan format file terbaca.")
