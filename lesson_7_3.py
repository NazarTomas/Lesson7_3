# def ceaser_cipher(text, shift):
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             shift_base = ord("A") if char.isupper() else ord('a')
#             encrypted_text += chr((ord(char)- shift_base+ shift)%26+shift_base)
#         else:
#             encrypted_text+=char
#     return encrypted_text

# text = input("Введіть текст для шифрування: ")
# shift = 3
# encrypted = ceaser_cipher(text, shift)
# print("Зашифрований текст:", encrypted)

import tkinter as tk

def ceaser_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount =  shift % 26
            if char.isupper():
                new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text():
    text = input_text.get()
    shift = int(shift_entry.get())
    result_text.set(ceaser_cipher(text, shift))

def decrypt_text():
    text = input_text.get()
    shift = int(shift_entry.get())
    decrypted_text = ceaser_cipher(text, shift, decrypt=True)
    result_text.set(decrypted_text)

root = tk.Tk()
root.title("Шифратор Цезаря")
root.geometry("500x400")
tk.Label(root, text="Введіть текст:").pack()
input_text = tk.Entry(root)
input_text.pack()

tk.Label(root, text="Введітьь ключ:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

tk.Button(root, text="Зашифрувати", command=encrypt_text).pack()
tk.Button(root, text="Розшифрувати", command=decrypt_text).pack()

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack()
root.mainloop()