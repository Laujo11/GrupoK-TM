# ----------IMPORTS----------
import tkinter as grupoK
from tkinter import CENTER, messagebox as cajaMensaje
from tkinter.font import BOLD

# ----------FUNCIONES----------


def abrirMenu():
    if bool(campoDeTextoPrincipal.get().strip()):
        cartel_opcion.configure(text=campoDeTextoPrincipal.get(
        ).strip() + ", elija el \napartado al cual quiere ingresar")
        ventanaPrincipal.withdraw()
        ventanaMenu.deiconify()
    else:
        cajaMensaje.showwarning("Ups!", "No te olvides de ingresar tu nombre")


def funcion_aprender_variables():
    ventanaVariable.deiconify()
    ventanaMenu.withdraw()


def funcionEnteros():
    ventanaEnteros.deiconify()
    ventanaVariable.withdraw()


def funcion_confirmar_enteros():
    ejemploCampo = campoDeTextoEnteros.get().strip()
    ejemploDado = "numero_de_manzanas = 2"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n (numero_de_manzanas = 2)")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaVariable.deiconify()
        ventanaEnteros.withdraw()


def funcion_volver_enteros():
    ventanaVariable.deiconify()
    ventanaEnteros.withdraw()


def funcionFlotantes():
    ventanaFlotantes.deiconify()
    ventanaVariable.withdraw()


def funcion_confirmar_flotantes():
    ejemploCampo = campoDeTextoFloat.get().strip()
    ejemploDado = "precioDeRemeras = 1560.99"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n (precioDeRemeras = 1560.99)")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaVariable.deiconify()
        ventanaFlotantes.withdraw()


def funcion_volver_flotantes():
    ventanaVariable.deiconify()
    ventanaFlotantes.withdraw()


def funcionCaracter():
    ventanaCaracter.deiconify()
    ventanaVariable.withdraw()


def funcion_confirmar_caracter():
    ejemploCampo = campoDeTextoCaracter.get().strip()
    ejemploDado = "estoEsUnCaracter = 'a'"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n (estoEsUnCaracter = 'a')")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaVariable.deiconify()
        ventanaCaracter.withdraw()


def funcion_volver_caracter():
    ventanaVariable.deiconify()
    ventanaCaracter.withdraw()


def funcionCadena():
    ventanaCadena.deiconify()
    ventanaVariable.withdraw()


def funcion_confirmar_cadena():
    ejemploCampo = campoDeTextoCadena.get().strip()
    ejemploDado = 'estoEsUnaCadena = "Hola estas en nuestro proyecto de metodologia"'
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", '¡Lo que escribiste no es igual al ejemplo!\n (estoEsUnaCadena = "Hola estas en nuestro proyecto de metodologia")')
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaVariable.deiconify()
        ventanaCadena.withdraw()


def funcion_volver_cadena():
    ventanaVariable.deiconify()
    ventanaCadena.withdraw()


def funcionLogico():
    ventanaLogico.deiconify()
    ventanaVariable.withdraw()


