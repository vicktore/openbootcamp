from tkinter import *

root = Tk()
elemento = StringVar()
list_box = Listbox(root)

list_element = ["rojo", "azul", "verde", "blanco"]

for item in list_element:
    list_box.insert(END, item)


list_box.pack()
label = Label(text="Lista de colores")
label.pack()

root.mainloop()
