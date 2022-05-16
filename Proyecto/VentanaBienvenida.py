import tkinter

ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.title("While(true): Aprender!")
ventanaPrincipal.geometry("500x500")
ventanaPrincipal.resizable(False, False)
ventanaPrincipal.config(bg= "LightGreen")
photo = tkinter.PhotoImage(file = "C:/Users/maxim/Downloads/GrupoK-TM/Proyecto/icono.ICO")
ventanaPrincipal.iconphoto(False, photo)

ventanaPrincipal.mainloop()