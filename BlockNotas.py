from tkinter import *
from tkinter import filedialog as f
from io import open

title = " Editor | Python - Tkinter"
root = Tk()
root.title(title)

# url de archivo
url_file = ""

#funciones
def new_file():
    global url_file
    text.delete(1.0,"end")
    url_file= ""
    url_file ="nuevo archivo"
    root.title(url_file + title)

def open_file():
    global url_file
    url_file = f.askopenfilename(initialdir = '.' , filetype =(("archivos de texto", "*.txt"),), title = "Abrir archivo")
    
    if url_file != "":
        file = open(url_file, 'r')
        content = file.read()
        text.delete(1.0, "end")
        text.insert('insert', content)
        file.close()
        root.title(url_file + title)

def save_file():
    global url_file
    if url_file != "":
        content = text.get (1.0, "end-ic")
        file = open(url_file, 'w+')
        file.write(content)
        root.title("archivo guardado" + url_file + title)
        file.close()
    else:
        file = f.asksaveasfile(title="Save_file", node='w', defaultextension=".txt")
        if file is not None:
            url_file = file.name
            content = text.get(1.0, "end-1c")
            file = open(url_file, 'w+')
            file.write(content)
            root.title("Archivo guardado"+ url_file + title)
            file.close()
        else:
            url_file =""
            root.title("Guardado cancelado" + url_file + title )
#menu
barra = Menu (root)
file_menu = Menu(barra, tearoff=0)
file_menu.add_command(label= "nuevo archivo", command = new_file)
file_menu.add_separator()
file_menu.add_command(label= "abrir archivo", command = open_file)
file_menu.add_separator()
file_menu.add_command(label= "guardar archivo", command = save_file)
file_menu.add_separator()
file_menu.add_command(label= "salir", command = root.quit)

barra.add_cascade(menu= file_menu, label = "archivo")

# caja de texto
text = Text (root)
text.pack(fill = "both", expand =1)
text.config(bd=0, padx=6 , pady=5 , font=("Ariel",16))

root.config(menu=barra)
root.mainloop()