"Program Manajemen Kontak"

class kontak:
    def __init__(self):
        self.kontak = []


    def melihat_kontak(self):
        # Melihat Semu Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["nama"]}({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukan Nama Kontak yang Baru: ")
        HP = input("Masukan Nomor HP Kontak yang Baru: ")
        email = input("Masukan Email Kontak yang Baru: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak Baru Berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1 :
            return
        else:
            i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah dihapus")
kontak_kantor = kontak()
kontak_keluarga = kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print ("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input ("Masukan Pilihan Menu Kontak (1,2,3,dan 4): ")

    if pilihan == '1':
        kontak_keluarga.melihat_kontak()

    elif pilihan == '2':
        kontak_keluarga.menambah_kontak()

    elif pilihan == '3':
        kontak_keluarga.menghapus_kontak()

    elif pilihan == '4':
        #keluar dari kontak
        break

    else:
        print("Anda memasukkan pilihan yang salah!")





