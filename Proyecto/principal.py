#imports
import tkinter as grupoK

#funciones
def funcion_aprender_variables():
    ventana = grupoK.Tk()

def funcion_aprender_condicionales():
    ventana = grupoK.Tk()

def funcion_aprender_bucles():
    ventana = grupoK.Tk()

def funcion_aprender_arreglos():
    ventana = grupoK.Tk()

def funcion_aprender_metodos():
    ventana = grupoK.Tk()

def funcion_volver():
    ventanaMenu.withdraw
    ventanaPrincipal.mainloop()
def abrirMenu():  
    ventanaPrincipal.withdraw
    ventanaMenu.mainloop()

#VENTANAS
#ventana principal
ventanaPrincipal = grupoK.Tk()
tituloVentanaPrincipal = "While(true): Aprender!"
ventanaPrincipal.title(tituloVentanaPrincipal)
ventanaPrincipal.geometry("400x400+500+50")
ventanaPrincipal.resizable(width=False, height=False)
ventanaPrincipal.config(bg= "LightGreen")
photo1 = grupoK.PhotoImage(file = "Proyecto/icono.png")
ventanaPrincipal.iconphoto(False, photo1)

#ventana menu
ventanaMenu = grupoK.Tk()
ventanaMenu.title("Menú de elección")
ventanaMenu.geometry("600x600+400+50")
ventanaMenu.resizable(width=False, height=False)
ventanaMenu.config(bg="SkyBlue")
#photo2 = grupoK.PhotoImage(file = "Proyecto/icono.png")
#ventanaMenu.iconphoto(False, photo2)

#ETIQUETAS
#etiquetas ventana principal
etiqueta_bienvenida = grupoK.Label(
    ventanaPrincipal,
    text="Bienvenido", 
    bg= "LightGreen",
    font="calibri")
etiqueta_bienvenida.pack()
etiqueta_bienvenida.place(x=150, y=10,  width=100, height=30)

#etiquetas ventana menu
cartel_opcion = grupoK.Label(ventanaMenu, 
    text="Elija el apartado al cual quiere ingresar")
cartel_opcion.pack()

#ENTRADAS
#entrada ventana principal
campoDeTextoPrincipal = grupoK.Entry(ventanaPrincipal,
    text="Ingresa tu nombre",
    font="calibri",
    background= "white")
campoDeTextoPrincipal.pack()
campoDeTextoPrincipal.place(x=100,y=100, width= 200, height= 30)

#BOTONES
#botones ventana principal
boton_menu_principal = grupoK.Button(
    ventanaPrincipal, 
    text="Menú",
    font="calibri",
    cursor="hand2",
    command= abrirMenu)
boton_menu_principal.pack()
boton_menu_principal.place(x=180, y=350, width=100, height=30)

boton_salir_principal = grupoK.Button(
    ventanaPrincipal, 
    text="Salir",
    font="calibri",
    cursor="hand2",
    command= exit)
boton_salir_principal.pack()
boton_salir_principal.place(x=290, y=350, width=100, height=30)

#botones ventana menu
boton_variables = grupoK.Button(
    ventanaMenu, text="Variables", command=funcion_aprender_variables)
boton_variables.pack()
boton_variables.place(x=250, y=50, width=100, height=30)
    
boton_condicionales = grupoK.Button(
    ventanaMenu, text="Condicionales", command=funcion_aprender_condicionales)
boton_condicionales.pack()
boton_condicionales.place(x=250, y=100, width=100, height=30)
    
boton_bucles = grupoK.Button(
    ventanaMenu, text="Bucles", command=funcion_aprender_bucles)
boton_bucles.pack()
boton_bucles.place(x=250, y=150, width=100, height=30)
    
boton_arreglos = grupoK.Button(
    ventanaMenu, text="Arreglos", command=funcion_aprender_arreglos)
boton_arreglos.pack()
boton_arreglos.place(x=250, y=200, width=100, height=30)
    
boton_metodos = grupoK.Button(
    ventanaMenu, text="Métodos", command=funcion_aprender_metodos)
boton_metodos.pack()
boton_metodos.place(x=250, y=250, width=100, height=30)
    
boton_volver = grupoK.Button(
    ventanaMenu, text="Volver", command=funcion_volver)
boton_volver.pack()
boton_volver.place(x=250, y=300, width=100, height=30)

#INICIO
ventanaPrincipal.mainloop()
