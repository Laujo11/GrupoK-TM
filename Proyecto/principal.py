# ----------IMPORTS----------
import tkinter as grupoK
from tkinter import CENTER, messagebox as cajaMensaje
from tkinter.font import BOLD

# ----------FUNCIONES----------


def abrirMenu():
    ventanaPrincipal.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_variables():
    ventanaVariable.deiconify()
    ventanaMenu.withdraw()


def funcionEnteros():
    ventanaEnteros.deiconify()
    ventanaVariable.withdraw()


def funcion_volver_enteros():
    ventanaVariable.deiconify()
    ventanaEnteros.withdraw()


def funcionFlotantes():
    ventanaFlotantes.deiconify()
    ventanaVariable.withdraw()


def funcion_volver_flotantes():
    ventanaVariable.deiconify()
    ventanaFlotantes.withdraw()


def funcionCaracter():
    ventanaCaracter.deiconify()
    ventanaVariable.withdraw()


def funcion_volver_caracter():
    ventanaVariable.deiconify()
    ventanaCaracter.withdraw()


def funcionCadena():
    ventanaCadena.deiconify()
    ventanaVariable.withdraw()


def funcion_volver_cadena():
    ventanaVariable.deiconify()
    ventanaCadena.withdraw()


def funcionLogico():
    ventanaLogico.deiconify()
    ventanaVariable.withdraw()


def funcion_volver_logicos():
    ventanaVariable.deiconify()
    ventanaLogico.withdraw()


def funcion_volver_variables():
    ventanaVariable.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_condicionales():
    ventanaCondicionales.deiconify()
    ventanaMenu.withdraw()


def funcionCondicionalSimple():
    ventanaCondicionalSimple.deiconify()
    ventanaCondicionales.withdraw()


def funcion_volver_condicional_simple():
    ventanaCondicionales.deiconify()
    ventanaCondicionalSimple.withdraw()


def funcionCondicionalAlternativo():
    ventanaCondicionalAlternativo.deiconify()
    ventanaCondicionales.withdraw()


def funcion_volver_condicional_alternativo():
    ventanaCondicionales.deiconify()
    ventanaCondicionalAlternativo.withdraw()


def funcionCondicionalAnidado():
    ventanaCondicionalAnidado.deiconify()
    ventanaCondicionales.withdraw()


def funcion_volver_condicional_anidado():
    ventanaCondicionales.deiconify()
    ventanaCondicionalAnidado.withdraw()


def funcionCondicionalSwitch():
    ventanaCondicionalSwitchCase.deiconify()
    ventanaCondicionales.withdraw()


def funcion_volver_condicional_switchCase():
    ventanaCondicionales.deiconify()
    ventanaCondicionalSwitchCase.withdraw()


def funcion_volver_condicionales():
    ventanaMenu.deiconify()
    ventanaCondicionales.withdraw()


def funcion_aprender_bucles():
    ventanaBucles.deiconify()
    ventanaMenu.withdraw()


def funcionFor():
    ventanaBucles.withdraw()
    ventanaFor.deiconify()


def funcionVolverFor():
    ventanaFor.withdraw()
    ventanaBucles.deiconify()


def funcionWhile():
    ventanaBucles.withdraw()
    ventanaWhile.deiconify()


def funcionVolverWhile():
    ventanaWhile.withdraw()
    ventanaBucles.deiconify()


def funcionDoWhile():
    ventanaBucles.withdraw()
    ventanaDoWhile.deiconify()


def funcionVolverDoWhile():
    ventanaDoWhile.withdraw()
    ventanaBucles.deiconify()


def funcionVolverBucle():
    ventanaBucles.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_arreglos():
    ventanaArreglos.deiconify()
    ventanaMenu.withdraw()


def funcionVector():
    ventanaArreglos.withdraw()
    ventanaVector.deiconify()


def funcionVolverVector():
    ventanaVector.withdraw()
    ventanaArreglos.deiconify()


def funcionMatriz():
    ventanaArreglos.withdraw()
    ventanaMatriz.deiconify()


def funcionVolverMatriz():
    ventanaMatriz.withdraw()
    ventanaArreglos.deiconify()


