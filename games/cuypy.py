import random
import main
from utils.helper import clear_screen

clear_screen()
# Pilihan goa
def start():
    print("===================================")
    print("         TEMUKAN CUYPY 🦝")
    print("===================================\n")
    
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        
        cuypy_position = random.randint(1, 4)
        goa = goa_kosong.copy()
        goa[cuypy_position - 1] = "|0_0|"
        
        print("Coba perhatikan goa di bawah ini:\n")
        print(' '.join(goa_kosong))  # tampilkan goa kosong
        
        try:
            pilihan_user = int(input("\nMenurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
            if pilihan_user < 1 or pilihan_user > 4:
                raise ValueError
        except ValueError:
            print("Pilihan harus angka antara 1 sampai 4!\n")
            continue

        print("\n" + ' '.join(goa) + "\n")

        if pilihan_user == cuypy_position:
            print(f"🎉 SELAMAT! Kamu menemukan CUYPY! Dia berada di goa nomor {cuypy_position}.\n")
        else:
            print(f"😿 CUYPY TIDAK ADA DISITU! Dia berada di goa nomor {cuypy_position}.\n")

        main_lagi = input("Coba lagi? [y/n]: ").lower()
        if main_lagi == "n":
            main.menu()  # balik ke menu utama
            break
        elif main_lagi != "y":
            print("Input tidak dikenali. Keluar dari permainan.")
            break

if __name__ == '__main__':
    start()

