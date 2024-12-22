import random
import main

# Pilihan goa
def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        
        cuypy_position = random.randint(1, 4)
        goa = goa_kosong.copy()
        goa[cuypy_position - 1] = "|0_0|"
        
        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        
        print(f'Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n')
        
        pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] Masukkan pilihan: "))
                
        if pilihan_user == cuypy_position:
            print(f"\n{goa}\n\nSELAMAT! Kamu menemukan CUYPY! Cuypy berada di goa nomor {cuypy_position}.")
        else:
            print(f"\n{goa}\n\nCUYPY TIDAK ADA DISITU! Dia berada di goa nomor {cuypy_position}.")       
                
        main_lagi= input("\nCoba Lagi? [yes/no]: ")
        if main_lagi == "no": 
            main.menu()
        elif main_lagi == "yes":
            start()

if __name__ == '__main__':
    start()

