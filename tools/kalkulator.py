import tkinter as tk
from tkinter import ttk
import main
from utils.helper import clear_screen

clear_screen()



class Calculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Kalkulator")
            self.root.geometry("300x400")
            self.root.resizable(False, False)
            
            self.expression = ""
            self.result_var = tk.StringVar()
            
            self.create_widgets()
        
        def create_widgets(self):
            # Entry widget untuk menampilkan ekspresi dan hasil
            entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), justify='right')
            entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
            
            # Membuat tombol-tombol
            buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+'
            ]
            
            for i, btn in enumerate(buttons):
                action = lambda x=btn: self.on_button_click(x)
                b = ttk.Button(self.root, text=btn, command=action)
                b.grid(row=(i//4)+1, column=i%4, sticky="nsew")
            
            # Tombol Clear (C)
            clear_button = ttk.Button(self.root, text='C', command=self.clear)
            clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")
            
            # Konfigurasi grid
            for i in range(6):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(4):
                self.root.grid_columnconfigure(i, weight=1)
        
        def on_button_click(self, char):
            if char == '=':
                try:
                    self.expression = str(eval(self.expression))
                except Exception as e:
                    self.expression = "Error"
            else:
                self.expression += str(char)
            self.result_var.set(self.expression)
        
        def clear(self):
            self.expression = ""
            self.result_var.set("")

def start():
    print("======================================")
    print("     SELAMAT DATANG DI KALKULATOR     ")
    print("======================================\n")
        
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

    kembali = input("\nUdahan ngitungnya? Ingin kembali ke menu? [y/n]: ")
    if kembali == "y": 
        main.menu()
    elif kembali == "n":
        start()
        
if __name__ == '__main__':
    start()
