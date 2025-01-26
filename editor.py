from customtkinter import *
from tkinter.filedialog import *
from tkinter import *
import subprocess

compiler = Tk()
compiler.title("Editor de código")
path_file = ''

def set_path_file(path):
    global path_file
    path_file = path

def run():
    command = f'python {path_file}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


def guardar():
    path = asksaveasfile(filetypes=(("mrcmt", "*.mrcmt"), ), )
    with open(path, "w") as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_path_file(path)

def abrir():
    path = askopenfilename(filetypes=(("mrcmt", "*.mrcmt"), ), )
    with open(path, "r") as file: # w(write) r(read)
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_path_file(path)

def imprime():
    editor.insert(END,"IMPRIME")

def condicional(): 
    editor.insert(END,"SI")

def condicional_siono():
    editor.insert(END,"SINO")

def condicional_ninguno():
    editor.insert(END,"SININGUNO")

def valor_entero():
    editor.insert(END,"ENTERO")

def contar():
    editor.insert(END,"CUENTA")

def titulo():
    editor.insert(END,"TITULO")

def potencia():
    editor.insert(END,("POTENCIA"))

def raiz():
    editor.insert(END, "RAIZQ()")

menu = Menu(compiler)

file_bar = Menu(menu, tearoff=0)
file_bar.add_command(label="Abrir", command=abrir)
file_bar.add_command(label="Guardar como", command=guardar)
menu.add_cascade(label="Archivo", menu=file_bar)

ini_bar = Menu(menu, tearoff=0)
ini_bar.add_command(label="Iniciar", command=run)
menu.add_cascade(label="Iniciar", menu=ini_bar)

func_bar = Menu(menu, tearoff=0)
func_bar.add_command(label="Imprimir", command=imprime)
func_bar.add_command(label="Condicional", command=condicional)
func_bar.add_command(label="Condicional o si no", command=condicional_siono)
func_bar.add_command(label="Condicional si no pasa ninguno de los dos", command=condicional_ninguno)
func_bar.add_command(label="Valor entero", command=valor_entero)
func_bar.add_command(label="Contar", command=contar)
func_bar.add_command(label="Titulo", command=titulo)
func_bar.add_command(label="Potencia", command=potencia)
func_bar.add_command(label="Raiz cuadrada", command=raiz)

menu.add_cascade(label="Funciones", menu=func_bar)
compiler.config(menu=menu)

editor = Text(height=40, width=1000)
editor.pack()

code_output = Text(height=8, width=1000)
code_output.pack()

compiler.mainloop()