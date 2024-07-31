print("NAMA : Kurniawan")
print("NIM  : 20230801054")
print("TUGAS: UAS BAHASA PEMROGRAMAN ")
print("TANGGAL: 29 JULI 2024")
print()

class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"

def tampilkan_barang(barang_list):
    if not barang_list:
        print("Tidak ada barang yang tersedia.")
    else:
        for idx, barang in enumerate(barang_list):
            print(f"{idx + 1}. {barang}")

def tambah_barang(barang_list):
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    print()
    barang_list.append(Barang(nama, harga, stok))

def hapus_barang(barang_list):
    tampilkan_barang(barang_list)
    idx = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
    if 0 <= idx < len(barang_list):
        barang_list.pop(idx)
        print("Barang berhasil dihapus.")
    else:
        print("Nomor barang tidak valid.")

def cari_barang(barang_list):
    nama = input("Masukkan nama barang yang dicari: ")
    for barang in barang_list:
        if barang.nama.lower() == nama.lower():
            print(barang)
            return
    print("Barang tidak ditemukan.")

def hitung_pembelian(barang_list):
    tampilkan_barang(barang_list)
    idx = int(input("Masukkan nomor barang yang ingin dibeli: ")) - 1
    if 0 <= idx < len(barang_list):
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        barang = barang_list[idx]
        if jumlah <= barang.stok:
            total_harga = jumlah * barang.harga
            barang.stok -= jumlah
            print(f"Total harga: {total_harga}")
            print(f"Sisa stok {barang.nama}: {barang.stok}")
        else:
            print("Stok tidak cukup.")
    else:
        print("Nomor barang tidak valid.")

def menu():
    print("Menu:")
    print("1. Tampilkan Barang")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("5. Hitung Pembelian")
    print("6. Keluar")
    print()
    pilihan = int(input("Masukkan pilihan (1-6): "))
    print()
    return pilihan

def main():
    barang_list = []
    while True:
        pilihan = menu()
        if pilihan == 1:
            tampilkan_barang(barang_list)
        elif pilihan == 2:
            tambah_barang(barang_list)
        elif pilihan == 3:
            hapus_barang(barang_list)
        elif pilihan == 4:
            cari_barang(barang_list)
        elif pilihan == 5:
            hitung_pembelian(barang_list)
        elif pilihan == 6:
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi")

if __name__ == "__main__":
    main()