def funcionVolverArreglo():
    ventanaArreglos.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_metodos():
    ventanaMetodos.deiconify()
    ventanaMenu.withdraw()


def funcion_procedimientos():
    ventanaMetodos.withdraw()
    ventanaProcedimientos.deiconify()


def funcion_volver_procedimientos():
    ventanaProcedimientos.withdraw()
    ventanaMetodos.deiconify()


def funcion_funciones():
    ventanaMetodos.withdraw()
    ventanaFunciones.deiconify()


def funcion_volver_funciones():
    ventanaFunciones.withdraw()
    ventanaMetodos.deiconify()


def funcion_volver_metodos():
    ventanaMetodos.withdraw()
    ventanaMenu.deiconify()


def funcion_volver_menu():
    ventanaMenu.withdraw()
    ventanaPrincipal.deiconify()


def salirProgramaDesdePrincipal():
    if cajaMensaje.askokcancel("No te vayas :(", "¿Seguro desea salir?"):
        ventanaPrincipal.destroy()
        ventanaMenu.destroy()
        ventanaEnteros.destroy()
        ventanaFlotantes.destroy()
        ventanaCaracter.destroy()
        ventanaCadena.destroy()
        ventanaLogico.destroy()
        ventanaVariable.destroy()
        ventanaCondicionales.destroy()
        ventanaCondicionalSimple.destroy()
        ventanaCondicionalAlternativo.destroy()
        ventanaCondicionalAnidado.destroy()
        ventanaCondicionalSwitchCase.destroy()
        ventanaBucles.destroy()
        ventanaFor.destroy()
        ventanaWhile.destroy()
        ventanaDoWhile.destroy()
        ventanaArreglos.destroy()
        ventanaVector.destroy()
        ventanaMatriz.destroy()
        ventanaMetodos.destroy()
        ventanaProcedimientos.destroy()
        ventanaFunciones.destroy()


# ----------ELEMENTOS----------
# VENTANA PRINCIPAL
# ventana
ventanaPrincipal = grupoK.Tk()
tituloVentanaPrincipal = "While(true): Aprender!"
ventanaPrincipal.title(tituloVentanaPrincipal)
ventanaPrincipal.geometry("400x200+500+100")
ventanaPrincipal.resizable(width=False, height=False)
ventanaPrincipal.config(bg="greenyellow")
#photo1 = grupoK.PhotoImage(file="Proyecto/icono.png")
#ventanaPrincipal.iconphoto(False, photo1)
ventanaPrincipal.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# entradas
campoDeTextoPrincipal = grupoK.Entry(ventanaPrincipal,
                                     text="Ingresa tu nombre",
                                     font="calibri",
                                     background="white")
campoDeTextoPrincipal.pack()
campoDeTextoPrincipal.place(x=100, y=80, width=200, height=30)

# etiquetas
etiqueta_bienvenida = grupoK.Label(ventanaPrincipal,
                                   text="Bienvenido",
                                   bg="greenyellow",
                                   font=("calibri", 20, "bold"))
etiqueta_bienvenida.pack()
etiqueta_bienvenida.place(x=125, y=10,  width=150, height=30)

mensaje_nombre = grupoK.Label(ventanaPrincipal,
                              text="Ingresá tu nombre",
                              bg="greenyellow",
                              font=("calibri", 12, "bold"))
mensaje_nombre.pack()
mensaje_nombre.place(x=125, y=40,  width=150, height=30)

# botones
boton_menu_principal = grupoK.Button(ventanaPrincipal,
                                     text="Ingresar",
                                     font=("calibri", 13, "bold"),
                                     cursor="hand2",
                                     command=abrirMenu)
boton_menu_principal.pack()
boton_menu_principal.place(x=180, y=150, width=100, height=30)

boton_salir_principal = grupoK.Button(ventanaPrincipal,
                                      text="Salir",
                                      font=("calibri", 13, "bold"),
                                      cursor="hand2",
                                      command=salirProgramaDesdePrincipal)
boton_salir_principal.pack()
boton_salir_principal.place(x=290, y=150, width=100, height=30)

