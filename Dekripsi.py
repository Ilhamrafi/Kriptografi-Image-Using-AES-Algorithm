import streamlit as st
import mysql.connector
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
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

# Fungsi untuk mendapatkan data terenkripsi berdasarkan nama file terenkripsi
def get_encrypted_data(filename):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT file_terenkripsi FROM file_enkripsi WHERE filename = %s"
    cursor.execute(query, (filename,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Fungsi untuk mendapatkan daftar nama file terenkripsi dari tabel file_enkripsi
def get_encrypted_filenames():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT filename FROM file_enkripsi"
    cursor.execute(query)
    filenames = [row[0] for row in cursor.fetchall()]
    conn.close()
    return filenames

# Fungsi untuk mendekripsi data menggunakan AES
def decrypt_data(encrypted_data, key):
    try:
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return decrypted_data
    except ValueError:
        pass

# Fungsi untuk halaman dekripsi
def decryption_page():
    st.title("Dekripsi Gambar")
    st.header("Pilih File Terenkripsi")

    # Mendapatkan daftar file terenkripsi dari tabel file_enkripsi
    encrypted_filenames = get_encrypted_filenames()

    # Menampilkan daftar file terenkripsi dalam bentuk selectbox
    selected_filename = st.selectbox("Pilih File Terenkripsi", encrypted_filenames)

    if selected_filename:
        # Mendapatkan data terenkripsi dari tabel file_enkripsi
        encrypted_data = get_encrypted_data(selected_filename)

        if encrypted_data:
            st.header("Kunci Dekripsi")
            key = st.text_input("Kunci Dekripsi")

            if st.button("Dekripsi"):
                key = hashlib.sha256(key.encode()).digest()[:16]  # Menghasilkan kunci dengan panjang 16 byte (128 bit)
                encrypted_data = base64.b64decode(encrypted_data)
                decrypted_data = decrypt_data(encrypted_data, key)

                if decrypted_data is not None:
                    # Tampilkan gambar terdekripsi
                    st.image(decrypted_data, use_column_width=True)

                    # Simpan gambar terdekripsi ke file
                    with open(selected_filename, "wb") as file:
                        file.write(decrypted_data)

                    # Ubah ekstensi file menjadi .jpg
                    output_filename = selected_filename.rsplit(".", 1)[0] + ".jpg"

                    # Simpan gambar terdekripsi sebagai file gambar
                    with open(output_filename, "wb") as file:
                        file.write(decrypted_data)

                    # Tambahkan tombol download
                    st.download_button("Download gambar hasil dekripsi", data=open(output_filename, 'rb'), file_name=output_filename)

                    st.success("Dekripsi berhasil.")