from os import popen, system, remove
from sys import exit
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename


user_win = str(popen("echo %USERNAME%").read()).replace("\n", "") # Lee el nombre del usuario de Windows para acceder a la carpeta.
vent = Tk()
vent.title("Lenguaje")


python_check = popen("python --version") 
if str(python_check).startswith("\"python\""):
    showwarning("El programa requiere tener Python instalado.", "Instale buscando la web oficial.") 
    vent.destroy()
    exit() # Si no se tiene Python instalado no funcionará. Añadir carpeta con dependencias.

def traduction(archive=("C:/Users/{}/Documents/mrcmt.mrcmt".format(str(user_win)))):
    archive_open = open(archive, "r")
    content = archive_open.read()
    archive_open.close()
    # Reemplazando código del interpretado a Python, incluyendo las palabras reservadas.
    content = content.replace("ABSOLUTO", "abs")
    content = content.replace("ACABACON", "endswith")
    content = content.replace("ABRE", "open")
    content = content.replace("AÑADE", "append")
    content = content.replace("BUSCA", "find")
    content = content.replace("BUSCARD", "rfind")
    content = content.replace("CADENA", "str")
    content = content.replace("CAP", "capitalize")
    content = content.replace("CENTRA", "center")
    content = content.replace("CLASE", "class")
    content = content.replace("CONSIGUE", "get")
    content = content.replace("CONTAR", "count")
    content = content.replace("CONTINUA", "continue")
    content = content.replace("COS", "cos")
    content = content.replace("CREADICCIONARIO", "fromkeys")
    content = content.replace("CUENTA", "count")
    content = content.replace("DEF_FUNCION", "def")
    content = content.replace("DESDE", "from")
    content = content.replace("DEVUELVE", "return")
    content = content.replace("DICCIONARIO", "dict")
    content = content.replace("EJECUTAR", "exec")
    content = content.replace("ELIMINA_LISTA", "remove")
    content = content.replace("ELIMINARX", "del")
    content = content.replace("ELECCIONRAN", "choice")
    content = content.replace("EMPIEZACON", "startswith")
    content = content.replace("EN", "in")
    content = content.replace("ENTERO", "int")
    content = content.replace("ESTABLECER_DEFECTO", "setdefault")
    content = content.replace("EVALUA", "eval")
    content = content.replace("EXCEPTO", "except")
    content = content.replace("FINALMENTE", "finally")
    content = content.replace("GRADOSR", "radians")
    content = content.replace("IMPORTAR", "import")
    content = content.replace("IMPRIMIR", "print")
    content = content.replace("INSERTA", "insert")
    content = content.replace("INTENTA", "try")
    content = content.replace("JUNTA", "joint")
    content = content.replace("LISTA", "list")
    content = content.replace("LOGARITMO", "log")
    content = content.replace("LONGITUD", "len")
    content = content.replace("MAYUS", "upper")
    content = content.replace("MAYUSXMINUS", "swapcase")
    content = content.replace("MEZCLA", "shuffle")
    content = content.replace("MIENTRAS", "while")
    content = content.replace("MINUS", "lower")
    content = content.replace("NO", "not")
    content = content.replace("ORDENA", "sort")
    content = content.replace("OR", "or")
    content = content.replace("PARTE", "break")
    content = content.replace("PARTIRD", "rstrip")
    content = content.replace("PARTIRI", "lstrip")
    content = content.replace("PASA", "pass")
    content = content.replace("POTENCIA", "pow")
    content = content.replace("POR", "for")
    content = content.replace("RAIZQ", "sqrt")
    content = content.replace("RANGO", "randrange")
    content = content.replace("RELL0", "zfill")
    content = content.replace("RELLENAD", "ljust")
    content = content.replace("REDONDEA", "round")
    content = content.replace("REVERTIR", "reverse")
    content = content.replace("SEPARA", "split")
    content = content.replace("SEPARALINEA", "splitlines")
    content = content.replace("SEN", "sin")
    content = content.replace("SI", "if")
    content = content.replace("SININGUNO", "elif")
    content = content.replace("SINO", "else")
    content = content.replace("SUMA_DICCIONARIO", "update")
    content = content.replace("SUMA_LISTA", "extend")
    content = content.replace("TAN", "tan")
    content = content.replace("TITULO", "title")
    content = content.replace("TRADUCIR", "translate")
    content = content.replace("TRADUCCION", "maketrans")
    content = content.replace("Y", "and")


    return content # Devuelve el contenido remplazado.

# Función que ejecuta y compila ella misma.
def execute():
    archive = askopenfilename(title="Ejecutar programa",initialdir="C:/Users/{}/Documents".format(str(user_win)), filetypes=(("mrcmt", "*.mrcmt"), ), )
    translate = traduction(archive)
    py = open("compilator.py", "w")
    py.write(translate)
    py.close()
    deleted = popen("cls").read().replace("\n", "")
    if deleted.startswith("\"cls\""):
        system("clear") # Sirve para Windows.
    else:
        system("cls") # Si no es Windows limpiará la consola en sistemas Linux.
    system("python compilator.py")
    remove("compilator.py") # Remueve el archivo que genera con Python de compilador.

def goeditor():
    popen("python editor.py") # Abre el editor al clickar el botón. Esta acción la puedes ver en botones: butoneditor



# Canvas
canva = Canvas(vent,background="white", height=1080, width=1920)

# Botones
buton_preview = Button(vent, text="Ejecutar", font="Arial 28", background="black", fg="white",command=lambda: execute())
butoneditor = Button(vent, text="Editar código", font="Arial 28", background="black", fg="white",command=lambda: goeditor())

# Columnas
buton_preview.grid(row=0, column=0)
butoneditor.grid(row=1,column=0)

# Loop principal. Sin él, la aplicación solo abriria un frame. (la verías aparecer y desaparecer)
vent.mainloop()