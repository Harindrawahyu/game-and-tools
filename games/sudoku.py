import main

def start():
    print("[COMING SOON]")
    
    
    kembali = input("\nMau kembali? [y/n]: ")
    if kembali == "y": 
        main.menu()
    elif kembali == "n":
        start()
        
        
        
if __name__ == '__main__':
    start()