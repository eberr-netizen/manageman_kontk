"Program Manajemen Kontak"


kontak1 = {'nama': "Andi", 'HP': '109989303', 'email': 'Andi@pyhton.com'}
kontak2 = {'nama': "Ani", 'HP': '165461258', 'email': 'Ani@pyhton.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print ("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input ("Masukan Pilihan Menu Kontak (1,2,3,dan 4): ")

    if pilihan == '1':
        #Melihat Semu Kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item ["nama"]}({item ["HP"]}, {item ["email"]})')
        else:
            print("Kontak masih kosong!")

    elif pilihan == '2':
        #Menambahkan Kontak
        nama = input("Masukan Nama Kontak yang Baru: ")
        HP =input("Masukan Nomor HP Kontak yang Baru: ")
        email =input("Masukan Email Kontak yang Baru: ")
        kontak_baru = {'nama':nama, 'HP':HP, 'email': email}
        kontak.append(kontak_baru)
        print("Kontak Baru Berhasil ditambahkan!")

    elif pilihan == '3':
        #Menghapus Kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]}({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong!")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus")

    elif pilihan == '4':
        #keluar dari kontak
        break

    else:
        print("Anda memasukkan pilihan yang salah!")





