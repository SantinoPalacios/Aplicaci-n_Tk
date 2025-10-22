import tkinter as tk




ventana = tk.Tk()
ventana.title('Nuestra primera app') # TITULO
ventana.geometry('200x300') # TAMAÑO DEL CUADRO
ventana.resizable(False,False)


etiqueta = tk.Label(ventana, text = 'Ingresar un nombre: ') # ETIQUETA PARA DECIR QUE HACER
etiqueta.pack()




entrada = tk.Entry(ventana) # PARA QUE EL USUARIO PUEDA INGRESAR ALGO EN LA ENTRADA
entrada.pack()




def saludar():
  nombre = entrada.get()
  etiqueta.config(text=f"Hola {nombre} ¿como estas?")




boton = tk.Button(ventana, text ="saludar", bg = "gold", command = saludar)
boton.pack()




segunda_etiqueta = tk.Label(ventana, text = "")
segunda_etiqueta.pack ()


ventana.mainloop()
