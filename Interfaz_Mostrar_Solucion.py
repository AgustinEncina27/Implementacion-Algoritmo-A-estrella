from tkinter import *
from tkinter import messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Mostrar_Solucion(tk.Frame):
    #Constructor de Mostrar_Solución
    def __init__(self, parent,controller):
        super().__init__(parent)
        ancho_ventana = 1200
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Boton
        self.botonSolucionFinal=Button(text="MOSTRAR SOLUCIÓN FINAL",command=lambda:[self.mostrarSolucionTotal(controller),self.botonSiguiente.place_forget()])
        self.botonSolucionFinal.place(x=450,y=440)
        self.botonSiguiente=Button(text="SIGUIENTE PASO",command=lambda:self.mostrarSolucionParcial(controller))
        self.botonSiguiente.place(x=740,y=440)
        
        
        
        controller.cargarDatosIniciales()
        controller.iniciarSolucionParcial()
        T = tk.Text(self, height = 30, width = 36)
        T.place(x=900,y=0)
        T.insert(tk.END, controller.mostrarTextoSolucion())
        f=controller.mostrarSolucionTotal()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=400,y=0)
       
    #Obtiene el controlador
    def set_controller(self, controller):
        self.controller = controller
    
    #Muestra el arbol con la solucion final, el texto con todas las iteraciones y los valores que se encuentran en las listas ABIERTA Y CERRADA
    def mostrarSolucionTotal(self,controller):
        z=controller.iniciarSolucionTotal()
        if(z==0):
            self.botonSiguiente.place_forget()
            self.botonSolucionFinal.place_forget()
            messagebox.showwarning("Advertencia","Se encontró la solución")
            T = tk.Text(self, height = 30, width = 36)
            T.place(x=900,y=0)
            T.insert(tk.END, controller.mostrarTextoSolucion())
            f=controller.mostrarSolucionTotal()
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=400,y=0)
        else:
            if(z==1):
                self.botonSiguiente.place_forget()
                self.botonSolucionFinal.place_forget()
                messagebox.showwarning("Advertencia","No se encontró la solución")

    #Muestra el arbol que se genera paso a paso, con los valores que se encuentran en las listas ABIERTA Y CERRADA
    def mostrarSolucionParcial(self,controller):
        z=controller.iniciarSolucionParcial()
        if(z==0):
            self.botonSiguiente.place_forget()
            self.botonSolucionFinal.place_forget()
            messagebox.showwarning("Advertencia","Se encontró la solución")
            f=controller.mostrarSolucionTotal()
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=400,y=0)
        else:
            if(z==2):
                messagebox.showwarning("Advertencia","No se encontró la solución")
            else:
                f=controller.mostrarSolucionTotal()
                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().place(x=400,y=0)
        T = tk.Text(self, height = 30, width = 36)
        T.place(x=900,y=0)
        T.insert(tk.END, controller.mostrarTextoSolucion())
            