# VENTANA MENU
# ventana
ventanaMenu = grupoK.Tk()
ventanaMenu.title("Menú de elección")
ventanaMenu.geometry("400x400+500+100")
ventanaMenu.resizable(width=False, height=False)
ventanaMenu.config(bg="royalblue")
#photo2 = grupoK.PhotoImage(file = "Proyecto/icono.png")
#ventanaMenu.iconphoto(False, photo1)
ventanaMenu.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
cartel_opcion = grupoK.Label(ventanaMenu,
                             text="Elija el apartado al cual quiere ingresar",
                             font=("calibri", 12, "bold"),
                             bg="royalblue")
cartel_opcion.pack()

# botones
boton_variables = grupoK.Button(ventanaMenu,
                                text="Variables",
                                command=funcion_aprender_variables)
boton_variables.pack()
boton_variables.place(x=150, y=50, width=100, height=30)

boton_condicionales = grupoK.Button(ventanaMenu,
                                    text="Condicionales",
                                    command=funcion_aprender_condicionales)
boton_condicionales.pack()
boton_condicionales.place(x=150, y=100, width=100, height=30)

boton_bucles = grupoK.Button(ventanaMenu,
                             text="Bucles",
                             command=funcion_aprender_bucles)
boton_bucles.pack()
boton_bucles.place(x=150, y=150, width=100, height=30)

boton_arreglos = grupoK.Button(ventanaMenu,
                               text="Arreglos",
                               command=funcion_aprender_arreglos)
boton_arreglos.pack()
boton_arreglos.place(x=150, y=200, width=100, height=30)

boton_metodos = grupoK.Button(ventanaMenu,
                              text="Métodos",
                              command=funcion_aprender_metodos)
boton_metodos.pack()
boton_metodos.place(x=150, y=250, width=100, height=30)

boton_volver_menu = grupoK.Button(ventanaMenu,
                                  text="Volver",
                                  command=funcion_volver_menu)
boton_volver_menu.pack()
boton_volver_menu.place(x=150, y=300, width=100, height=30)

# VENTANA VARIABLES
# ventana
ventanaVariable = grupoK.Tk()
ventanaVariable.title("Variables")
ventanaVariable.geometry("400x350+500+100")
ventanaVariable.resizable(width=False, height=False)
ventanaVariable.config(bg="coral")
ventanaVariable.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
elegir = grupoK.Label(ventanaVariable,
                      text="Elija el tipo de variable que quiere aprender",
                      font=("calibri", 12, "bold"),
                      bg="coral")
elegir.pack()

# botones
botonEntero = grupoK.Button(ventanaVariable,
                            text="Enteros",
                            command=funcionEnteros)
botonEntero.pack()
botonEntero.place(x=150, y=50, width=100, height=30)

botonFlotantes = grupoK.Button(ventanaVariable,
                               text="Flotantes",
                               command=funcionFlotantes)
botonFlotantes.pack()
botonFlotantes.place(x=150, y=100, width=100, height=30)

botonCaracter = grupoK.Button(ventanaVariable,
                              text="Caracter",
                              command=funcionCaracter)
botonCaracter.pack()
botonCaracter.place(x=150, y=150, width=100, height=30)

botonCadena = grupoK.Button(ventanaVariable,
                            text="Cadena",
                            command=funcionCadena)
botonCadena.pack()
botonCadena.place(x=150, y=200, width=100, height=30)

botonBoolean = grupoK.Button(ventanaVariable,
                             text="Boolean",
                             command=funcionLogico)
botonBoolean.pack()
botonBoolean.place(x=150, y=250, width=100, height=30)

boton_volver_variables = grupoK.Button(ventanaVariable,
                                       text="Volver",
                                       command=funcion_volver_variables)
boton_volver_variables.pack()
boton_volver_variables.place(x=150, y=300, width=100, height=30)

# VENTANA ENTEROS
# ventana
ventanaEnteros = grupoK.Tk()
ventanaEnteros.title("Enteros")
ventanaEnteros.geometry("400x350+500+100")
ventanaEnteros.resizable(width=False, height=False)
ventanaEnteros.config(bg="coral1")
ventanaEnteros.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaEnteros = grupoK.Label(ventanaEnteros,
                               text="Variables de tipo entero",
                               font=("calibri", 12, "bold"),
                               background="coral1")
