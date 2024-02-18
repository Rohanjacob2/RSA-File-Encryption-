import tkinter as tk #Import necessary modules from tkinter library
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedStyle
import rsa  #Import rsa library for cryptographic operations
import os
import shutil #Import shutil for file and directory operations
import random

#Function to generate RSA key pair (public and private keys)
def generate_rsa_key_pair(): 
    global publicKey, privateKey
    publicKey, privateKey = rsa.newkeys(1024)  #Generate 1024-bit RSA key pair

#Function to open a file using file dialog and return its path
def open_file(): 
    file_path = filedialog.askopenfilename()
    filename_label.config(text="Selected File: " + os.path.basename(file_path))
    return file_path

#Function to display a message using a messagebox
def show_message(message): 
    messagebox.showinfo("Status", message)

#Switches the visibility of the password in the entry widget
def toggle_password_visibility(): 
    current_show_state = password_entry.cget("show")
    if current_show_state == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

#Function to authenticate login based on a hardcoded password
def authenticate_login(): 
    entered_password = password_entry.get()

    if entered_password == "purushu":
        show_message("Login successful! You can now encrypt/decrypt files.")
        enable_file_operations()
    else:
        show_message("Incorrect password! Please try again.")

#Function to enable file operation buttons after successful login
def enable_file_operations(): 
    encrypt_button.config(state=tk.NORMAL)
    decrypt_button.config(state=tk.NORMAL)
    save_button.config(state=tk.NORMAL)
    verify_button.config(state=tk.NORMAL)
    sign_button.config(state=tk.NORMAL)
    shred_button.config(state=tk.NORMAL)
    logout_button.config(state=tk.NORMAL)
    text_box.config(state=tk.NORMAL)  

#Function to logout, clear entries, and disable file operation buttons
def logout(): 
    password_entry.delete(0, tk.END)
    disable_file_operations()
    text_box.config(state=tk.NORMAL) 
    text_box.delete("1.0", tk.END)  
    text_box.config(state=tk.DISABLED)  
    show_message("Logout successful! You can no longer encrypt/decrypt files.")

#Function to disable file operation buttons
def disable_file_operations(): 
    encrypt_button.config(state=tk.DISABLED)
    decrypt_button.config(state=tk.DISABLED)
    save_button.config(state=tk.DISABLED)
    verify_button.config(state=tk.DISABLED)
    sign_button.config(state=tk.DISABLED)
    shred_button.config(state=tk.DISABLED)
    logout_button.config(state=tk.DISABLED)
    text_box.config(state=tk.DISABLED)  

#Function to encrypt a file using RSA encryption
def encrypt_file(): 
    file_path = open_file()
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    encryptedList = []
    for i in range(0, len(plaintext), 117):
        chunk = plaintext[i:i+117]
        chunk_cipher = rsa.encrypt(chunk, publicKey)
        encryptedList.append(chunk_cipher)

    ciphertext = b''.join(encryptedList)

    with open(file_path, 'wb') as f:
        f.write(ciphertext)

    show_message(f"File encrypted successfully and saved as: {os.path.basename(file_path)}")

#Function to decrypt a file using RSA decryption
def decrypt_file(): 
    file_path = open_file()
    
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    decryptedList = []
    for i in range(0, len(ciphertext), 128):
        chunk = ciphertext[i:i+128]
        chunk_plain = rsa.decrypt(chunk, privateKey)
        decryptedList.append(chunk_plain)

    plaintext = b''.join(decryptedList)

    with open(file_path, 'wb') as f:
        f.write(plaintext)

    show_message(f"File decrypted successfully and saved as: {os.path.basename(file_path)}")

#Function to sign a file using RSA digital signature
def sign(): 
    global signature
    file_path = open_file()

    with open(file_path, "rb") as f:
        plaintext = f.read()

    signature = rsa.sign(plaintext, privateKey, 'SHA-512')

    with open('signature.txt', 'wb') as p:
        p.write(signature)

    show_message("File signed successfully!")

#Function to verify the digital signature of a file
def verify(): 
    file_path = open_file()

    with open(file_path, "rb") as f:
        plaintext = f.read()
    
    try:
        rsa.verify(plaintext, signature, publicKey)
        show_message("Signature is valid.")
    except Exception:
        show_message("Signature is invalid.")

