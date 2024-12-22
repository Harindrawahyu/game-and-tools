

def start():
    print("SELAMAT DATANG DI CAESAR CHIPER")
    def caesar_cipher(text, shift, mode='encrypt'):
        result = ""
        
        # Adjust shift for decryption
        if mode == 'decrypt':
            shift = -shift

        for char in text:
            # Encrypt/Decrypt uppercase letters
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Encrypt/Decrypt lowercase letters
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                # Non-alphabetic characters are added unchanged
                result += char

        return result

    # Example usage
    if __name__ == "__main__":
        # Get user input for the message
        message = input("Enter the message: ")
        shift_value = int(input("Enter the shift value (integer): "))
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

        # Validate mode input
        if mode not in ['enc', 'dec']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        else:
            # Perform encryption or decryption
            result_message = caesar_cipher(message, shift_value, mode)
            print(f"Result: {result_message}")
            
        
if __name__ == '__main__':
    start()
