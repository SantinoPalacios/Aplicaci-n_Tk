import tkinter as tk


ventana = tk.Tk()
ventana.title("DrawingTime")
ventana.geometry('450x450')


et_etiqueta = tk.Label(ventana, text = 'Bienvenido/a')
et_etiqueta.pack()


et_usuario = tk.Label(ventana, text = "Ingresa nombre de usuario")
et_usuario.pack()


ingresar_usuario = tk.Entry(ventana)
ingresar_usuario.pack()


et_contrasenia = tk.Label(ventana, text = "Ingresa tu contraseña")
et_contrasenia.pack()


ingresar_contrasenia = tk.Entry(ventana)
ingresar_contrasenia.pack()

usuario_correcto = "Santino"
contrasenia_correcta = "123"

def iniciar_sesion():
   usuario = ingresar_usuario.get()
   constrasenia = ingresar_contrasenia.get()
   if usuario == usuario_correcto and constrasenia == contrasenia_correcta:
      segunda_etiqueta.config(text = f'Inicio de seción correctamente',bg = "black", fg = "cyan")
   else:
      segunda_etiqueta.config(text = f'la contraseña o el usuario estan incorrectos',bg = "black", fg= "red")

def salir():
   ventana.destroy()

exit = tk.Button(ventana, text = "Salir", bg = "black", fg = "yellow", command = salir)
boton = tk.Button(ventana, text = "Iniciar Sesión", bg = "cyan", command = iniciar_sesion)
boton.pack()


segunda_etiqueta = tk.Label(ventana)
segunda_etiqueta.pack()


ventana.mainloop()