def funcion_confirmar_logicos():
    ejemploCampo = campoDeTextoLogico.get().strip()
    ejemploDado1 = "x = true"
    ejemploDado2 = "y = false"

    if (ejemploCampo == "x = true, y = false"):
        cajaMensaje.showwarning(
            "Ups!", "¡Escribe solo uno de los ejemplos!\n (x = true , y = false)")
    else:
        if (ejemploCampo != ejemploDado1):
            if(ejemploCampo != ejemploDado2):
                cajaMensaje.showwarning(
                    "Ups!", "¡Lo que escribiste no es igual a alguno de los ejemplos!\n (x = true , y = false)")
            else:
                cajaMensaje.showinfo(
                    "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
                ventanaVariable.deiconify()
                ventanaLogico.withdraw()
        else:
            cajaMensaje.showinfo(
                "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
            ventanaVariable.deiconify()
            ventanaLogico.withdraw()


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


def funcion_confirmar_cond_simple():
    ejemploCampo = campoDeTextoCondSimple.get("1.0", "end").strip()
    ejemploDado = "if (edad>18):\n\tprint(\"Es mayor de edad\")"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n if (edad>18):\n\tprint(\"Es mayor de edad\")")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaCondicionales.deiconify()
        ventanaCondicionalSimple.withdraw()


def funcion_volver_condicional_simple():
    ventanaCondicionales.deiconify()
    ventanaCondicionalSimple.withdraw()


def funcionCondicionalAlternativo():
    ventanaCondicionalAlternativo.deiconify()
    ventanaCondicionales.withdraw()


def funcion_confirmar_cond_alternativo():
    ejemploCampo = campoDeTextoCondAlter.get("1.0", "end").strip()
    ejemploDado = "if (edad>18):\n\tprint(\"Es mayor de edad\")\nelse:\n\tprint(\"Es menor de edad\")"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\nif (edad>18):\n\tprint(\"Es mayor de edad\")\nelse:\n\tprint(\"Es menor de edad\")")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaCondicionales.deiconify()
        ventanaCondicionalAlternativo.withdraw()


def funcion_volver_condicional_alternativo():
    ventanaCondicionales.deiconify()
    ventanaCondicionalAlternativo.withdraw()


def funcionCondicionalAnidado():
    ventanaCondicionalAnidado.deiconify()
    ventanaCondicionales.withdraw()


def funcion_confirmar_cond_anidado():
    ejemploCampo = campoDeTextoCondAnid.get("1.0", "end").strip()
    ejemploDado = "if (edad>=18):\n\tif (edad>18):\n\t\tprint(\"Ya entró en la etapa de juventud\")\n\telse:\n\t\tprint(\"Sigue en la etapa de adolescencia\")\nelse:\n\tprint(\"Es menor de edad\")"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n if (edad>=18):\n\tif (edad>18):\n\t\tprint(\"Ya entró en la etapa de juventud\") \n\telse:\n\t\tprint(\"Sigue en la etapa de adolescencia\") \n else:\n\tprint(\"Es menor de edad\")")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaCondicionales.deiconify()
        ventanaCondicionalAnidado.withdraw()


def funcion_volver_condicional_anidado():
    ventanaCondicionales.deiconify()
    ventanaCondicionalAnidado.withdraw()


def funcionCondicionalSwitch():
    ventanaCondicionalSwitchCase.deiconify()
    ventanaCondicionales.withdraw()


def funcion_confirmar_cond_switch_case():
    ejemploCampo = campoDeTextoCondMCase.get("1.0", "end").strip()
    ejemploDado = "match color:\n\tcase \"rojo\":\n\t\tprint(\"El color es rojo\")\n\tcase \"azul\":\n\t\tprint(\"El color es azul\")\n\tcase \"verde\":\n\t\tprint(\"El color es verde\")\n\tcase_:\n\t\tprint(\"No existe ese color\")"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n match color: \n\tcase \"rojo\":\n\t\tprint(\"El color es rojo\")\n\tcase \"azul\":\n\t\tprint(\"El color es azul\")\n\tcase \"verde\":\n\t\tprint(\"El color es verde\")\n\tcase_:\n\t\tprint(\"No existe ese color\")")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaCondicionales.deiconify()
        ventanaCondicionalSwitchCase.withdraw()


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


def funcion_confirmar_for():
    ejemploCampo = campoDeTextoFor.get("1.0","end").strip()
    ejemploDado = "for i in range(1, 11):\n\tprint(i)"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n for i in range(1, 11): \n\tprint(i)")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaFor.withdraw()
        ventanaBucles.deiconify()


def funcionVolverFor():
    ventanaFor.withdraw()
    ventanaBucles.deiconify()


def funcionWhile():
    ventanaBucles.withdraw()
    ventanaWhile.deiconify()


def funcion_confirmar_while():
    ejemploCampo = campoDeTextoWhile.get("1.0","end").strip()
    ejemploDado = "a = 1\nwhile (a < 10):\n\tprint(\"¡Hola, mundo!\")\n\ta = a + 1"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n a = 1\nwhile (a < 10):\n\tprint(\"¡Hola, mundo!\")\n\ta = a + 1")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaWhile.withdraw()
        ventanaBucles.deiconify()


def funcionVolverWhile():
    ventanaWhile.withdraw()
    ventanaBucles.deiconify()


#def funcionDoWhile():
    #ventanaBucles.withdraw()
    #ventanaDoWhile.deiconify()


#def funcion_confirmar_Dowhile():
    #ejemploCampo = campoDeTextoDoWhile.get().strip()
    #ejemploDado = "-"
    #if (ejemploCampo != ejemploDado):
        #cajaMensaje.showwarning(
            #"Ups!", "¡Lo que escribiste no es igual al ejemplo!\n (-)")
    #else:
        #cajaMensaje.showinfo(
            #"Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        #ventanaDoWhile.withdraw()
        #ventanaBucles.deiconify()


#def funcionVolverDoWhile():
    #ventanaDoWhile.withdraw()
    #ventanaBucles.deiconify()


def funcionVolverBucle():
    ventanaBucles.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_arreglos():
    ventanaArreglos.deiconify()
    ventanaMenu.withdraw()


def funcionVector():
    ventanaArreglos.withdraw()
    ventanaVector.deiconify()


def funcion_confirmar_vector():
    ejemploCampo = campoDeTextoVector.get().strip()
    ejemploDado = "m = [1,2,3,4]"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n m = [1,2,3,4]")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaVector.withdraw()
        ventanaArreglos.deiconify()


def funcionVolverVector():
    ventanaVector.withdraw()
    ventanaArreglos.deiconify()


def funcionMatriz():
    ventanaArreglos.withdraw()
    ventanaMatriz.deiconify()


def funcion_confirmar_matriz():
    ejemploCampo = campoDeTextoMatriz.get().strip()
    ejemploDado = "m = [[1,2],[3,4]]"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n m = [[1,2],[3,4]]")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaMatriz.withdraw()
        ventanaArreglos.deiconify()


def funcionVolverMatriz():
    ventanaMatriz.withdraw()
    ventanaArreglos.deiconify()


def funcionVolverArreglo():
    ventanaArreglos.withdraw()
    ventanaMenu.deiconify()


def funcion_aprender_metodos():
    ventanaFunciones.deiconify()
    ventanaMenu.withdraw()


#def funcion_procedimientos():
    #ventanaMetodos.withdraw()
    #ventanaProcedimientos.deiconify()


#def funcion_confirmar_procedimientos():
    #ejemploCampo = campoDeTextoProcedimientos.get().strip()
    #ejemploDado = "-"
    #if (ejemploCampo != ejemploDado):
        #cajaMensaje.showwarning(
            #"Ups!", "¡Lo que escribiste no es igual al ejemplo!\n (-)")
    #else:
        #cajaMensaje.showinfo(
            #"Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        #ventanaProcedimientos.withdraw()
        #ventanaMetodos.deiconify()


#def funcion_volver_procedimientos():
    #ventanaProcedimientos.withdraw()
    #ventanaMetodos.deiconify()


#def funcion_funciones():
#    ventanaMetodos.withdraw()
#    ventanaFunciones.deiconify()


def funcion_confirmar_funciones():
    ejemploCampo = campoDeTextoFunciones.get("1.0","end").strip()
    ejemploDado = "def es_par(numero):\n\tif (numero % 2 == 0):\n\t\treturn True\n\telse:\n\t\treturn False"
    if (ejemploCampo != ejemploDado):
        cajaMensaje.showwarning(
            "Ups!", "¡Lo que escribiste no es igual al ejemplo!\n def es_par(numero):\n\tif (numero % 2 == 0):\n\t\treturn True\n\telse:\n\t\treturn False")
    else:
        cajaMensaje.showinfo(
            "Muy bien!", "¡Completaste este apartado! Ya puedes volver.")
        ventanaFunciones.withdraw()
        ventanaMenu.deiconify()


#def funcion_volver_funciones():
#    ventanaFunciones.withdraw()
#    ventanaMetodos.deiconify()


def funcion_volver_metodos():
    ventanaFunciones.withdraw()
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
        #ventanaDoWhile.destroy()
        ventanaArreglos.destroy()
        ventanaVector.destroy()
        ventanaMatriz.destroy()
        #ventanaMetodos.destroy()
        #ventanaProcedimientos.destroy()
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
# photo1 = grupoK.PhotoImage(file="Proyecto/icono.png")
# ventanaPrincipal.iconphoto(False, photo1)
ventanaPrincipal.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# entradas
campoDeTextoPrincipal = grupoK.Entry(ventanaPrincipal,
                                     font="Arial",
                                     background="white",
                                     width=11)
campoDeTextoPrincipal.pack()
campoDeTextoPrincipal.place(x=100, y=80, width=200, height=30)

# etiquetas
etiqueta_bienvenida = grupoK.Label(ventanaPrincipal,
                                   text="Bienvenido",
                                   bg="greenyellow",
                                   font=("calibri", 20, "bold"))
etiqueta_bienvenida.pack()
etiqueta_bienvenida.place(x=115, y=10,  width=170, height=30)

mensaje_nombre = grupoK.Label(ventanaPrincipal,
                              text="Ingresá tu nombre",
                              bg="greenyellow",
                              font=("calibri", 12, "bold"))
mensaje_nombre.pack()
mensaje_nombre.place(x=105, y=40,  width=190, height=30)

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
# photo2 = grupoK.PhotoImage(file = "Proyecto/icono.png")
# ventanaMenu.iconphoto(False, photo1)
ventanaMenu.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
cartel_opcion = grupoK.Label(ventanaMenu,
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
                              text="Funciones",
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
ventanaVariable.geometry("420x350+500+100")
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
etiquetaEnteros.place(x=90, y=5, width=230, height=40)

etiquetaTeoriaEnteros = grupoK.Label(ventanaEnteros,
                                     text="Para definir este tipo de variables debemos \nasignar un valor entero a una \nvariable al momento de declararla...\n\nPor ejemplo: \"numero_de_manzanas = 2\"",
                                     font=("calibri", 11, "normal"),
                                     background="coral1",
                                     anchor="nw")
etiquetaTeoriaEnteros.pack()
etiquetaTeoriaEnteros.place(x=30, y=40, width=360, height=140)

etiquetaIntentoEnteros = grupoK.Label(ventanaEnteros,
                                      text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                      font=("calibri", 11, "normal"),
                                      background="coral1",
                                      anchor="nw")
etiquetaIntentoEnteros.pack()
etiquetaIntentoEnteros.place(x=20, y=170, width=360, height=50)

# entradas
campoDeTextoEnteros = grupoK.Entry(ventanaEnteros,
                                   font=("calibri", 12),
                                   background="white"
                                   )
campoDeTextoEnteros.pack()
campoDeTextoEnteros.place(x=50, y=240, width=300, height=40)

# botones
boton_confirmar_enteros = grupoK.Button(ventanaEnteros,
                                        text="Confirmar",
                                        command=funcion_confirmar_enteros)
boton_confirmar_enteros.pack()
boton_confirmar_enteros.place(x=80, y=300, width=100, height=30)

boton_volver_enteros = grupoK.Button(ventanaEnteros,
                                     text="Volver",
                                     command=funcion_volver_enteros)
boton_volver_enteros.pack()
boton_volver_enteros.place(x=220, y=300, width=100, height=30)

# VENTANA FLOTANTES/REALES
# ventana
ventanaFlotantes = grupoK.Tk()
ventanaFlotantes.title("Flotantes")
ventanaFlotantes.geometry("400x320+500+100")
ventanaFlotantes.resizable(width=False, height=False)
ventanaFlotantes.config(bg="coral2")
ventanaFlotantes.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFlotantes = grupoK.Label(ventanaFlotantes,
                                 text="Teoría sobre flotantes",
                                 font=("calibri", 12, "bold"),
                                 background="coral2")
etiquetaFlotantes.pack()

etiquetaTeoriaFlotantes = grupoK.Label(ventanaFlotantes,
                                       text="Para definir este tipo de variables debemos \nasignar un valor decimal a una \nvariable al momento de declararla...\n\nPor ejemplo: \"precioDeRemeras = 1560.99\"",
                                       font=("calibri", 11, "normal"),
                                       background="coral2",
                                       anchor="nw")
etiquetaTeoriaFlotantes.pack()
etiquetaTeoriaFlotantes.place(x=30, y=30, width=360, height=120)

etiquetaIntentoFloat = grupoK.Label(ventanaFlotantes,
                                    text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                    font=("calibri", 11, "normal"),
                                    background="coral2",
                                    anchor="nw")
etiquetaIntentoFloat.pack()
etiquetaIntentoFloat.place(x=20, y=150, width=360, height=70)

# entradas

campoDeTextoFloat = grupoK.Entry(ventanaFlotantes,
                                 font=("calibri", 12),
                                 background="white"
                                 )
campoDeTextoFloat.pack()
campoDeTextoFloat.place(x=50, y=220, width=300, height=40)

# botones
boton_confirmar_flotantes = grupoK.Button(ventanaFlotantes,
                                          text="Confirmar",
                                          command=funcion_confirmar_flotantes)
boton_confirmar_flotantes.pack()
boton_confirmar_flotantes.place(x=80, y=280, width=100, height=30)

boton_volver_flotantes = grupoK.Button(ventanaFlotantes,
                                       text="Volver",
                                       command=funcion_volver_flotantes)
boton_volver_flotantes.pack()
boton_volver_flotantes.place(x=220, y=280, width=100, height=30)


# VENTANA CARACTERES
# ventana
ventanaCaracter = grupoK.Tk()
ventanaCaracter.title("Caracteres")
ventanaCaracter.geometry("410x305+500+100")
ventanaCaracter.resizable(width=False, height=False)
ventanaCaracter.config(bg="coral3")
ventanaCaracter.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCaracter = grupoK.Label(ventanaCaracter,
                                text="Teoría sobre carácteres",
                                font=("calibri", 12, "bold"),
                                background="coral3")
etiquetaCaracter.pack()

etiquetaTeoriaCaracter = grupoK.Label(ventanaCaracter,
                                      text="Para definir este tipo de variables debemos \ningresar un caracter entre un par de comillas \nsimples en una variable al momento de declararla...\n\nPor ejemplo: \"estoEsUnCaracter = 'a' \"",
                                      font=("calibri", 11, "normal"),
                                      background="coral3",
                                      anchor="nw")
etiquetaTeoriaCaracter.pack()
etiquetaTeoriaCaracter.place(x=10, y=30, width=390, height=120)

etiquetaIntentoCaracter = grupoK.Label(ventanaCaracter,
                                       text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                       font=("calibri", 11, "normal"),
                                       background="coral3",
                                       anchor="nw")
etiquetaIntentoCaracter.pack()
etiquetaIntentoCaracter.place(x=20, y=150, width=360, height=70)

# entradas

campoDeTextoCaracter = grupoK.Entry(ventanaCaracter,
                                    font=("calibri", 12),
                                    background="white"
                                    )
campoDeTextoCaracter.pack()
campoDeTextoCaracter.place(x=50, y=210, width=300, height=40)

# botones
boton_confirmar_caracteres = grupoK.Button(ventanaCaracter,
                                           text="Confirmar",
                                           command=funcion_confirmar_caracter)
boton_confirmar_caracteres.pack()
boton_confirmar_caracteres.place(x=80, y=260, width=100, height=30)

boton_volver_caracter = grupoK.Button(ventanaCaracter,
                                      text="Volver",
                                      command=funcion_volver_caracter)
boton_volver_caracter.pack()
boton_volver_caracter.place(x=220, y=260, width=100, height=30)

# VENTANA CADENAS
# ventana
ventanaCadena = grupoK.Tk()
ventanaCadena.title("Cadenas de texto")
ventanaCadena.geometry("410x350+500+100")
ventanaCadena.resizable(width=False, height=False)
ventanaCadena.config(bg="brown")
ventanaCadena.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCadena = grupoK.Label(ventanaCadena,
                              text="Teoría sobre cadenas",
                              font=("calibri", 12, "bold"),
                              background="brown")
etiquetaCadena.pack()

etiquetaTeoriaCadena = grupoK.Label(ventanaCadena,
                                    text="Para definir este tipo de variables debemos \ningresar un texto entre un par de comillas \ndoble en una variable al momento de declararla...\n\nPor ejemplo: \"estoEsUnaCadena = \"Hola estas en \nnuestro proyecto de metodologia\"\"",
                                    font=("calibri", 11, "normal"),
                                    background="brown",
                                    anchor="nw")
etiquetaTeoriaCadena.pack()
etiquetaTeoriaCadena.place(x=10, y=30, width=380, height=150)

etiquetaIntentoCadena = grupoK.Label(ventanaCadena,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="brown",
                                     anchor="nw")
etiquetaIntentoCadena.pack()
etiquetaIntentoCadena.place(x=20, y=180, width=360, height=70)

# entradas

campoDeTextoCadena = grupoK.Entry(ventanaCadena,
                                  font=("calibri", 12),
                                  background="white"
                                  )
campoDeTextoCadena.pack()
campoDeTextoCadena.place(x=50, y=250, width=300, height=40)


# botones
boton_confirmar_cadenas = grupoK.Button(ventanaCadena,
                                        text="Confirmar",
                                        command=funcion_confirmar_cadena)
boton_confirmar_cadenas.pack()
boton_confirmar_cadenas.place(x=80, y=300, width=100, height=30)


boton_volver_cadena = grupoK.Button(ventanaCadena,
                                    text="Volver",
                                    command=funcion_volver_cadena)
boton_volver_cadena.pack()
boton_volver_cadena.place(x=220, y=300, width=100, height=30)

# VENTANA LÓGICOS
# ventana
ventanaLogico = grupoK.Tk()
ventanaLogico.title("Lógicos")
ventanaLogico.geometry("400x350+500+100")
ventanaLogico.resizable(width=False, height=False)
ventanaLogico.config(bg="brown1")
ventanaLogico.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaLogico = grupoK.Label(ventanaLogico,
                              text="Teoría sobre lógicos",
                              font=("calibri", 12, "bold"),
                              background="brown1")
etiquetaLogico.pack()

etiquetaTeoriaLogico = grupoK.Label(ventanaLogico,
                                    text="Para definir este tipo de variables debemos \ningresar \"True\" si es verdadero y \"False\" si es\nfalso, a una variable al momento de declararla...\n\nPor ejemplo: \"x = true, y = false\"",
                                    font=("calibri", 11, "normal"),
                                    background="brown1",
                                    anchor="nw")
etiquetaTeoriaLogico.pack()
etiquetaTeoriaLogico.place(x=10, y=30, width=380, height=150)

etiquetaIntentoLogico = grupoK.Label(ventanaLogico,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="brown1",
                                     anchor="nw")
etiquetaIntentoLogico.pack()
etiquetaIntentoLogico.place(x=20, y=150, width=360, height=70)

# entradas

campoDeTextoLogico = grupoK.Entry(ventanaLogico,
                                  font=("calibri", 12),
                                  background="white"
                                  )
campoDeTextoLogico.pack()
campoDeTextoLogico.place(x=50, y=230, width=300, height=40)


# botones
boton_confirmar_logicos = grupoK.Button(ventanaLogico,
                                        text="Confirmar",
                                        command=funcion_confirmar_logicos)
boton_confirmar_logicos.pack()
boton_confirmar_logicos.place(x=80, y=300, width=100, height=30)

boton_volver_logicos = grupoK.Button(ventanaLogico,
                                     text="Volver",
                                     command=funcion_volver_logicos)
boton_volver_logicos.pack()
boton_volver_logicos.place(x=220, y=300, width=100, height=30)

# VENTANA CONDICIONALES
# ventana
ventanaCondicionales = grupoK.Tk()
ventanaCondicionales.title("Condicionales")
ventanaCondicionales.geometry("400x350+500+100")
ventanaCondicionales.resizable(width=False, height=False)
ventanaCondicionales.config(bg="aquamarine")
ventanaCondicionales.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
elegirCondic = grupoK.Label(ventanaCondicionales,
                            text="Elija el tipo de condicional que quiere aprender",
                            font=("calibri", 11, "bold"),
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
                                  text="Condicional Match Case ",
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
ventanaCondicionalSimple.geometry("410x450+500+100")
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

etiquetaTeoriaCondSimple = grupoK.Label(ventanaCondicionalSimple,
                                    text="Un condicional simple es cuando a la hora de \npresentar la elección tenemos la opción \nde realizar una actividad o no realizar ninguna. \nPara definirlo tiene que \ncolocarse un \"if\" acompañado con la \ncondicion que necesite y una accion.",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    anchor="nw")
etiquetaTeoriaCondSimple.pack()
etiquetaTeoriaCondSimple.place(x=30, y=30, width=360, height=150)

etiquetaTeoriaCondSimpleEj = grupoK.Label(ventanaCondicionalSimple,
                                    text="\tPor ejemplo: \n\"if (edad>18): \n\tprint(\"Es mayor de edad\")\"",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaCondSimpleEj.pack()
etiquetaTeoriaCondSimpleEj.place(x=50, y=170, width=360, height=200)

etiquetaIntentoCondSimple = grupoK.Label(ventanaCondicionalSimple,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="aquamarine",
                                     anchor="nw")
etiquetaIntentoCondSimple.pack()
etiquetaIntentoCondSimple.place(x=30, y=260, width=360, height=70)

# entradas
campoDeTextoCondSimple = grupoK.Text(ventanaCondicionalSimple,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoCondSimple.pack()
campoDeTextoCondSimple.place(x=20, y=320)
campoDeTextoCondSimple.config(width=37, 
                                height=3)

# botones
boton_confirmar_condSimple = grupoK.Button(ventanaCondicionalSimple,
                                           text="Confirmar",
                                           command=funcion_confirmar_cond_simple)
boton_confirmar_condSimple.pack()
boton_confirmar_condSimple.place(x=80, y=400, width=100, height=30)

boton_volver_condicional_simple = grupoK.Button(ventanaCondicionalSimple,
                                                text="Volver",
                                                command=funcion_volver_condicional_simple)
boton_volver_condicional_simple.pack()
boton_volver_condicional_simple.place(x=220, y=400, width=100, height=30)

# VENTANA CONDICIONAL ALTERNATIVO
# ventana
ventanaCondicionalAlternativo = grupoK.Tk()
ventanaCondicionalAlternativo.title("Condicional Alternativo")
ventanaCondicionalAlternativo.geometry("510x500+500+100")
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


etiquetaTeoriaCondAlter = grupoK.Label(ventanaCondicionalAlternativo,
                                    text="Un condicional alternativo es cuando a la hora \nde presentarse la elección tenemos la opción de realizar\n una actividad u otra. Para definirlo tiene que colocarse un\n \"if\" y un \"else\" acompañado con una condicion y dos acciones.",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    anchor="nw")
etiquetaTeoriaCondAlter.pack()
etiquetaTeoriaCondAlter.place(x=20, y=30, width=470, height=150)

etiquetaTeoriaCondAlterEj = grupoK.Label(ventanaCondicionalAlternativo,
                                    text="\tPor ejemplo: \n\"if (edad>18): \n\tprint(\"Es mayor de edad\") \n else: \n \tprint(\"Es menor de edad\")\"",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaCondAlterEj.pack()
etiquetaTeoriaCondAlterEj.place(x=90, y=130, width=360, height=250)

etiquetaIntentoCondAlter = grupoK.Label(ventanaCondicionalAlternativo,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="aquamarine",
                                     anchor="nw")
etiquetaIntentoCondAlter.pack()
etiquetaIntentoCondAlter.place(x=80, y=250, width=360, height=70)


# entradas
campoDeTextoCondAlter = grupoK.Text(ventanaCondicionalAlternativo,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoCondAlter.pack()
campoDeTextoCondAlter.place(x=70, y=320)
campoDeTextoCondAlter.config(width=37, 
                                height=4)

# botones
boton_confirmar_condAlter = grupoK.Button(ventanaCondicionalAlternativo,
                                          text="Confirmar",
                                          command=funcion_confirmar_cond_alternativo)
boton_confirmar_condAlter.pack()
boton_confirmar_condAlter.place(x=80, y=440, width=100, height=30)

boton_volver_condicional_alternativo = grupoK.Button(ventanaCondicionalAlternativo,
                                                     text="Volver",
                                                     command=funcion_volver_condicional_alternativo)
boton_volver_condicional_alternativo.pack()
boton_volver_condicional_alternativo.place(x=350, y=440, width=100, height=30)

# VENTANA CONDICIONAL ANIDADO
# ventana
ventanaCondicionalAnidado = grupoK.Tk()
ventanaCondicionalAnidado.title("Condicional Anidado")
ventanaCondicionalAnidado.geometry("550x570+500+100")
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

etiquetaTeoriaCondAnid = grupoK.Label(ventanaCondicionalAnidado,
                                    text="Una estructura condicional es anidada cuando por la \nrama del verdadero o el falso de una estructura condicional \nhay otra estructura condicional. Para definirla tiene\n que colocarse un nuevo \"if\" dentro de otro \"if\" o \"else\". ",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    anchor="nw")
etiquetaTeoriaCondAnid.pack()
etiquetaTeoriaCondAnid.place(x=40, y=30, width=470, height=150)

etiquetaTeoriaCondAnidEj = grupoK.Label(ventanaCondicionalAnidado,
                                    text="\t\tPor ejemplo: \n\"if (edad>=18): \n\tif (edad>18): \n\t\tprint(\"Ya entró en la etapa de juventud\") \n\telse: \n\t\tprint(\"Sigue en la etapa de adolescencia\") \n else: \n\tprint(\"Es menor de edad\")\"",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaCondAnidEj.pack()
etiquetaTeoriaCondAnidEj.place(x=45, y=130, width=460, height=350)

etiquetaIntentoCondAnid = grupoK.Label(ventanaCondicionalAnidado,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="aquamarine",
                                     anchor="nw")
etiquetaIntentoCondAnid.pack()
etiquetaIntentoCondAnid.place(x=90, y=310, width=360, height=70)

# entradas
campoDeTextoCondAnid = grupoK.Text(ventanaCondicionalAnidado,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoCondAnid.pack()
campoDeTextoCondAnid.place(x=15, y=380)
campoDeTextoCondAnid.config(width=51, 
                                height=7)

# botones
boton_confirmar_condAnid = grupoK.Button(ventanaCondicionalAnidado,
                                         text="Confirmar",
                                         command=funcion_confirmar_cond_anidado)
boton_confirmar_condAnid.pack()
boton_confirmar_condAnid.place(x=70, y=530, width=100, height=30)

boton_volver_condicional_anidado = grupoK.Button(ventanaCondicionalAnidado,
                                                 text="Volver",
                                                 command=funcion_volver_condicional_anidado)
boton_volver_condicional_anidado.pack()
boton_volver_condicional_anidado.place(x=350, y=530, width=100, height=30)

# VENTANA CONDICIONAL MATCH CASE
# ventana
ventanaCondicionalSwitchCase = grupoK.Tk()
ventanaCondicionalSwitchCase.title("Condicional Match Case")
ventanaCondicionalSwitchCase.geometry("650x700+400+100")
ventanaCondicionalSwitchCase.resizable(width=False, height=False)
ventanaCondicionalSwitchCase.config(bg="aquamarine")
ventanaCondicionalSwitchCase.protocol(
    "WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaCondMC = grupoK.Label(ventanaCondicionalSwitchCase,
                              text="Teoría sobre condicional match-case",
                              font=("calibri", 12, "bold"),
                              background="aquamarine")
etiquetaCondMC.pack()

etiquetaTeoriaCondMc = grupoK.Label(ventanaCondicionalSwitchCase,
                                text="El condicional match-case es una estructura que evalúa más de un caso y se \ncaracteriza por seleccionar una opción entre varias. Para definir un condicional \ntiene que colocarse un \"match\" acompañado de la variable que se va a comparar\n y varios \"case\" que son las distintas opciones y un \"case_\" que se usa cuando \nno es ninguna de las opciones.",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    anchor="nw")
etiquetaTeoriaCondMc.pack()
etiquetaTeoriaCondMc.place(x=20, y=30, width=620, height=400)

etiquetaTeoriaCondMcEj = grupoK.Label(ventanaCondicionalSwitchCase,
                                    text="\t\tPor ejemplo: \nmatch color: \n\tcase \"rojo\": \n\t\tprint(\"El color es rojo\") \n\tcase \"azul\": \n\t\tprint(\"El color es azul\") \n\tcase \"verde\": \n\t\tprint(\"El color es verde\") \n\tcase_: \n\t\tprint(\"No existe ese color\")",
                                    font=("calibri", 11, "normal"),
                                    background="aquamarine",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaCondMcEj.pack()
etiquetaTeoriaCondMcEj.place(x=150, y=150, width=360, height=350)

etiquetaIntentoMc = grupoK.Label(ventanaCondicionalSwitchCase,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="aquamarine",
                                     anchor="nw")
etiquetaIntentoMc.pack()
etiquetaIntentoMc.place(x=150, y=370, width=360, height=70)

# entradas
campoDeTextoCondMCase = grupoK.Text(ventanaCondicionalSwitchCase,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoCondMCase.pack()
campoDeTextoCondMCase.place(x=130, y=420)
campoDeTextoCondMCase.config(width=39, 
                                height=9)

# botones
boton_confirmar_condMC = grupoK.Button(ventanaCondicionalSwitchCase,
                                       text="Confirmar",
                                       command=funcion_confirmar_cond_switch_case)
boton_confirmar_condMC.pack()
boton_confirmar_condMC.place(x=140, y=630, width=100, height=30)

boton_volver_condicional_match_case = grupoK.Button(ventanaCondicionalSwitchCase,
                                                     text="Volver",
                                                     command=funcion_volver_condicional_switchCase)
boton_volver_condicional_match_case.pack()
boton_volver_condicional_match_case.place(x=420, y=630, width=100, height=30)

# VENTANA BUCLES
# ventana
ventanaBucles = grupoK.Tk()
ventanaBucles.title("Bucles")
ventanaBucles.geometry("400x350+500+100")
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

#botonDoWhile = grupoK.Button(ventanaBucles,
                             #text="Do-While",
                             #command=funcionDoWhile)
#botonDoWhile.pack()
#botonDoWhile.place(x=150, y=150, width=100, height=30)

botonVolverBucles = grupoK.Button(ventanaBucles,
                                  text="Volver",
                                  command=funcionVolverBucle)
botonVolverBucles.pack()
botonVolverBucles.place(x=150, y=150, width=100, height=30)

# VENTANA FOR
# ventana
ventanaFor = grupoK.Tk()
ventanaFor.title("For")
ventanaFor.geometry("450x500+500+100")
ventanaFor.resizable(width=False, height=False)
ventanaFor.config(bg="thistle1")
ventanaFor.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFor = grupoK.Label(ventanaFor,
                           text="Teoría sobre For",
                           font=("calibri", 12, "bold"),
                           background="thistle1")
etiquetaFor.pack()

etiquetaTeoriaFor = grupoK.Label(ventanaFor,
                                    text="El bucle For se utiliza para repetir una \no más instrucciones un determinado número de \nveces. Para definir un bucle For se tiene que colocar \nla palabra \"for\" seguida de un indice \npor ejemplo \"i\", seguido de la palabra \nreservada \"in\" y la funcion \"range\" \nque recibe como parametro un numero \ninicial y un numero final.",
                                    font=("calibri", 11, "normal"),
                                    background="thistle1",
                                    anchor="nw")
etiquetaTeoriaFor.pack()
etiquetaTeoriaFor.place(x=20, y=30, width=400, height=170)

etiquetaTeoriaForEj = grupoK.Label(ventanaFor,
                                    text="\tPor ejemplo: \nfor i in range(1, 11): \n\tprint(i)",
                                    font=("calibri", 11, "normal"),
                                    background="thistle1",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaForEj.pack()
etiquetaTeoriaForEj.place(x=90, y=210, width=360, height=200)

etiquetaIntentoFor = grupoK.Label(ventanaFor,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="thistle1",
                                     anchor="nw")
etiquetaIntentoFor.pack()
etiquetaIntentoFor.place(x=50, y=290, width=360, height=70)


# entradas
campoDeTextoFor = grupoK.Text(ventanaFor,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoFor.pack()
campoDeTextoFor.place(x=30, y=350)
campoDeTextoFor.config(width=37, 
                            height=3)

# botones
boton_confirmar_for = grupoK.Button(ventanaFor,
                                    text="Confirmar",
                                    command=funcion_confirmar_for)
boton_confirmar_for.pack()
boton_confirmar_for.place(x=80, y=450, width=100, height=30)

botonVolverFor = grupoK.Button(ventanaFor,
                               text="Volver",
                               command=funcionVolverFor)
botonVolverFor.pack()
botonVolverFor.place(x=250, y=450, width=100, height=30)

# VENTANA WHILE
# ventana
ventanaWhile = grupoK.Tk()
ventanaWhile.title("While")
ventanaWhile.geometry("500x500+500+100")
ventanaWhile.resizable(width=False, height=False)
ventanaWhile.config(bg="DarkSeaGreen1")
ventanaWhile.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaWhile = grupoK.Label(ventanaWhile,
                             text="Teoría sobre While",
                             font=("calibri", 12, "bold"),
                             background="DarkSeaGreen1")
etiquetaWhile.pack()

etiquetaTeoriaWhile= grupoK.Label(ventanaWhile,
                                    text="El bucle while evalúa una condición y luego ejecuta un \nbloque de código si la condición es verdadera. Para definir \nun bucle While se tiene que colocar la palabra \"while\" \ny luego la condicion, dentro de este bucle se tiene que colocar\n una accion para que el valor comparado avance y se pueda \nseguir ejecutando el bucle.",
                                    font=("calibri", 11, "normal"),
                                    background="DarkSeaGreen1",
                                    anchor="nw")
etiquetaTeoriaWhile.pack()
etiquetaTeoriaWhile.place(x=20, y=30, width=480, height=150)

etiquetaTeoriaWhileEj = grupoK.Label(ventanaWhile,
                                    text="\tPor ejemplo: \na = 1 \nwhile (a < 10): \n\tprint(\"¡Hola, mundo!\") \n\ta = a + 1",
                                    font=("calibri", 11, "normal"),
                                    background="DarkSeaGreen1",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaWhileEj.pack()
etiquetaTeoriaWhileEj.place(x=90, y=170, width=360, height=200)

etiquetaIntentoWhile = grupoK.Label(ventanaWhile,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="DarkSeaGreen1",
                                     anchor="nw")
etiquetaIntentoWhile.pack()
etiquetaIntentoWhile.place(x=70, y=290, width=360, height=70)

# entradas
campoDeTextoWhile = grupoK.Text(ventanaWhile,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoWhile.pack()
campoDeTextoWhile.place(x=60, y=350)
campoDeTextoWhile.config(width=37, 
                            height=4)

# botones
boton_confirmar_while = grupoK.Button(ventanaWhile,
                                      text="Confirmar",
                                      command=funcion_confirmar_while)
boton_confirmar_while.pack()
boton_confirmar_while.place(x=80, y=450, width=100, height=30)

botonVolverWhile = grupoK.Button(ventanaWhile,
                                 text="Volver",
                                 command=funcionVolverWhile)
botonVolverWhile.pack()
botonVolverWhile.place(x=320, y=450, width=100, height=30)

# VENTANA DO-WHILE
# ventana
#ventanaDoWhile = grupoK.Tk()
#ventanaDoWhile.title("Do-While")
#ventanaDoWhile.geometry("400x350+500+100")
#ventanaDoWhile.resizable(width=False, height=False)
#ventanaDoWhile.config(bg="powder blue")
#ventanaDoWhile.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
#etiquetaDoWhile = grupoK.Label(ventanaDoWhile,
                               #text="Teoría sobre Do-While",
                               #font=("calibri", 12, "bold"),
                               #background="powder blue")
#etiquetaDoWhile.pack()

# entradas
#campoDeTextoDoWhile = grupoK.Entry(ventanaDoWhile,
                                   #font=("calibri", 12),
                                   #background="white"
                                   #)
#campoDeTextoDoWhile.pack()
#campoDeTextoDoWhile.place(x=50, y=200, width=300, height=40)

# botones
#boton_confirmar_Dowhile = grupoK.Button(ventanaDoWhile,
                                        #text="Confirmar",
                                        #command=funcion_confirmar_Dowhile)
#boton_confirmar_Dowhile.pack()
#boton_confirmar_Dowhile.place(x=80, y=250, width=100, height=30)

#botonVolverDoWhile = grupoK.Button(ventanaDoWhile,
                                   #text="Volver",
                                   #command=funcionVolverDoWhile)
#botonVolverDoWhile.pack()
#botonVolverDoWhile.place(x=220, y=250, width=100, height=30)

# VENTANA ARREGLOS
# ventana
ventanaArreglos = grupoK.Tk()
ventanaArreglos.title("Arreglos")
ventanaArreglos.geometry("400x350+500+100")
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
ventanaVector.geometry("400x450+500+100")
ventanaVector.resizable(width=False, height=False)
ventanaVector.config(bg="dark salmon")
ventanaVector.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaVector = grupoK.Label(ventanaVector,
                              text="Teoría sobre Vectores",
                              font=("calibri", 12, "bold"),
                              background="dark salmon")
etiquetaVector.pack()

etiquetaTeoriaVector= grupoK.Label(ventanaVector,
                                    text="Un vector es una lista que se usa \npara almacenar multiples valores. \nPara definir un vector se crea una variable \ny entre \"[]\" se asignan los valores que se \nquieran almacenar separados por una \",\".",
                                    font=("calibri", 11, "normal"),
                                    background="dark salmon",
                                    anchor="nw")
etiquetaTeoriaVector.pack()
etiquetaTeoriaVector.place(x=40, y=30, width=360, height=150)

etiquetaTeoriaVectorEj = grupoK.Label(ventanaVector,
                                    text="\tPor ejemplo: \n m = [1,2,3,4]",
                                    font=("calibri", 11, "normal"),
                                    background="dark salmon",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaVectorEj.pack()
etiquetaTeoriaVectorEj.place(x=70, y=160, width=360, height=200)

etiquetaIntentoVector = grupoK.Label(ventanaVector,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="dark salmon",
                                     anchor="nw")
etiquetaIntentoVector.pack()
etiquetaIntentoVector.place(x=30, y=240, width=360, height=70)


# entradas
campoDeTextoVector = grupoK.Entry(ventanaVector,
                                  font=("calibri", 12),
                                  background="white"
                                  )
campoDeTextoVector.pack()
campoDeTextoVector.place(x=50, y=320, width=300, height=40)

# botones
boton_confirmar_vector = grupoK.Button(ventanaVector,
                                       text="Confirmar",
                                       command=funcion_confirmar_vector)
boton_confirmar_vector.pack()
boton_confirmar_vector.place(x=80, y=400, width=100, height=30)

botonVolverVector = grupoK.Button(ventanaVector,
                                  text="Volver",
                                  command=funcionVolverVector)
botonVolverVector.pack()
botonVolverVector.place(x=220, y=400, width=100, height=30)

# VENTANA MATRIZ
# ventana
ventanaMatriz = grupoK.Tk()
ventanaMatriz.title("Matrices")
ventanaMatriz.geometry("450x500+500+100")
ventanaMatriz.resizable(width=False, height=False)
ventanaMatriz.config(bg="DarkOliveGreen4")
ventanaMatriz.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaMatriz = grupoK.Label(ventanaMatriz,
                              text="Teoría sobre Matrices",
                              font=("calibri", 12, "bold"),
                              background="DarkOliveGreen4")
etiquetaMatriz.pack()

etiquetaTeoriaMatriz= grupoK.Label(ventanaMatriz,
                                    text="Una matriz es una estructura de datos bidimencional \ndonde los datos almacenados se organizan en \nfilas y columnas. Para definir una matriz\n se crea una variable, entre \"[]\" se colocan \notros \"[]\" que van a definir las filas \ny dentros de estos se almacenan los valores que \nquiere guardar, separador por \",\" \n que definirian las columnas.",
                                    font=("calibri", 11, "normal"),
                                    background="DarkOliveGreen4",
                                    anchor="nw")
etiquetaTeoriaMatriz.pack()
etiquetaTeoriaMatriz.place(x=15, y=30, width=400, height=180)

etiquetaTeoriaMatrizEj = grupoK.Label(ventanaMatriz,
                                    text="\tPor ejemplo: \n m = [[1,2],[3,4]]",
                                    font=("calibri", 11, "normal"),
                                    background="DarkOliveGreen4",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaMatrizEj.pack()
etiquetaTeoriaMatrizEj.place(x=100, y=220, width=360, height=200)

etiquetaIntentoMatriz = grupoK.Label(ventanaMatriz,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="DarkOliveGreen4",
                                     anchor="nw")
etiquetaIntentoMatriz.pack()
etiquetaIntentoMatriz.place(x=40, y=280, width=360, height=70)


# entradas
campoDeTextoMatriz = grupoK.Entry(ventanaMatriz,
                                  font=("calibri", 12),
                                  background="white"
                                  )
campoDeTextoMatriz.pack()
campoDeTextoMatriz.place(x=70, y=360, width=300, height=40)

# botones
boton_confirmar_matriz = grupoK.Button(ventanaMatriz,
                                       text="Confirmar",
                                       command=funcion_confirmar_matriz)
boton_confirmar_matriz.pack()
boton_confirmar_matriz.place(x=80, y=450, width=100, height=30)


botonVolverMatriz = grupoK.Button(ventanaMatriz,
                                  text="Volver",
                                  command=funcionVolverMatriz)
botonVolverMatriz.pack()
botonVolverMatriz.place(x=250, y=450, width=100, height=30)

# VENTANA MÉTODOS
# ventana
#ventanaMetodos = grupoK.Tk()
#ventanaMetodos.title("Métodos")
#ventanaMetodos.geometry("400x350+500+100")
#ventanaMetodos.resizable(width=False, height=False)
#ventanaMetodos.config(bg="orchid1")
#ventanaMetodos.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
#etiquetaMetodos = grupoK.Label(ventanaMetodos,
#                               text="Elegí una opción",
#                               font=("calibri", 12, "bold"),
#                               background="orchid1")
#etiquetaMetodos.pack()

# botones
#botonProcedimientos = grupoK.Button(ventanaMetodos,
                                    #text="Procedimientos",
                                    #command=funcion_procedimientos)
#botonProcedimientos.pack()
#botonProcedimientos.place(x=150, y=50, width=100, height=30)

#botonFunciones = grupoK.Button(ventanaMetodos,
#                               text="Funciones",
#                               command=funcion_funciones)
#botonFunciones.pack()
#botonFunciones.place(x=150, y=100, width=100, height=30)

#boton_volver_metodos = grupoK.Button(ventanaMetodos,
#                                     text="Volver",
#                                     command=funcion_volver_metodos)
#boton_volver_metodos.pack()
#boton_volver_metodos.place(x=150, y=150, width=100, height=30)

# VENTANA PROCEDIMIENTOS
# ventana
#ventanaProcedimientos = grupoK.Tk()
#ventanaProcedimientos.title("Procedimientos")
#ventanaProcedimientos.geometry("400x350+500+100")
#ventanaProcedimientos.resizable(width=False, height=False)
#ventanaProcedimientos.config(bg="orange")
#ventanaProcedimientos.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
#etiquetaProcedimientos = grupoK.Label(ventanaProcedimientos,
                                      #text="Teoría sobre procedimientos",
                                      #font=("calibri", 12, "bold"),
                                      #background="orange")
#etiquetaProcedimientos.pack()

#etiquetaTeoriaProcedimientos= grupoK.Label(ventanaProcedimientos,
                                    #text="No existen los procedimientos en Python",
                                    #font=("calibri", 11, "normal"),
                                    #background="orange",
                                    #anchor="nw")
#etiquetaTeoriaProcedimientos.pack()
#etiquetaTeoriaProcedimientos.place(x=40, y=30, width=360, height=150)

#etiquetaTeoriaProcedimientosEj = grupoK.Label(ventanaProcedimientos,
                                    #text="",
                                    #font=("calibri", 11, "normal"),
                                    #background="orange",
                                    #justify= "left",
                                    #anchor="nw")
#etiquetaTeoriaProcedimientosEj.pack()
#etiquetaTeoriaProcedimientosEj.place(x=50, y=160, width=360, height=200)

#etiquetaIntentoProcedimientos = grupoK.Label(ventanaProcedimientos,
                                     #text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     #font=("calibri", 11, "normal"),
                                     #background="orange",
                                     #anchor="nw")
#etiquetaIntentoProcedimientos.pack()
#etiquetaIntentoProcedimientos.place(x=30, y=270, width=360, height=70)

# entradas
#campoDeTextoProcedimientos = grupoK.Entry(ventanaProcedimientos,
                                          #font=("calibri", 12),
                                          #background="white"
                                          #)
#campoDeTextoProcedimientos.pack()
#campoDeTextoProcedimientos.place(x=50, y=200, width=300, height=40)

# botones
#boton_confirmar_procedimientos = grupoK.Button(ventanaProcedimientos,
                                               #text="Confirmar",
                                               #command=funcion_confirmar_procedimientos)
#boton_confirmar_procedimientos.pack()
#boton_confirmar_procedimientos.place(x=80, y=250, width=100, height=30)

#boton_volver_procedimientos = grupoK.Button(ventanaProcedimientos,
                                            #text="Volver",
                                            #command=funcion_volver_procedimientos)
#boton_volver_procedimientos.pack()
#boton_volver_procedimientos.place(x=220, y=250, width=100, height=30)

# VENTANA FUNCIONES
# ventana
ventanaFunciones = grupoK.Tk()
ventanaFunciones.title("Funciones")
ventanaFunciones.geometry("450x500+500+100")
ventanaFunciones.resizable(width=False, 
                            height=False)
ventanaFunciones.config(bg="red")
ventanaFunciones.protocol("WM_DELETE_WINDOW", salirProgramaDesdePrincipal)

# etiquetas
etiquetaFunciones = grupoK.Label(ventanaFunciones,
                                 text="Teoría sobre funciones",
                                 font=("calibri", 12, "bold"),
                                 background="red")
etiquetaFunciones.pack()

etiquetaTeoriaFunciones= grupoK.Label(ventanaFunciones,
                                    text="Las funciones son bloques de código que se \npueden reutilizar simplemente llamando a la función. \nSe definen con la palabra clave \"def\", seguida\ndel nombre de la función y, si tiene, sus parámetros.",
                                    font=("calibri", 11, "normal"),
                                    background="red",
                                    anchor="nw")
etiquetaTeoriaFunciones.pack()
etiquetaTeoriaFunciones.place(x=15, y=30, width=410, height=150)

etiquetaTeoriaFuncionesEj = grupoK.Label(ventanaFunciones,
                                    text="\tPor ejemplo: \ndef es_par(numero): \n\tif (numero % 2 == 0): \n\t\treturn True \n\telse: \n\t\treturn False",
                                    font=("calibri", 11, "normal"),
                                    background="red",
                                    justify= "left",
                                    anchor="nw")
etiquetaTeoriaFuncionesEj.pack()
etiquetaTeoriaFuncionesEj.place(x=80, y=130, width=360, height=200)

etiquetaIntentoFunciones = grupoK.Label(ventanaFunciones,
                                     text="¡Ahora intentalo tu!, ingresa el ejemplo anterior \nen el siguiente campo:",
                                     font=("calibri", 11, "normal"),
                                     background="red",
                                     anchor="nw")
etiquetaIntentoFunciones.pack()
etiquetaIntentoFunciones.place(x=50, y=270, width=360, height=70)

# entradas
campoDeTextoFunciones = grupoK.Text(ventanaFunciones,
                                      font=("calibri", 12),
                                      background="white")
campoDeTextoFunciones.pack()
campoDeTextoFunciones.place(x=30, y=320)
campoDeTextoFunciones.config(width=37, 
                                height=5)

# botones
# botones
boton_confirmar_funciones = grupoK.Button(ventanaFunciones,
                                          text="Confirmar",
                                          command=funcion_confirmar_funciones)
boton_confirmar_funciones.pack()
boton_confirmar_funciones.place(x=80, y=450, width=100, height=30)

boton_volver_funciones = grupoK.Button(ventanaFunciones,
                                       text="Volver",
                                       command=funcion_volver_metodos)
boton_volver_funciones.pack()
boton_volver_funciones.place(x=240, y=450, width=100, height=30)

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
#ventanaDoWhile.withdraw()
ventanaArreglos.withdraw()
ventanaVector.withdraw()
ventanaMatriz.withdraw()
#ventanaMetodos.withdraw()
#ventanaProcedimientos.withdraw()
ventanaFunciones.withdraw()
ventanaPrincipal.mainloop()
