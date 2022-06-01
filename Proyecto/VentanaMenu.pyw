#imports
import tkinter

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
    boton_variables.place(x=250, y=50, width=100, height=30)
    
    boton_condicionales = tkinter.Button(
        ventanaMenu, text="Condicionales", command=funcion_aprender_condicionales)
    boton_condicionales.pack()
    boton_condicionales.place(x=250, y=100, width=100, height=30)
    
    boton_bucles = tkinter.Button(
        ventanaMenu, text="Bucles", command=funcion_aprender_bucles)
    boton_bucles.pack()
    boton_bucles.place(x=250, y=150, width=100, height=30)
    
    boton_arreglos = tkinter.Button(
        ventanaMenu, text="Arreglos", command=funcion_aprender_arreglos)
    boton_arreglos.pack()
    boton_arreglos.place(x=250, y=200, width=100, height=30)
    
    boton_metodos = tkinter.Button(
        ventanaMenu, text="Métodos", command=funcion_aprender_metodos)
    boton_metodos.pack()
    boton_metodos.place(x=250, y=250, width=100, height=30)
    
    boton_volver = tkinter.Button(
        ventanaMenu, text="Volver", command=funcion_volver)
    boton_volver.pack()
    boton_volver.place(x=250, y=300, width=100, height=30)

    ventanaMenu.mainloop()
