import tkinter as tk  # Mengimpor pustaka Tkinter dan memberi nama pendek 'tk'
from tkinter import messagebox  # Mengimpor modul messagebox untuk menampilkan pesan kesalahan

def hasil_prediksi():
    try:
        # Loop untuk memeriksa setiap kolom input nilai
        for entry in input_nilai:
            nilai = int(entry.get())  # Mengambil nilai dari entry dan mengubahnya menjadi integer
            # Memeriksa apakah nilai berada dalam rentang 0 hingga 100
            if not (0 <= nilai <= 100):
                raise ValueError("nilainya harus antara 0 sampe 100")  # Mengeluarkan kesalahan jika nilai tidak valid
        # Jika semua nilai valid, tampilkan hasil prediksi
        label_hasil.config(text="Hasil Prediksi: Prodi Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika ada input yang tidak valid
        messagebox.showerror("input yang bener", "pastiin semua inputnya itu angka yang bener 0 - 100")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela
root.geometry("400x500")  # Mengatur ukuran jendela

# Membuat label judul di atas aplikasi
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
label_judul.pack(pady=20)  # Menambahkan padding vertikal di sekitar label

input_nilai = []  # List untuk menyimpan kolom input nilai
# Loop untuk membuat 10 kolom input nilai
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label_mata_pelajaran = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label_mata_pelajaran.pack(pady=5)  # Menambahkan padding vertikal di sekitar label
    
    # Membuat kolom input untuk nilai
    entry_nilai = tk.Entry(root)
    entry_nilai.pack(pady=5)  # Menambahkan padding vertikal di sekitar entry
    
    input_nilai.append(entry_nilai)  # Menyimpan entry ke dalam list input_nilai

# Membuat tombol untuk mendapatkan hasil prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=20)  # Menambahkan padding vertikal di sekitar tombol

# Membuat label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 14))
label_hasil.pack(pady=10)  # Menambahkan padding vertikal di sekitar label hasil

# Memulai loop utama aplikasi untuk menampilkan jendela
root.mainloop()