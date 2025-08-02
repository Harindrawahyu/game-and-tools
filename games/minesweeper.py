# import main
from tkinter import *

def start():
    print("===============================================")
    print("          SELAMAT DATANG DI GAME MINESWEEPER 💣 ")
    print("==============================================\n")
    
    # minesweeper
    root = Tk()
    root.configure(bg="black")
    root.geometry('800x500')
    root.title("Minesweeper 💣")
    root.resizable(False, False)
    
    top_frame = Frame(
        root,
        bg='red',
        width=800,
        height=80
    )
    top_frame.place(x=0, y=0)
    
    left_frame = Frame(
        root,
        bg='blue',
        width=100,
        height=420
)
    left_frame.place(x=0, y=80)

    root.mainloop()
    
    
    
    
    
    
    
    
    # kembali = input("\nMau kembali? [y/n]: ")
    # if kembali == "y": 
    #     main.menu()
    # elif kembali == "n":
    #     start()
        
        
        
if __name__ == '__main__':
    start()