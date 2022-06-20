from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cambiar_Nodo_Inicial(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Cambiar Nodo Inicial")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 250 // 2
        posicion = str(500) + "x" + str(250) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el nuevo NODO INICIAL:")
        lbl1.place(x=5,y=40)
        nuevoNodoInicial=Entry(self)
        nuevoNodoInicial.place(x=170,y=40)

        botonCreacion=Button(self,text="CAMBIAR NODO INICIAL",command=lambda:self.cambiarNodoInicial(nuevoNodoInicial.get(), controller, master)).place(x=330,y=70)

    def cambiarNodoInicial(self, nuevoNodoInicial, controller, master):
        if(not(nuevoNodoInicial.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nuevoNodoInicial)==""):
                messagebox.showwarning("Advertencia","Ingrese el NUEVO INICIAL por favor")
            else:
                bandera = controller.cambiarNodoInicial(int(nuevoNodoInicial))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","Ingrese unicamente un NODO VALIDO")
                else:
                    master.refrescarFigura(controller)
        self.destroy()
        self.update()