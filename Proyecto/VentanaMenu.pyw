def abrirMenu():
    ventanaPrincipal.withdraw()
    
    ventanaMenu = tkinter.Tk()
    
    ventanaMenu.title("Menú de elección")
    
    ventanaMenu.geometry("600x600+400+50")
    
    ventanaMenu.resizable(width=False, height=False)
    
    ventanaMenu.config(bg="SkyBlue")
    
    cartel_opcion = tkinter.Label(
        ventanaMenu, text="Elija el apartado al cual quiere ingresar")
    cartel_opcion.pack()
    
    boton_variables = tkinter.Button(
        ventanaMenu, text="Variables", command=funcion_aprender_variables)
    boton_variables.pack()
    
    boton_condicionales = tkinter.Button(
        ventanaMenu, text="Condicionales", command=funcion_aprender_condicionales)
    boton_condicionales.pack()
    
    boton_bucles = tkinter.Button(
        ventanaMenu, text="Bucles", command=funcion_aprender_bucles)
    boton_bucles.pack()
    
    boton_arreglos = tkinter.Button(
        ventanaMenu, text="Arreglos", command=funcion_aprender_arreglos)
    boton_arreglos.pack()
    
    boton_metodos = tkinter.Button(
        ventanaMenu, text="Métodos", command=funcion_aprender_metodos)
    boton_metodos.pack()
    
    boton_volver = tkinter.Button(
        ventanaMenu, text="Volver", command=funcion_volver)
    boton_volver.pack()
    
    ventanaMenu.mainloop()