#Function to save the content of a text box to a file
def save_file(): 
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_box.get("1.0", tk.END))

#Function to securely shred a file (overwrite with random data and delete)
def shred_file(): 
    file_path = open_file()

    with open(file_path, 'wb') as f:
        f.write(os.urandom(os.path.getsize(file_path)))

    os.remove(file_path)

    show_message(f"File shredded successfully: {os.path.basename(file_path)}")

#Create the main tkinter window
root = tk.Tk() 
root.title("Secure File Encryption")
root.config(bg="#f2f2f2")  

#Set the theme for ttk widgets
style = ThemedStyle(root) 
style.set_theme("vista")  

generate_rsa_key_pair() #Generate RSA key pair during program initialization

#UI title
label = ttk.Label(root, text="Secure File Encryption", font=("Segoe UI", 20), foreground="#3498db", background="#f2f2f2")
label.pack(pady=20)

#Create and pack widgets for the user interface
login_frame = ttk.Frame(root, padding=(5, 5, 5, 5)) 
login_frame.pack()

#Create a label for the password entry in the login frame
password_label = ttk.Label(login_frame, text="Enter Password:", font=("Segoe UI", 12), foreground="#3498db", background="#f2f2f2") 
password_label.pack(side=tk.LEFT, padx=5) 

#Create an entry widget for password input with characters
password_entry = ttk.Entry(login_frame, show="*") 
password_entry.pack(side=tk.LEFT, padx=5)

#Create a button to toggle password visibility 
toggle_password_button = ttk.Button(login_frame, text="👁", command=toggle_password_visibility, cursor="hand2", width=2) 
toggle_password_button.pack(side=tk.LEFT, padx=5) 

#Creates a login button with necessary style
login_button = ttk.Button(root, text="Login", command=authenticate_login, style="Rounded.TButton", cursor="hand2") 
login_button.pack(pady=10) 

#Create a frame for encrypt and decrypt buttons
encrypt_decrypt_frame = ttk.Frame(root, padding=(5, 5, 5, 5))
encrypt_decrypt_frame.pack()

#Makes an encrypt button with necessary style
encrypt_button = ttk.Button(encrypt_decrypt_frame, text="Encrypt File", command=encrypt_file, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
encrypt_button.pack(side=tk.LEFT, padx=2)

#Make a decrypt button with necessary style
decrypt_button = ttk.Button(encrypt_decrypt_frame, text="Decrypt File", command=decrypt_file, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED) 
decrypt_button.pack(side=tk.LEFT, padx=2) 

#Makes a frame for the buttons to sign, verify, and shred
sign_verify_shred_frame = ttk.Frame(root, padding=(5, 5, 5, 5))
sign_verify_shred_frame.pack()

#Sign button
sign_button = ttk.Button(sign_verify_shred_frame, text="Sign", command=sign, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
sign_button.pack(side=tk.LEFT, padx=2)

#Verify button
verify_button = ttk.Button(sign_verify_shred_frame, text="Verify", command=verify, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
verify_button.pack(side=tk.LEFT, padx=2)

#Shred button
shred_button = ttk.Button(sign_verify_shred_frame, text="Shred File", command=shred_file, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
shred_button.pack(side=tk.LEFT, padx=2)

#Create a label to display the selected file status
filename_label = ttk.Label(root, text="Selected File: None", font=("Segoe UI", 12), foreground="black", background="#D3D3D3") 
filename_label.pack(pady=10)

#Make a text box widget to display content
text_box = tk.Text(root, height=6, width=40, bg="#ecf0f1", fg="#2c3e50", font=("Segoe UI", 10), state=tk.DISABLED) 
text_box.pack(pady=10)

save_button = ttk.Button(root, text="Save Decrypted Content", command=save_file, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
save_button.pack(pady=10)

logout_button = ttk.Button(root, text="Logout", command=logout, style="Rounded.TButton", cursor="hand2", state=tk.DISABLED)
logout_button.pack(pady=10)

#Configure ttk button style
style.configure("Rounded.TButton", borderwidth=0, relief="flat", padding=10, font=("Segoe UI", 10)) 

root.mainloop() #Start the main loop for the tkinter window