etiquetaEnteros.pack()
etiquetaEnteros.place(x=100, y=5, width=200, height=30)

etiquetaTeoriaEnteros = grupoK.Label(ventanaEnteros,
                                     text="Para definir este tipo de variables debemos asignar un \nvalor entero a una variable al momento de declararla...\n\nPor ejemplo: num_entero = 2",
                                     font=("calibri", 11, "normal"),
                                     background="coral1",
                                     anchor="nw")
etiquetaTeoriaEnteros.pack()
etiquetaTeoriaEnteros.place(x=20, y=30, width=360, height=90)

etiquetaIntentoEnteros = grupoK.Label(ventanaEnteros,
                                      text="¡Ahora intentalo tu!",
                                      font=("calibri", 11, "normal"),
                                      background="coral1",
                                      anchor="nw")
etiquetaIntentoEnteros.pack()
etiquetaIntentoEnteros.place(x=20, y=120, width=360, height=40)


# botones
boton_volver_enteros = grupoK.Button(ventanaEnteros,
                                     text="Volver",
                                     command=funcion_volver_enteros)
boton_volver_enteros.pack()
boton_volver_enteros.place(x=150, y=300, width=100, height=30)

# VENTANA FLOTANTES/REALES
# ventana
ventanaFlotantes = grupoK.Tk()
ventanaFlotantes.title("Flotantes")
ventanaFlotantes.geometry("400x250+500+100")
ventanaFlotantes.resizable(width=False, height=False)
ventanaFlotantes.config(bg="coral2")
ventanaFlotantes.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFlotantes = grupoK.Label(ventanaFlotantes,
                                 text="Teoría sobre flotantes",
                                 font=("calibri", 12, "bold"),
                                 background="coral2")
etiquetaFlotantes.pack()

# botones
boton_volver_flotantes = grupoK.Button(ventanaFlotantes,
                                       text="Volver",
                                       command=funcion_volver_flotantes)
boton_volver_flotantes.pack()
boton_volver_flotantes.place(x=150, y=200, width=100, height=30)


# VENTANA CARACTERES
# ventana
ventanaCaracter = grupoK.Tk()
ventanaCaracter.title("Caracteres")
ventanaCaracter.geometry("400x250+500+100")
ventanaCaracter.resizable(width=False, height=False)
ventanaCaracter.config(bg="coral3")
ventanaCaracter.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCaracter = grupoK.Label(ventanaCaracter,
                                text="Teoría sobre carácteres",
                                font=("calibri", 12, "bold"),
                                background="coral3")
etiquetaCaracter.pack()

# botones
boton_volver_caracter = grupoK.Button(ventanaCaracter,
                                      text="Volver",
                                      command=funcion_volver_caracter)
boton_volver_caracter.pack()
boton_volver_caracter.place(x=150, y=200, width=100, height=30)

# VENTANA CADENAS
# ventana
ventanaCadena = grupoK.Tk()
ventanaCadena.title("Cadenas de texto")
ventanaCadena.geometry("400x250+500+100")
ventanaCadena.resizable(width=False, height=False)
ventanaCadena.config(bg="red")
ventanaCadena.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCadena = grupoK.Label(ventanaCadena,
                              text="Teoría sobre cadenas",
                              font=("calibri", 12, "bold"),
                              background="red")
etiquetaCadena.pack()


# botones
boton_volver_cadena = grupoK.Button(ventanaCadena,
                                    text="Volver",
                                    command=funcion_volver_cadena)
boton_volver_cadena.pack()
boton_volver_cadena.place(x=150, y=200, width=100, height=30)

# VENTANA LÓGICOS
# ventana
ventanaLogico = grupoK.Tk()
ventanaLogico.title("Lógicos")
ventanaLogico.geometry("400x250+500+100")
ventanaLogico.resizable(width=False, height=False)
ventanaLogico.config(bg="coral3")
ventanaLogico.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaLogico = grupoK.Label(ventanaLogico,
                              text="Teoría sobre lógicos",
                              font=("calibri", 12, "bold"),
                              background="coral3")
