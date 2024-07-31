import tkinter as tk
from tkinter import messagebox

# ID dan password yang valid
VALID_ID = "admin"
VALID_PASSWORD = "escekek123"

# Dictionary untuk menyimpan jumlah sisa kamar untuk setiap tipe kamar
sisa_kamar = {
    'M': 15,
    'S': 20,
    'L': 25,
    'A': 30,
    'E': 10
}

# Dictionary untuk menyimpan rekap penjualan
rekap_penjualan = {
    'Melati': {'jumlah': 0, 'pendapatan': 0, 'total_lama_sewa': 0},
    'Sakura': {'jumlah': 0, 'pendapatan': 0, 'total_lama_sewa': 0},
    'Lily': {'jumlah': 0, 'pendapatan': 0, 'total_lama_sewa': 0},
    'Anggrek': {'jumlah': 0, 'pendapatan': 0, 'total_lama_sewa': 0},
    'Edelweis': {'jumlah': 0, 'pendapatan': 0, 'total_lama_sewa': 0}
}

def format_rupiah(angka):
    return f"Rp.{angka:,.0f}".replace(",", ".")

def login():
    def verify_login():
        user_id = entry_id.get()
        password = entry_password.get()
        if user_id == VALID_ID and password == VALID_PASSWORD:
            login_window.destroy()
            show_main_app()
        else:
            messagebox.showerror("Login Error", "ID atau password salah")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x250")
    login_window.configure(bg="white")

    # Frame untuk konten login
    login_frame = tk.Frame(login_window, bg="white", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(login_frame, text="ID:", bg="white", font=('Arial', 14)).pack(pady=5)
    entry_id = tk.Entry(login_frame, font=('Arial', 14))
    entry_id.pack(pady=5)
    entry_id.bind('<Return>', lambda event: entry_password.focus_set())  # Fokus ke entry_password

    tk.Label(login_frame, text="Password:", bg="white", font=('Arial', 14)).pack(pady=5)
    entry_password = tk.Entry(login_frame, show="*", font=('Arial', 14))
    entry_password.pack(pady=5)
    entry_password.bind('<Return>', lambda event: verify_login())  # Verifikasi login

    tk.Button(login_frame, text="Login", command=verify_login, font=('Arial', 14)).pack(pady=10)

    login_window.mainloop()

def show_main_app():
    def pilih_kamar(kode_kamar):
        global selected_kode_kamar
        selected_kode_kamar = kode_kamar
        frame_pilih_kamar.grid_forget()
        frame_input.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        frame_output.grid(row=0, column=1, padx=10, pady=10, sticky='ne')
        entry_nama_customer.focus_set()

    def enter_key(event):
        if event.widget == entry_nama_petugas:
            entry_nama_customer.focus_set()
        elif event.widget == entry_nama_customer:
            entry_tanggal.focus_set()
        elif event.widget == entry_tanggal:
            entry_bulan.focus_set()
        elif event.widget == entry_bulan:
            entry_tahun.focus_set()
        elif event.widget == entry_tahun:
            entry_lama_sewa.focus_set()
        elif event.widget == entry_lama_sewa:
            entry_uang_bayar.focus_set()
        elif event.widget == entry_uang_bayar:
            hitung_pembayaran()

    def hitung_pembayaran():
        nama_petugas = entry_nama_petugas.get()
        nama_customer = entry_nama_customer.get()
        tanggal_check_in = f"{entry_tanggal.get()}/{entry_bulan.get()}/{entry_tahun.get()}"
        lama_sewa = int(entry_lama_sewa.get())
        uang_bayar = int(entry_uang_bayar.get())
        kode_kamar = selected_kode_kamar

        if kode_kamar not in sisa_kamar:
            messagebox.showerror("Error", "Kode kamar tidak valid")
            return

        if sisa_kamar[kode_kamar] == 0:
            messagebox.showerror("Error", "Kamar tidak tersedia")
            return

        # Menentukan nama kamar dan harga sewa
        if kode_kamar == 'M':
            nama_kamar = 'Melati'
            harga_sewa = 650000
        elif kode_kamar == 'S':
            nama_kamar = 'Sakura'
            harga_sewa = 550000
        elif kode_kamar == 'L':
            nama_kamar = 'Lily'
            harga_sewa = 400000
        elif kode_kamar == 'A':
            nama_kamar = 'Anggrek'
            harga_sewa = 350000
        elif kode_kamar == 'E':
            nama_kamar = 'Edelweis'
            harga_sewa = 1000000

        jumlah_bayar = harga_sewa * lama_sewa

        # Menghitung PPN (diskon)
        if lama_sewa > 5:
            ppn = 0.10 * jumlah_bayar
        elif lama_sewa > 3:
            ppn = 0.05 * jumlah_bayar
        else:
            ppn = 0

        total_bayar = jumlah_bayar - ppn
        uang_kembali = uang_bayar - total_bayar

        # Menampilkan hasil di output field
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Bukti Pemesanan Kamar\nHotel 'SEJUK ASRI'\n")
        output_text.insert(tk.END, f"=================\n")
        output_text.insert(tk.END, f"Nama Petugas: {nama_petugas}\n")
        output_text.insert(tk.END, f"Nama Customer: {nama_customer}\n")
        output_text.insert(tk.END, f"Tanggal Check-in: {tanggal_check_in}\n")
        output_text.insert(tk.END, f"=================\n")
        output_text.insert(tk.END, f"Nama Kamar Yang di pesan: {nama_kamar}\n")
        output_text.insert(tk.END, f"Harga sewa permalam: {format_rupiah(harga_sewa)}\n")
        output_text.insert(tk.END, f"Lama sewa: {lama_sewa} malam\n")
        output_text.insert(tk.END, f"PPN: {format_rupiah(ppn)}\n")
        output_text.insert(tk.END, f"Jumlah Bayar: {format_rupiah(jumlah_bayar)}\n")
        output_text.insert(tk.END, f"Total Bayar: {format_rupiah(total_bayar)}\n")
        output_text.insert(tk.END, f"Uang Bayar: {format_rupiah(uang_bayar)}\n")
        output_text.insert(tk.END, f"Uang Kembali: {format_rupiah(uang_kembali)}\n")
        output_text.insert(tk.END, f"Sisa Kamar {nama_kamar}: {sisa_kamar[kode_kamar] - 1}\n")

        return kode_kamar, nama_kamar, lama_sewa, jumlah_bayar

    def hapus():
        entry_nama_petugas.delete(0, tk.END)
        entry_nama_customer.delete(0, tk.END)
        entry_tanggal.delete(0, tk.END)
        entry_bulan.delete(0, tk.END)
        entry_tahun.delete(0, tk.END)
        entry_lama_sewa.delete(0, tk.END)
        entry_uang_bayar.delete(0, tk.END)
        output_text.delete("1.0", tk.END)
        frame_input.grid_forget()
        frame_output.grid_forget()
        frame_pilih_kamar.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    def cetak():
        result = hitung_pembayaran()
        if result and messagebox.askyesno("Cetak", "Apakah Anda ingin mencetak bukti pemesanan?"):
            kode_kamar, nama_kamar, lama_sewa, jumlah_bayar = result
            sisa_kamar[kode_kamar] -= 1
            rekap_penjualan[nama_kamar]['jumlah'] += 1
            rekap_penjualan[nama_kamar]['pendapatan'] += jumlah_bayar  # Update pendapatan dengan jumlah bayar
            rekap_penjualan[nama_kamar]['total_lama_sewa'] += lama_sewa
            hapus()

    def lihat_rekap():
        rekap_window = tk.Toplevel(root)
        rekap_window.title("Rekap Penjualan")
        rekap_window.geometry("600x400")

        rekap_text = tk.Text(rekap_window, height=20, width=80, bg="white")
        rekap_text.pack(padx=10, pady=10)

        rekap_text.insert(tk.END, "Rekap Penjualan Kamar\nHotel 'SEJUK ASRI'\n")
        rekap_text.insert(tk.END, "========================\n")
        for nama_kamar, data in rekap_penjualan.items():
            rekap_text.insert(tk.END, f"Nama Kamar: {nama_kamar}\n")
            rekap_text.insert(tk.END, f"Jumlah Terjual: {data['jumlah']}\n")
            rekap_text.insert(tk.END, f"Pendapatan: {format_rupiah(data['pendapatan'])}\n")
            rekap_text.insert(tk.END, f"Total Lama Sewa: {data['total_lama_sewa']} malam\n")
            rekap_text.insert(tk.END, "========================\n")

        rekap_text.insert(tk.END, "Sisa Kamar:\n")
        for kode, sisa in sisa_kamar.items():
            nama_kamar = {
                'M': 'Melati',
                'S': 'Sakura',
                'L': 'Lily',
                'A': 'Anggrek',
                'E': 'Edelweis'
            }[kode]
            rekap_text.insert(tk.END, f"{nama_kamar}: {sisa}\n")

    root = tk.Tk()
    root.title("Hotel SEJUK ASRI")
    root.configure(bg="light green")

    # Frame untuk memilih kamar
    global frame_pilih_kamar
    frame_pilih_kamar = tk.Frame(root, bg="light green")
    frame_pilih_kamar.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Frame untuk input fields
    global frame_input
    frame_input = tk.Frame(root, bg="light green")

    # Frame untuk output field
    global frame_output
    frame_output = tk.Frame(root, bg="light green")

    # Input fields
    tk.Label(frame_input, text="Nama Petugas:", bg="light green").grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry_nama_petugas = tk.Entry(frame_input)
    entry_nama_petugas.grid(row=0, column=1, padx=5, pady=5)
    entry_nama_petugas.bind('<Return>', enter_key)

    tk.Label(frame_input, text="Nama Customer:", bg="light green").grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entry_nama_customer = tk.Entry(frame_input)
    entry_nama_customer.grid(row=1, column=1, padx=5, pady=5)
    entry_nama_customer.bind('<Return>', enter_key)

    tk.Label(frame_input, text="Tanggal Check-in (Tanggal/Bulan/Tahun):", bg="light green").grid(row=2, column=0, sticky='w', padx=5, pady=5)
    entry_tanggal = tk.Entry(frame_input, width=5)
    entry_tanggal.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    entry_tanggal.bind('<Return>', enter_key)
    entry_bulan = tk.Entry(frame_input, width=5)
    entry_bulan.grid(row=2, column=1, padx=5, pady=5)
    entry_bulan.bind('<Return>', enter_key)
    entry_tahun = tk.Entry(frame_input, width=8)
    entry_tahun.grid(row=2, column=1, padx=5, pady=5, sticky='e')
    entry_tahun.bind('<Return>', enter_key)

    tk.Label(frame_input, text="Lama Sewa:", bg="light green").grid(row=3, column=0, sticky='w', padx=5, pady=5)
    entry_lama_sewa = tk.Entry(frame_input)
    entry_lama_sewa.grid(row=3, column=1, padx=5, pady=5)
    entry_lama_sewa.bind('<Return>', enter_key)

    tk.Label(frame_input, text="Uang Bayar:", bg="light green").grid(row=4, column=0, sticky='w', padx=5, pady=5)
    entry_uang_bayar = tk.Entry(frame_input)
    entry_uang_bayar.grid(row=4, column=1, padx=5, pady=5)
    entry_uang_bayar.bind('<Return>', enter_key)

    # Output field
    output_text = tk.Text(frame_output, height=20, width=50, bg="white")
    output_text.grid(row=0, column=0, padx=10, pady=10)

    # Buttons
    button_frame = tk.Frame(root, bg="light green")
    button_frame.grid(row=1, column=0, columnspan=2, pady=10)

    tk.Button(button_frame, text="Hitung Pembayaran", command=hitung_pembayaran).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Cetak", command=cetak).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Hapus", command=hapus).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Rekap Penjualan", command=lihat_rekap).grid(row=0, column=3, padx=5)
    tk.Button(button_frame, text="Keluar", command=root.quit).grid(row=0, column=4, padx=5)

    # Menampilkan pilihan kamar
    tk.Button(frame_pilih_kamar, text="Melati \nRp.650.000", font=('Arial', 16), command=lambda: pilih_kamar('M'), width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame_pilih_kamar, text="Sakura \nRp.550.000", font=('Arial', 16), command=lambda: pilih_kamar('S'), width=20, height=2).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_pilih_kamar, text="Lily \nRp.400.000", font=('Arial', 16), command=lambda: pilih_kamar('L'), width=20, height=2).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(frame_pilih_kamar, text="Anggrek \nRp.350.000", font=('Arial', 16), command=lambda: pilih_kamar('A'), width=20, height=2).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(frame_pilih_kamar, text="Edelweis \nRp.1.000.000", font=('Arial', 16), command=lambda: pilih_kamar('E'), width=20, height=2).grid(row=4, column=0, padx=5, pady=5)

    root.mainloop()

# Menampilkan dialog login
login()
