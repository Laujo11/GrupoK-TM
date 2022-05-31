import tkinter

ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.title("While(true): Aprender!")
ventanaPrincipal.geometry("400x600")
ventanaPrincipal.config(bg= "LightGreen")
photo = tkinter.PhotoImage(file = "C:/Users/maxim/Downloads/GrupoK-TM/Proyecto/icono.png")
ventanaPrincipal.iconphoto(False, photo)

etiqueta_bienvenida = tkinter.Label(
    ventanaPrincipal,text="Bienvenido", bg= "LightGreen")
etiqueta_bienvenida.pack()
etiqueta_bienvenida.place(x=150, y=10, width=100, height=30)


boton_menu_principal = tkinter.Button(
    ventanaPrincipal, text="Menú", command=abrirMenu)
boton_menu_principal.pack()
boton_menu_principal.place(x=150, y=60, width=100, height=30)

boton_salir_principal = tkinter.Button(
    ventanaPrincipal, text="Salir")
boton_salir_principal.pack()
boton_salir_principal.place(x=150, y=110, width=100, height=30)


ventanaPrincipal.mainloop()