etiquetaLogico.pack()

# botones
boton_volver_logicos = grupoK.Button(ventanaLogico,
                                     text="Volver",
                                     command=funcion_volver_logicos)
boton_volver_logicos.pack()
boton_volver_logicos.place(x=150, y=200, width=100, height=30)

# VENTANA CONDICIONALES
# ventana
ventanaCondicionales = grupoK.Tk()
ventanaCondicionales.title("Condicionales")
ventanaCondicionales.geometry("400x300+500+100")
ventanaCondicionales.resizable(width=False, height=False)
ventanaCondicionales.config(bg="aquamarine")
ventanaCondicionales.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
elegirCondic = grupoK.Label(ventanaCondicionales,
                            text="Elija el tipo de condicional que quiere aprender",
                            font=("calibri", 12, "bold"),
                            bg="aquamarine")
elegirCondic.pack()

# botones
botonCondicSimpl = grupoK.Button(ventanaCondicionales,
                                 text="Condicional Simple",
                                 command=funcionCondicionalSimple)
botonCondicSimpl.pack()
botonCondicSimpl.place(x=100, y=50, width=200, height=30)

botonCondicAltern = grupoK.Button(ventanaCondicionales,
                                  text="Condicional Alternativo",
                                  command=funcionCondicionalAlternativo)
botonCondicAltern.pack()
botonCondicAltern.place(x=100, y=100, width=200, height=30)

botonCondicAnidado = grupoK.Button(ventanaCondicionales,
                                   text="Condicional Anidado",
                                   command=funcionCondicionalAnidado)
botonCondicAnidado.pack()
botonCondicAnidado.place(x=100, y=150, width=200, height=30)

botonCondicSwitch = grupoK.Button(ventanaCondicionales,
                                  text="Condicional Switch Case ",
                                  command=funcionCondicionalSwitch)
botonCondicSwitch.pack()
botonCondicSwitch.place(x=100, y=200, width=200, height=30)

boton_volver_condicionales = grupoK.Button(ventanaCondicionales,
                                           text="Volver",
                                           command=funcion_volver_condicionales)
boton_volver_condicionales.pack()
boton_volver_condicionales.place(x=150, y=250, width=100, height=30)

# VENTANA CONDICIONAL SIMPLE
# ventana
ventanaCondicionalSimple = grupoK.Tk()
ventanaCondicionalSimple.title("Condicional Simple")
ventanaCondicionalSimple.geometry("400x300+500+100")
ventanaCondicionalSimple.resizable(width=False, height=False)
ventanaCondicionalSimple.config(bg="aquamarine")
ventanaCondicionalSimple.protocol(
    "WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCondSimple = grupoK.Label(ventanaCondicionalSimple,
                                  text="Teoría sobre condicional simple",
                                  font=("calibri", 12, "bold"),
                                  background="aquamarine")
etiquetaCondSimple.pack()

# botones
boton_volver_condicional_simple = grupoK.Button(ventanaCondicionalSimple,
                                                text="Volver",
                                                command=funcion_volver_condicional_simple)
boton_volver_condicional_simple.pack()
boton_volver_condicional_simple.place(x=150, y=250, width=100, height=30)

# VENTANA CONDICIONAL ALTERNATIVO
# ventana
ventanaCondicionalAlternativo = grupoK.Tk()
ventanaCondicionalAlternativo.title("Condicional Alternativo")
ventanaCondicionalAlternativo.geometry("400x300+500+100")
ventanaCondicionalAlternativo.resizable(width=False, height=False)
ventanaCondicionalAlternativo.config(bg="aquamarine")
ventanaCondicionalAlternativo.protocol(
    "WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCondAlter = grupoK.Label(ventanaCondicionalAlternativo,
                                 text="Teoría sobre condicional alternativo",
                                 font=("calibri", 12, "bold"),
                                 background="aquamarine")
etiquetaCondAlter.pack()

# botones
boton_volver_condicional_alternativo = grupoK.Button(ventanaCondicionalAlternativo,
                                                     text="Volver",
                                                     command=funcion_volver_condicional_alternativo)
