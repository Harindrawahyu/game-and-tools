from libs import welcome_massage, exit_program
from games import cuypy, minesweeper
from tools import kalkulator, caesarchiper
from utils.helper import clear_screen

clear_screen()

def menu():
    while True:
        try:
            print("\n===== MENU PROGRAM =====")
            print("1. Game Cuypy")
            print("2. Game Minesweeper (unfinished)")
            print("3. Kalkulator")
            print("4. Caesar Chiper")
            print("5. Keluar Program")

            user_option = int(input("\nSilahkan pilih menu [1-5]: "))
    
            if user_option == 1:
                cuypy.start()
            elif user_option == 2:
                minesweeper.start()
            elif user_option == 3:
                kalkulator.start()
            elif user_option == 4:
                caesarchiper.start()
            elif user_option == 5:
                exit_program()
                break
            else:
                print("⚠️ Pilihan tidak tersedia. Masukkan angka dari 1 sampai 5.\n")
        except ValueError:
            print("❌ Input tidak valid! Harus berupa angka.\n")
    
def main():
    welcome_massage()
    menu()
    
if __name__ == '__main__':
    main()