import tkinter as tk
import subprocess

ventana = tk.Tk()
ventana.configure(bg='black',cursor="pirate")
ventana.geometry('400x600')
ventana.title('Proyecto 1 LFP')
ventana.resizable(0,0)

def analizar():
    subprocess.call(['python', 'prueba77.py'])

def generarArchivoJson():
    subprocess.call(['python', 'generarJson.py'])



def ventana_guardar():
    ventana2= tk.Toplevel(ventana)
    ventana2.configure(bg='black',cursor="pirate")
    ventana2.geometry('700x700')
    ventana2.title('Proyecto 1 LFP')
    ventana2.resizable(0,0)
    def guardar_archivo():
        contenido = texto.get("1.0", "end-1c")
        with open("archivo.txt", "w") as archivo:
            archivo.write(contenido)

    texto = tk.Text(ventana2,width=500,height=500)
    texto.place(x=250,y=40)

    scrollbar = tk.Scrollbar(ventana2)

    scrollbar.configure(command=texto.yview)
    texto.configure(yscrollcommand=scrollbar.set)

    scrollbar.place(x=200, y=40, height=200)
    texto.place(x=200, y=40, width=260, height=200)

    boton_guardar1=tk.Button(ventana2, text='Guardar', command=guardar_archivo)
    boton_guardar1.configure(bg='skyblue')
    boton_guardar1.place(x=50,y=40)

    boton_regresar = tk.Button(ventana2, text="Regresar", command=ventana.tkraise)
    boton_regresar.place(x=50,y=100)


    ventana2.mainloop



boton_analizar = tk.Button(ventana, text='Analizar', command=analizar, height=3, width=11)
boton_analizar.configure(bg='skyblue')
boton_analizar.place(x=50,y=270)

boton_guardar=tk.Button(ventana, text='Guardar', command=ventana_guardar, height=3, width=11)
boton_guardar.configure(bg='skyblue')
boton_guardar.place(x=50,y=50)

boton_abrir=tk.Button(ventana, text='Abrir', command=analizar, height=3, width=11)
boton_abrir.configure(bg='skyblue')
boton_abrir.place(x=50,y=150)

boton_errores=tk.Button(ventana, text='Errores', command=generarArchivoJson, height=3, width=11)
boton_errores.configure(bg='skyblue')
boton_errores.place(x=50,y=390)

boton_salir=tk.Button(ventana, text='Salir', command=analizar, height=3, width=11)
boton_salir.configure(bg='skyblue')
boton_salir.place(x=50,y=510)

boton_ayuda=tk.Button(ventana, text='Ayuda', command=analizar, height=3, width=11)
boton_ayuda.configure(bg='skyblue')
boton_ayuda.place(x=250,y=50)

boton_usuario=tk.Button(ventana, text='Manual de Usuario', command=analizar, height=3, width=11)
boton_usuario.configure(bg='skyblue')
boton_usuario.place(x=250,y=270)

boton_tecnico=tk.Button(ventana, text='Manual Técnico', command=analizar, height=3, width=11)
boton_tecnico.configure(bg='skyblue')
boton_tecnico.place(x=250,y=150)



ventana.mainloop()