boton_volver_condicional_alternativo.pack()
boton_volver_condicional_alternativo.place(x=150, y=250, width=100, height=30)

# VENTANA CONDICIONAL SIMPLE
# ventana
ventanaCondicionalAnidado = grupoK.Tk()
ventanaCondicionalAnidado.title("Condicional Anidado")
ventanaCondicionalAnidado.geometry("400x300+500+100")
ventanaCondicionalAnidado.resizable(width=False, height=False)
ventanaCondicionalAnidado.config(bg="aquamarine")
ventanaCondicionalAnidado.protocol(
    "WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCondAnid = grupoK.Label(ventanaCondicionalAnidado,
                                text="Teoría sobre condicional anidado",
                                font=("calibri", 12, "bold"),
                                background="aquamarine")
etiquetaCondAnid.pack()

# botones
boton_volver_condicional_anidado = grupoK.Button(ventanaCondicionalAnidado,
                                                 text="Volver",
                                                 command=funcion_volver_condicional_anidado)
boton_volver_condicional_anidado.pack()
boton_volver_condicional_anidado.place(x=150, y=250, width=100, height=30)

# VENTANA CONDICIONAL SWITCH CASE
# ventana
ventanaCondicionalSwitchCase = grupoK.Tk()
ventanaCondicionalSwitchCase.title("Condicional Switch Case")
ventanaCondicionalSwitchCase.geometry("400x300+500+100")
ventanaCondicionalSwitchCase.resizable(width=False, height=False)
ventanaCondicionalSwitchCase.config(bg="aquamarine")
ventanaCondicionalSwitchCase.protocol(
    "WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCondSC = grupoK.Label(ventanaCondicionalSwitchCase,
                              text="Teoría sobre condicional switch-case",
                              font=("calibri", 12, "bold"),
                              background="aquamarine")
etiquetaCondSC.pack()

# botones
boton_volver_condicional_switch_case = grupoK.Button(ventanaCondicionalSwitchCase,
                                                     text="Volver",
                                                     command=funcion_volver_condicional_switchCase)
boton_volver_condicional_switch_case.pack()
boton_volver_condicional_switch_case.place(x=150, y=250, width=100, height=30)

# VENTANA BUCLES
# ventana
ventanaBucles = grupoK.Tk()
ventanaBucles.title("Bucles")
ventanaBucles.geometry("400x250+500+100")
ventanaBucles.resizable(width=False, height=False)
ventanaBucles.config(bg="cyan2")
ventanaBucles.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaBucles = grupoK.Label(ventanaBucles,
                              text="Elija el bucle que quiere aprender",
                              font=("calibri", 12, "bold"),
                              background="cyan2")
etiquetaBucles.pack()

# botones
botonFor = grupoK.Button(ventanaBucles,
                         text="For",
                         command=funcionFor)
botonFor.pack()
botonFor.place(x=150, y=50, width=100, height=30)

botonWhile = grupoK.Button(ventanaBucles,
                           text="While",
                           command=funcionWhile)
botonWhile.pack()
botonWhile.place(x=150, y=100, width=100, height=30)

botonDoWhile = grupoK.Button(ventanaBucles,
                             text="Do-While",
                             command=funcionDoWhile)
botonDoWhile.pack()
botonDoWhile.place(x=150, y=150, width=100, height=30)

botonVolverBucles = grupoK.Button(ventanaBucles,
                                  text="Volver",
                                  command=funcionVolverBucle)
botonVolverBucles.pack()
botonVolverBucles.place(x=150, y=200, width=100, height=30)

# VENTANA FOR
# ventana
ventanaFor = grupoK.Tk()
ventanaFor.title("For")
ventanaFor.geometry("400x250+500+100")
ventanaFor.resizable(width=False, height=False)
ventanaFor.config(bg="thistle1")
ventanaFor.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFor = grupoK.Label(ventanaFor,
                           text="Teoría sobre For",
                           font=("calibri", 12, "bold"),
                           background="thistle1")
etiquetaFor.pack()

# botones
botonVolverFor = grupoK.Button(ventanaFor,
                               text="Volver",
                               command=funcionVolverFor)
