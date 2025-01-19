from tkinter import *
import customtkinter
from customtkinter import CTkOptionMenu

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("700x450")


def color_picker(choice):
    my_label.configure(text=choice, text_color=choice)


def color_picker2():
    my_label.configure(text=my_option.get(), text_color=my_option.get())


colors = ["Red", "Green", "Blue"]

my_option: CTkOptionMenu = customtkinter.CTkOptionMenu(root, values=colors)  # command=color_picker)
my_option.pack(pady=40)

my_label = customtkinter.CTkLabel(root, text="", )
my_label.pack(pady=10)

pick_button = customtkinter.CTkButton(root, text="Make Choice", command=color_picker2())
pick_button.pack(pady=30)

root.mainloop()
