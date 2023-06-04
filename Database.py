import streamlit as st
import mysql.connector
import pandas as pd

# Fungsi untuk membuat koneksi ke database MySQL
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Informatika-20",
        database="kriptografi"
    )
    return conn

# Fungsi untuk mendapatkan daftar nama tabel dalam database
def get_table_names():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    table_names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return table_names

# Fungsi untuk mendapatkan isi tabel berdasarkan nama tabel
def get_table_content(table_name):
    conn = create_connection()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Fungsi untuk menghapus data gambar dari tabel image_files dalam database MySQL
def delete_data(table_name, data_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"DELETE FROM {table_name} WHERE id = %s"
    cursor.execute(query, (data_id,))
    conn.commit()
    conn.close()

# Fungsi untuk mengedit data gambar dalam tabel image_files dalam database MySQL
def edit_data(table_name, data_id, column_name, new_value):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"UPDATE {table_name} SET {column_name} = %s WHERE id = %s"
    cursor.execute(query, (new_value, data_id))
    conn.commit()
    conn.close()

# Fungsi untuk menambah data baru ke tabel dalam database MySQL
def add_data(table_name, data):
    conn = create_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO {table_name} VALUES {data}"
    cursor.execute(query)
    conn.commit()
    conn.close()

# Fungsi untuk halaman database
def database_page():
    st.title("Database")
    st.header("Daftar Tabel")

    # Mendapatkan daftar tabel dari database
    table_names = get_table_names()

    # Menampilkan daftar tabel dalam bentuk selectbox
    selected_table = st.selectbox("Pilih Tabel", table_names)

    if selected_table:
        # Mendapatkan isi tabel terpilih
        table_content = get_table_content(selected_table)

        # Menampilkan isi tabel dalam bentuk dataframe
        st.dataframe(table_content)

        # Mengambil pilihan dari radio option (hapus, edit, atau tambah)
        selected_action = st.radio("Pilihan Opsi", ("Hapus", "Edit", "Tambah"))

        if selected_action == "Hapus":
            # Hapus baris berdasarkan ID
            data_id = st.text_input("ID Data", value="")
            if st.button("Hapus"):
                delete_data(selected_table, data_id)
                st.success(f"Data dengan ID {data_id} berhasil dihapus!")

        elif selected_action == "Edit":
            # Edit baris berdasarkan ID dan kolom yang dipilih
            data_id = st.text_input("ID Data", value="")
            column_name = st.text_input("Kolom yang akan diedit", value="")
            new_value = st.text_input("Nilai Baru", value="")
            if st.button("Edit"):
                edit_data(selected_table, data_id, column_name, new_value)
                st.success(f"Data dengan ID {data_id} berhasil diubah!")

        elif selected_action == "Tambah":
            # Tambah data baru ke tabel
            # Misalnya, jika tabel "users" memiliki kolom id (auto increment), username, dan password, Anda dapat memasukkan data baru dengan format (null, 'nama_pengguna', 'kata_sandi'). 
            data = st.text_input("Data Baru (dalam format yang sesuai dengan tabel)", value="")
            if st.button("Tambah"):
                add_data(selected_table, data)
                st.success("Data baru berhasil ditambahkan!")