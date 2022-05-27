import tkinter

ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.title("While(true): Aprender!")
ventanaPrincipal.geometry("400x600")
ventanaPrincipal.config(bg= "LightGreen")
photo = tkinter.PhotoImage(file = "C:/Users/maxim/Downloads/GrupoK-TM/Proyecto/icono.png")
ventanaPrincipal.iconphoto(False, photo)

etiqueta_bienvenida = tkinter.Label(ventanaPrincipal,text="Bienvenido", bg= "lightgreen")
etiqueta_bienvenida.place(x=10, y=10, width= 100, height=30)
etiqueta_bienvenida.pack()

boton_continuar_principal = tkinter.Button(ventanaPrincipal, text= "Continuar")
boton_continuar_principal.place(x= 5, y= 565, width= 30, height= 30)
boton_continuar_principal.pack()
boton_salir_principal = tkinter.Button(ventanaPrincipal, text="Salir")
boton_salir_principal.place(x= 380, y= 580, width= 20, height= 20)
boton_salir_principal.pack()

ventanaPrincipal.mainloop()