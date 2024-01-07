import tkinter as tk
from tkinter import messagebox, simpledialog
from RSA import generate_key_pair, encrypt, decrypt



#Current Issues: 
#       Need to be able to import a file, instead of having to type out the message
#       Need to be able to save the keys to a file
#           Maybe try saving the keys separately, as "PublicKey.txt" and "PrivateKey.txt"


class RSA_App:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption Program")

        self.generate_keys_button = tk.Button(root, text="Generate Key Pair", command=self.generate_keys_callback)
        self.generate_keys_button.pack(pady=10)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_callback)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(root,text="Decrypt", command=self.decrypt_callback)
        self.decrypt_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)


    def generate_keys_callback(self):
        public_key, private_key,modulus = generate_key_pair()
        keys_info = f"Public Key: {public_key}\nPrivate Key: {private_key}"
        messagebox.showinfo("Generated Keys", keys_info)

    def encrypt_callback(self):
        message = simpledialog.askstring("Input", "Enter the message to encrypt:")
        public_key = simpledialog.askstring("Input", "Enter the recipient's public key:")
        encrypted_message = encrypt(message, public_key)
        messagebox.showinfo("Encryption Result", f"Encrypted Message: {encrypted_message}")

    def decrypt_callback(self):
        encrypted_message = simpledialog.askstring("Input", "Enter the encrypted message:")
        private_key = simpledialog.askstring("Input", "Enter your private key:")
        decrypted_message = decrypt(encrypted_message, private_key)
        messagebox.showinfo("Decryption Result", f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RSA_App(root)
    root.mainloop()