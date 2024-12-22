from libs import welcome_massage, exit_program
from games import cuypy, sudoku
from tools import kalkulator, caesarchiper

def menu():
    user_option = int(input(f'\nMenu Program:\n1. Game Cuypy\n2. Game Sudoku(unfishied)\n3. Kalkulator\n4. CaesarChiper\n5. Keluar Program\n\nSilahkan pilih menu: '))
    
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        sudoku.start()
    elif user_option == 3:
        kalkulator.start()
    elif user_option == 4:
        caesarchiper.start()
    elif user_option == 5:
        exit_program()
    else:
        input('Hanya boleh pilih yang ada di menu: ')
    
def main():
    welcome_massage()
    menu()
    
if __name__ == '__main__':
    main()