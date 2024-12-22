#1
# hobbies = ["main bola", "berenang", "ngoding", "k", "sugs", "hdi", "jooo", "jojoo"]
# tmp_hobbies = hobbies

# print(hobbies[len(hobbies) - 3])

#2
# print(f"hobbies -> {hobbies}")

# tmp_hobbies[1] = "biliard"

# print(f"tmp_hobbies -> {tmp_hobbies}")


# goa_kosong = ['|_|', '|_|', '|_|', '|_|']
# print("  ".join(goa_kosong))

# while True:
#     try:
#         pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] Masukkan pilihan: "))
#         break  # Keluar dari loop jika input berhasil diubah menjadi integer
#     except ValueError:
#         print("Input yang kamu masukkan salah. Silakan coba lagi.")


#START
# import random

# welcome_message = "WELCOME TO CUYPY GAMES!"
# cuypy_position = random.randint(1, 4)

# print("*****************************")
# print(f"** {welcome_message} **")
# print("*****************************")

# nama_user = input("masukan nama kamu: ")

# bentuk_goa = "|_|"
# goa_kosong = [bentuk_goa] * 4 # INI TETEP HARUS KOSONG

# goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
# goa[cuypy_position - 1] = "|0_0|"

# while True:
#     print(f'''
#     Halo {nama_user}! Coba perhatikan goa dibawah ini  
#     {goa_kosong}
#     ''')

#     pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

#     confirm_answer = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")

#     if confirm_answer == "n":
#         print("program dihentikan!")
#         exit()
#     elif confirm_answer == "y":
#         if pilihan_user == cuypy_position:
#             print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
#         else:
#             print(f"\n{goa}\n\nUncchhh kamu kalah 🙊")
#     else:
#         print("Silahkan ulangi programnya!")
#         exit()

#         play_again = input("\n\napakah ingin melanjutkan gamenya lagi? [y/n]")
#         if play_again == "n":
#             break



# import tkinter as tk
# from tkinter import ttk

# class Calculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Kalkulator")
#         self.root.geometry("300x400")
#         self.root.resizable(False, False)
        
#         self.expression = ""
#         self.result_var = tk.StringVar()
        
#         self.create_widgets()
    
#     def create_widgets(self):
#         # Entry widget untuk menampilkan ekspresi dan hasil
#         entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), justify='right')
#         entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
#         # Membuat tombol-tombol
#         buttons = [
#             '7', '8', '9', '/',
#             '4', '5', '6', '*',
#             '1', '2', '3', '-',
#             '0', '.', '=', '+'
#         ]
        
#         for i, btn in enumerate(buttons):
#             action = lambda x=btn: self.on_button_click(x)
#             b = ttk.Button(self.root, text=btn, command=action)
#             b.grid(row=(i//4)+1, column=i%4, sticky="nsew")
        
#         # Tombol Clear (C)
#         clear_button = ttk.Button(self.root, text='C', command=self.clear)
#         clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")
        
#         # Konfigurasi grid
#         for i in range(6):
#             self.root.grid_rowconfigure(i, weight=1)
#         for i in range(4):
#             self.root.grid_columnconfigure(i, weight=1)
    
#     def on_button_click(self, char):
#         if char == '=':
#             try:
#                 self.expression = str(eval(self.expression))
#             except Exception as e:
#                 self.expression = "Error"
#         else:
#             self.expression += str(char)
#         self.result_var.set(self.expression)
    
#     def clear(self):
#         self.expression = ""
#         self.result_var.set("")

# if __name__ == "__main__":
#     root = tk.Tk()
#     calc = Calculator(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk
import numpy as np

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.root.geometry("600x400")
        
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for Matrix A
        self.matrix_a_label = ttk.Label(self.root, text="Matrix A:")
        self.matrix_a_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.matrix_a_entries = self.create_matrix_entries(1, 0)
        
        # Labels and Entries for Matrix B
        self.matrix_b_label = ttk.Label(self.root, text="Matrix B:")
        self.matrix_b_label.grid(row=0, column=1, padx=10, pady=10)
        
        self.matrix_b_entries = self.create_matrix_entries(1, 1)
        
        # Buttons for operations
        self.add_button = ttk.Button(self.root, text="Add", command=self.add_matrices)
        self.add_button.grid(row=6, column=0, pady=10)
        
        self.multiply_button = ttk.Button(self.root, text="Multiply", command=self.multiply_matrices)
        self.multiply_button.grid(row=6, column=1, pady=10)
        
        # Label and Entry for Result
        self.result_label = ttk.Label(self.root, text="Result:")
        self.result_label.grid(row=7, column=0, padx=10, pady=10, columnspan=2)
        
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    
    def create_matrix_entries(self, start_row, column):
        entries = []
        for i in range(4):
            row_entries = []
            for j in range(4):
                entry = ttk.Entry(self.root, width=5)
                entry.grid(row=start_row + i, column=column, padx=5, pady=5)
                row_entries.append(entry)
            entries.append(row_entries)
        return entries

    def get_matrix_from_entries(self, entries):
        matrix = []
        for row_entries in entries:
            row = []
            for entry in row_entries:
                value = entry.get()
                row.append(float(value) if value else 0)
            matrix.append(row)
        return np.array(matrix)
    
    def add_matrices(self):
        matrix_a = self.get_matrix_from_entries(self.matrix_a_entries)
        matrix_b = self.get_matrix_from_entries(self.matrix_b_entries)
        result = matrix_a + matrix_b
        self.display_result(result)
    
    def multiply_matrices(self):
        matrix_a = self.get_matrix_from_entries(self.matrix_a_entries)
        matrix_b = self.get_matrix_from_entries(self.matrix_b_entries)
        result = np.dot(matrix_a, matrix_b)
        self.display_result(result)
    
    def display_result(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()

