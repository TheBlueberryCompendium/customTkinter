from tkinter import *
import customtkinter
from PIL import Image
root = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

my_image=customtkinter.CTkImage(light_image=Image.open('blueberries.png'), size=(600,337.5))

my_label = customtkinter.CTkLabel(master=root, text="", image=my_image)
my_label.place(x=0, y=0)

root.geometry("600x337.5")
def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=(250, 100), fill="both")

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 23))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)  # Place to add logic
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10, )

root.mainloop()