botonVolverFor.pack()
botonVolverFor.place(x=150, y=200, width=100, height=30)

# VENTANA WHILE
# ventana
ventanaWhile = grupoK.Tk()
ventanaWhile.title("While")
ventanaWhile.geometry("400x250+500+100")
ventanaWhile.resizable(width=False, height=False)
ventanaWhile.config(bg="DarkSeaGreen1")
ventanaWhile.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaWhile = grupoK.Label(ventanaWhile,
                             text="Teoría sobre While",
                             font=("calibri", 12, "bold"),
                             background="DarkSeaGreen1")
etiquetaWhile.pack()

# botones
botonVolverWhile = grupoK.Button(ventanaWhile,
                                 text="Volver",
                                 command=funcionVolverWhile)
botonVolverWhile.pack()
botonVolverWhile.place(x=150, y=200, width=100, height=30)

# VENTANA DO-WHILE
# ventana
ventanaDoWhile = grupoK.Tk()
ventanaDoWhile.title("Do-While")
ventanaDoWhile.geometry("400x250+500+100")
ventanaDoWhile.resizable(width=False, height=False)
ventanaDoWhile.config(bg="powder blue")
ventanaDoWhile.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaDoWhile = grupoK.Label(ventanaDoWhile,
                               text="Teoría sobre Do-While",
                               font=("calibri", 12, "bold"),
                               background="powder blue")
etiquetaDoWhile.pack()

# botones
botonVolverDoWhile = grupoK.Button(ventanaDoWhile,
                                   text="Volver",
                                   command=funcionVolverDoWhile)
botonVolverDoWhile.pack()
botonVolverDoWhile.place(x=150, y=200, width=100, height=30)

# VENTANA ARREGLOS
# ventana
ventanaArreglos = grupoK.Tk()
ventanaArreglos.title("Arreglos")
ventanaArreglos.geometry("400x250+500+100")
ventanaArreglos.resizable(width=False, height=False)
ventanaArreglos.config(bg="maroon")
ventanaArreglos.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaArreglo = grupoK.Label(ventanaArreglos,
                               text="Elija el arreglo que quiere aprender",
                               font=("calibri", 12, "bold"),
                               background="maroon")
etiquetaArreglo.pack()

# botones
botonVector = grupoK.Button(ventanaArreglos,
                            text="Vectores",
                            command=funcionVector)
botonVector.pack()
botonVector.place(x=150, y=50, width=100, height=30)

botonMatriz = grupoK.Button(ventanaArreglos,
                            text="Matrices",
                            command=funcionMatriz)
botonMatriz.pack()
botonMatriz.place(x=150, y=100, width=100, height=30)

botonVolverArreglor = grupoK.Button(ventanaArreglos,
                                    text="Volver",
                                    command=funcionVolverArreglo)
botonVolverArreglor.pack()
botonVolverArreglor.place(x=150, y=150, width=100, height=30)

# VENTANA VECTOR
# ventana
ventanaVector = grupoK.Tk()
ventanaVector.title("Vectores")
ventanaVector.geometry("400x250+500+100")
ventanaVector.resizable(width=False, height=False)
ventanaVector.config(bg="dark salmon")
ventanaVector.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaVector = grupoK.Label(ventanaVector,
                              text="Teoría sobre Vectores",
                              font=("calibri", 12, "bold"),
                              background="dark salmon")
etiquetaVector.pack()

# botones
botonVolverVector = grupoK.Button(ventanaVector,
                                  text="Volver",
                                  command=funcionVolverVector)
botonVolverVector.pack()
botonVolverVector.place(x=150, y=200, width=100, height=30)

# VENTANA MATRIZ
# ventana
ventanaMatriz = grupoK.Tk()
ventanaMatriz.title("Matrices")
ventanaMatriz.geometry("400x250+500+100")
ventanaMatriz.resizable(width=False, height=False)
ventanaMatriz.config(bg="DarkOliveGreen4")
ventanaMatriz.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaMatriz = grupoK.Label(ventanaMatriz,
                              text="Teoría sobre Matrices",
                              font=("calibri", 12, "bold"),
                              background="DarkOliveGreen4")
