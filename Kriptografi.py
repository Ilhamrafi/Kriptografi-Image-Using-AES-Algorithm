import streamlit as st
import mysql.connector
from Cryptodome.Cipher import AES
from Import import *
from Enkripsi import *
from Dekripsi import *
from Database import *

# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Informatika-20",
        database="kriptografi"
    )
    return conn

# Fungsi untuk melakukan verifikasi login
def verify_login(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

# Fungsi untuk halaman login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = verify_login(username, password)
        if result is not None:
            st.success("Login berhasil!")
            st.session_state['is_logged_in'] = True
        else:
            st.error("Username atau password salah!")

# Fungsi utama
def main():
    st.set_page_config(page_title="Kriptografi")

    # Mengecek apakah user sudah login atau belum
    is_logged_in = st.session_state.get('is_logged_in', False)

    if not is_logged_in:
        login_page()
    else:
        selected = st.sidebar.selectbox(
            "Menu",
            ["Import Data", "Enkripsi", "Dekripsi", "Database"],
            format_func=lambda x: "Import Data" if x == "Import Data" else ("Enkripsi" if x == "Enkripsi" else ("Dekripsi" if x == "Dekripsi" else "Database")),
            index=0,
            help="Choose an option"
        )

        if selected == "Import Data":
            import_page()

        elif selected == "Enkripsi":
            encryption_page()

        elif selected == "Dekripsi":
            decryption_page()
        
        elif selected == "Database":
            database_page()

        # Tambahkan tombol logout di bawah selectbox
        if st.sidebar.button("Logout"):
            st.session_state.pop('is_logged_in', None)
            st.experimental_rerun()

if __name__ == "__main__":
    main()