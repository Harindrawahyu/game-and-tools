# FUNCTION
import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_massage():
    style = "*" * (len(PC_NAME) + 14)
    
    print(style)
    print(f"** WELCOME {PC_NAME} **")
    print(style)
    
def exit_program():
    print('Program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2..')
    sleep(1)
    print('1..') 
    sleep(1)
    print('Program berhasil dihentikan')
    print("\nTerima kasih telah menggunakan program ini 👋")
    
if __name__ == '__main__':
    welcome_massage()
    exit_program()