etiquetaMatriz.pack()

# botones
botonVolverMatriz = grupoK.Button(ventanaMatriz,
                                  text="Volver",
                                  command=funcionVolverMatriz)
botonVolverMatriz.pack()
botonVolverMatriz.place(x=150, y=200, width=100, height=30)

# VENTANA MÉTODOS
# ventana
ventanaMetodos = grupoK.Tk()
ventanaMetodos.title("Métodos")
ventanaMetodos.geometry("400x250+500+100")
ventanaMetodos.resizable(width=False, height=False)
ventanaMetodos.config(bg="orchid1")
ventanaMetodos.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaMetodos = grupoK.Label(ventanaMetodos,
                               text="Elegí una opción",
                               font=("calibri", 12, "bold"),
                               background="orchid1")
etiquetaMetodos.pack()

# botones
botonProcedimientos = grupoK.Button(ventanaMetodos,
                                    text="Procedimientos",
                                    command=funcion_procedimientos)
botonProcedimientos.pack()
botonProcedimientos.place(x=150, y=50, width=100, height=30)

botonFunciones = grupoK.Button(ventanaMetodos,
                               text="Funciones",
                               command=funcion_funciones)
botonFunciones.pack()
botonFunciones.place(x=150, y=100, width=100, height=30)

boton_volver_metodos = grupoK.Button(ventanaMetodos,
                                     text="Volver",
                                     command=funcion_volver_metodos)
boton_volver_metodos.pack()
boton_volver_metodos.place(x=150, y=150, width=100, height=30)

# VENTANA PROCEDIMIENTOS
# ventana
ventanaProcedimientos = grupoK.Tk()
ventanaProcedimientos.title("Procedimientos")
ventanaProcedimientos.geometry("400x250+500+100")
ventanaProcedimientos.resizable(width=False, height=False)
ventanaProcedimientos.config(bg="orange")
ventanaProcedimientos.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaProcedimientos = grupoK.Label(ventanaProcedimientos,
                                      text="Teoría sobre procedimientos",
                                      font=("calibri", 12, "bold"),
                                      background="orange")
etiquetaProcedimientos.pack()

# botones
boton_volver_procedimientos = grupoK.Button(ventanaProcedimientos,
                                            text="Volver",
                                            command=funcion_volver_procedimientos)
boton_volver_procedimientos.pack()
boton_volver_procedimientos.place(x=150, y=150, width=100, height=30)

# VENTANA FUNCIONES
# ventana
ventanaFunciones = grupoK.Tk()
ventanaFunciones.title("Funciones")
ventanaFunciones.geometry("400x250+500+100")
ventanaFunciones.resizable(width=False, height=False)
ventanaFunciones.config(bg="red")
ventanaFunciones.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFunciones = grupoK.Label(ventanaFunciones,
                                 text="Teoría sobre funciones",
                                 font=("calibri", 12, "bold"),
                                 background="red")
etiquetaFunciones.pack()

# botones
boton_volver_funciones = grupoK.Button(ventanaFunciones,
                                       text="Volver",
                                       command=funcion_volver_funciones)
boton_volver_funciones.pack()
boton_volver_funciones.place(x=150, y=150, width=100, height=30)

# ------------------------------------------------------
# INICIO
ventanaMenu.withdraw()
ventanaVariable.withdraw()
ventanaEnteros.withdraw()
ventanaFlotantes.withdraw()
ventanaCaracter.withdraw()
ventanaCadena.withdraw()
ventanaLogico.withdraw()
ventanaCondicionales.withdraw()
ventanaCondicionalSimple.withdraw()
ventanaCondicionalAlternativo.withdraw()
ventanaCondicionalAnidado.withdraw()
ventanaCondicionalSwitchCase.withdraw()
ventanaBucles.withdraw()
ventanaFor.withdraw()
ventanaWhile.withdraw()
ventanaDoWhile.withdraw()
ventanaArreglos.withdraw()
ventanaVector.withdraw()
ventanaMatriz.withdraw()
ventanaMetodos.withdraw()
ventanaProcedimientos.withdraw()
ventanaFunciones.withdraw()
ventanaPrincipal.mainloop()
