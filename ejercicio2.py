import tkinter as tk


ventana = tk.Tk()
ventana.title("DrawingTime")
ventana.geometry('450x450')
frame1 = tk.Frame(ventana, bg = "green",bd = 5, relief = "groove", width = "200", height = "300")
frame1.pack(pady=10)

et_etiqueta = tk.Label(frame1, text = 'Bienvenido/a')
et_etiqueta.pack(pady=10)


et_usuario = tk.Label(frame1, text = "Ingresa nombre de usuario")
et_usuario.pack(pady=10)


ingresar_usuario = tk.Entry(frame1)
ingresar_usuario.pack(pady=10)


et_contrasenia = tk.Label(frame1, text = "Ingresa tu contraseña")
et_contrasenia.pack(pady=10)


ingresar_contrasenia = tk.Entry(frame1)
ingresar_contrasenia.pack(pady=10)

usuario_correcto = "Santino"
contrasenia_correcta = "123"

def iniciar_sesion():
   usuario = ingresar_usuario.get()
   constrasenia = ingresar_contrasenia.get()
   if usuario == usuario_correcto and constrasenia == contrasenia_correcta:
      segunda_etiqueta.config(text = f'Inicio de seción correctamente',bg = "black", fg = "cyan")
   else:
      segunda_etiqueta.config(text = f'la contraseña o el usuario estan incorrectos',bg = "black", fg= "red")


boton = tk.Button(frame1, text = "Iniciar Sesión", bg = "cyan", command = iniciar_sesion)
boton.pack(pady=10)


segunda_etiqueta = tk.Label(ventana)
segunda_etiqueta.pack(pady=10)


ventana.mainloop()