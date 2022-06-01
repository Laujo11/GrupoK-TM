#imports
import tkinter as interfaz
#import VentanaBienvenida
from metodos import funcion_aprender_variables

def abrirMenu():
    #VentanaBienvenida.ventanaPrincipal.withdraw()    
    
    ventanaMenu = interfaz.Tk()
    
    ventanaMenu.title("Menú de elección")
    
    ventanaMenu.geometry("600x600+400+50")
    
    ventanaMenu.resizable(width=False, height=False)
    
    ventanaMenu.config(bg="SkyBlue")
    
    cartel_opcion = interfaz.Label(
        ventanaMenu, text="Elija el apartado al cual quiere ingresar")
    cartel_opcion.pack()
    
    boton_variables = interfaz.Button(
        ventanaMenu, text="Variables", command=funcion_aprender_variables)
    boton_variables.pack()
    boton_variables.place(x=250, y=50, width=100, height=30)
    
    boton_condicionales = interfaz.Button(
        ventanaMenu, text="Condicionales", command=funcion_aprender_condicionales)
    boton_condicionales.pack()
    boton_condicionales.place(x=250, y=100, width=100, height=30)
    
    boton_bucles = interfaz.Button(
        ventanaMenu, text="Bucles", command=funcion_aprender_bucles)
    boton_bucles.pack()
    boton_bucles.place(x=250, y=150, width=100, height=30)
    
    boton_arreglos = interfaz.Button(
        ventanaMenu, text="Arreglos", command=funcion_aprender_arreglos)
    boton_arreglos.pack()
    boton_arreglos.place(x=250, y=200, width=100, height=30)
    
    boton_metodos = interfaz.Button(
        ventanaMenu, text="Métodos", command=funcion_aprender_metodos)
    boton_metodos.pack()
    boton_metodos.place(x=250, y=250, width=100, height=30)
    
    boton_volver = interfaz.Button(
        ventanaMenu, text="Volver", command=funcion_volver)
    boton_volver.pack()
    boton_volver.place(x=250, y=300, width=100, height=30)

    ventanaMenu.mainloop()
