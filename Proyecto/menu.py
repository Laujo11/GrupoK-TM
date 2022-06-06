#imports
import tkinter as grupoK
from metodosMenu import funcion_aprender_variables
from metodosMenu import funcion_aprender_condicionales
from metodosMenu import funcion_aprender_bucles
from metodosMenu import funcion_aprender_arreglos
from metodosMenu import funcion_aprender_metodos
from metodosMenu import funcion_volver

def abrirMenu():
    #VentanaBienvenida.ventanaPrincipal.withdraw()    
    
    ventanaMenu = grupoK.Tk()
    
    ventanaMenu.title("Menú de elección")
    
    ventanaMenu.geometry("600x600+400+50")
    
    ventanaMenu.resizable(width=False, height=False)
    
    ventanaMenu.config(bg="SkyBlue")
    
    cartel_opcion = grupoK.Label(
        ventanaMenu, text="Elija el apartado al cual quiere ingresar")
    cartel_opcion.pack()
    
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

    ventanaMenu.mainloop()
