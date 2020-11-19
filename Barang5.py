# Menu informasi
def Show_menu():
    print("---------------------------------------")
    print("      Selamat Datang di Toko Kami      ")
    print("---------------------------------------")
    print("                 Menu                 ")
    print("[1] Baju")
    print("[2] Celana")
    print("[3] Help")
    print("[4] Exit")
    print()
    print("Silahkan memasukkan pilihan dengan angka 1 atau 2")
    print("Jika ingin melihat petunjuk, masukkan angka 3")
    print()
    menu = input("Silahkan masukkan pilihan Anda: ")

    while (int(menu) < 1) or (int(menu) > 4):
        print("Tidak terdaftar")
        print("Silahkan memasukkan pilihan dengan angka 1 atau 2")
        print("Jika ingin melihat petunjuk, masukkan angka 3")
        menu = input("Silahkan masukkan pilihan Anda: ")
    
    if menu == "1":
        Baju()
    elif menu == "2":
        Celana()
    elif menu == "3":
        Help()
    elif menu == "4":
        exit()

def Help():
    print()
    print("---------- Selamat datang di Toko Kami ----------")
    print("Silahkan memasukkan pilihan dengan angka 1 atau 2")
    print("Jika ingin melihat petunjuk, masukkan angka 3")
    print("Jika ingin keluar, masukkan angka 4")
    print("Rating barang dalam rentang 1 hingga 10")
    print()
    kembali = input("Silahkan mengisi '0' untuk kembali: ")
    while kembali != "0":
        print("Kode salah, silahkan ulangi")
        kembali = input("Silahkan mengisi '0' untuk kembali: ")
    if kembali:
        print()
        Show_menu()

def Baju():
    beli1 = 0
    rate1 = 0 
    jumlah1 = 0
    stok1 = 99
    print("Baju")
    print("Harga: Rp250000")
    print("Stok barang: " + str(stok1))
    print("Barang yang sudah terbeli: " + str(beli1))
    print("Rating: " + str(rate1) + " dari " + str(jumlah1) + " pengguna")
    beli1 = int(input("Banyaknya baju yang ingin dibeli: "))
    total_harga = beli1 * 250000
    print("Total harga: Rp" + str(total_harga))
    rate1 += int(input("Masukkan rating: "))
    jumlah1 += 1
    stok1 = stok1 - beli1
    beli1 += beli1
    print("Rating: " + str(rate1) + " dari " + str(jumlah1) + " pengguna")
    print("Stok: " + str(stok1))
    print("Barang yang sudah terbeli: " + str(beli1))
    print("Terima kasih sudah berbelanja dengan kami")
    print()
    kembali = input("Silahkan mengisi '0' untuk kembali ke menu: ")
    while kembali != "0":
        print("Kode salah, silahkan ulangi")
        kembali = input("Silahkan mengisi '0' untuk kembali ke menu: ")
    if kembali:
        Show_menu()
    
def Celana():
    beli2 = 0
    rate2 = 0 
    jumlah2 = 0
    stok2 = 99
    print("Celana")
    print("Harga: Rp250000")
    print("Stok barang: " + str(stok2))
    print("Barang yang sudah terbeli: " + str(beli2))
    print("Rating: " + str(rate2) + " dari " + str(jumlah2) + " pengguna")
    beli2 = int(input("Banyaknya celana yang ingin dibeli: "))
    total_harga = beli2 * 250000
    print("Total harga: Rp" + str(total_harga))
    rate2 += int(input("Masukkan rating: "))
    jumlah2 += 1
    stok2 = stok2 - beli2
    beli2 += beli2
    print("Rating: " + str(rate2) + " dari " + str(jumlah2) + " pengguna")
    print("Stok: " + str(stok2))
    print("Barang yang sudah terbeli: " + str(beli2))
    print("Terima kasih sudah berbelanja dengan kami")
    print()
    kembali = input("Silahkan mengisi '0' untuk kembali ke menu: ")
    while kembali != "0":
        print("Kode salah, silahkan ulangi")
        kembali = input("Silahkan mengisi '0' untuk kembali ke menu: ")
    if kembali:
        Show_menu()

Show_menu()