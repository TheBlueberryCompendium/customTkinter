from tkinter import *
import customtkinter
from PIL import Image

root = customtkinter.CTk()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


my_image=customtkinter.CTkImage(light_image=Image.open('blueberries.png'), size=(1200,675))

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)

root.mainloop()
