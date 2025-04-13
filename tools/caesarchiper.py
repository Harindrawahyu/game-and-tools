import main
from utils.helper import clear_screen

clear_screen()


def enkripsi_caesar(teks, shift):
        hasil = ""
        for char in teks:
            if char.isalpha():
                geser = ord('A') if char.isupper() else ord('a')
                hasil += chr((ord(char) - geser + shift) % 26 + geser)
            else:
                hasil += char  # biarkan karakter non-huruf tetap
        return hasil
    
def dekripsi_caesar(teks, shift):
        return enkripsi_caesar(teks, -shift)

def start():
    print("======================================")
    print("     SELAMAT DATANG DI CAESAR CHIPER ")
    print("======================================\n")

    while True:
        print("Menu:")
        print("1. Enkripsi Pesan")
        print("2. Dekripsi Pesan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            pesan = input("Masukkan pesan yang ingin dienkripsi: ")
            try:
                shift = int(input("Masukkan nilai shift (angka): "))
            except ValueError:
                print("Shift harus berupa angka!\n")
                continue
            hasil = enkripsi_caesar(pesan, shift)
            print("Hasil Enkripsi:", hasil)
            print()
        
        elif pilihan == '2':
            pesan = input("Masukkan pesan yang ingin didekripsi: ")
            try:
                shift = int(input("Masukkan nilai shift (angka): "))
            except ValueError:
                print("Shift harus berupa angka!\n")
                continue
            hasil = dekripsi_caesar(pesan, shift)
            print("Hasil Dekripsi:", hasil)
            print()
        
        elif pilihan == '3':
#Opsi keluar 
            kembali = input("\nIngin kembali ke menu? [y/n]: ")
            if kembali == "y": 
                main.menu()
            elif kembali == "n":
                start()
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.\n")
    

if __name__ == '__main__':
    start()
