print("NAMA : Kurniawan")
print("NIM  : 20230801054")
print("TUGAS: UAS BAHASA PEMROGRAMAN ")
print("TANGGAL: 29 JULI 2024")
print()

import math

def menu():
    print()
    print("Pilih Bangun Datar:")
    print("1. Segi Empat")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")
    print()
    pilihan = int(input("Masukkan pilihan (1-5): "))
    print()
    return pilihan

def hitung_segi_empat():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitung_segitiga():
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi_a = float(input("Masukkan panjang sisi a: "))
    sisi_b = float(input("Masukkan panjang sisi b: "))
    sisi_c = float(input("Masukkan panjang sisi c: "))
    luas = 0.5 * alas * tinggi
    keliling = sisi_a + sisi_b + sisi_c
    return luas, keliling

def hitung_lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari
    return luas, keliling

def main():
    while True:
        pilihan = menu()
        if pilihan == 1:
            luas, keliling = hitung_segi_empat()
            nama = "Segi Empat"
        elif pilihan == 2:
            luas, keliling = hitung_persegi_panjang()
            nama = "Persegi Panjang"
        elif pilihan == 3:
            luas, keliling = hitung_segitiga()
            nama = "Segitiga"
        elif pilihan == 4:
            luas, keliling = hitung_lingkaran()
            nama = "Lingkaran"
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid, silakan pilih kembali")
            continue

        print(f"Nama Bangun Datar: {nama}")
        print(f"Luas: {luas}")
        print(f"Keliling: {keliling}")

if __name__ == "__main__":
    main()
