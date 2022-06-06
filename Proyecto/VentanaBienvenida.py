#imports
import tkinter as grupoK
from menu import abrirMenu

#ventanas
ventanaPrincipal = grupoK.Tk()
tituloVentanaPrincipal = "While(true): Aprender!"
ventanaPrincipal.title(tituloVentanaPrincipal)
ventanaPrincipal.geometry("400x400+500+50")
ventanaPrincipal.resizable(width=False, height=False)
ventanaPrincipal.config(bg= "LightGreen")
photo = grupoK.PhotoImage(file = "Proyecto/icono.png")
ventanaPrincipal.iconphoto(False, photo)

#etiquetas
etiqueta_bienvenida = grupoK.Label(
    ventanaPrincipal,
    text="Bienvenido", 
    bg= "LightGreen",
    font="calibri")
etiqueta_bienvenida.pack()
etiqueta_bienvenida.place(x=150, y=10,  width=100, height=30)

#campos de texto
campoDeTextoPrincipal = grupoK.Entry(ventanaPrincipal,
    text="Ingresa tu nombre",
    font="calibri",
    background= "white")
campoDeTextoPrincipal.pack()
campoDeTextoPrincipal.place(x=100,y=100, width= 200, height= 30)

#botones
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

#main
ventanaPrincipal.mainloop()
