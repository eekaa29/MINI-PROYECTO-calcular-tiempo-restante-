import tkinter

#1-crear ventana
ventana= tkinter.Tk()
ventana.geometry("400x300")
#2-crear etiqueta
etiqueta= tkinter.Label(ventana,text="Hola mundo", bg= "blue")
etiqueta.pack(fill= tkinter.X)#el comando pack sirve para hacer aparecer lo que estes creando en la ventana
#3-crear botones:
boton1 = tkinter.Button(ventana, text= "Presiona para que se haga la magia")
boton1.pack()
#4-darle utilidad a los botones:
def saludo():
    print("Hola Rakel, que tal estas?")
boton2 = tkinter.Button(ventana, text= "Presiona para que se haga la magia", command=saludo)#IMPORTANTE, hay que poner el nombre de la funcion 
#sin parentesis, porque sino se ejecuta antes de que le demos al boton y no tendría sentido.
boton2.pack()
#5-FUNCION INTERACTIVA(USANDO LAMBDA):
def saludo(nombre):
    print(f"Hola, {nombre}, ¿que tal estás?")

boton3= tkinter.Button(ventana, text= "Presiona para ver la magia", command= lambda: saludo("Rakel"))
boton3.pack()

#6-JUGANDO CON ETIQUETAS:
caja_de_texto= tkinter.Entry(ventana)
caja_de_texto.pack()
etiqueta2= tkinter.Label(ventana)
etiqueta2.pack()
def saludo():
    texto= caja_de_texto.get()
    etiqueta2["text"]= texto
boton3 = tkinter.Button(ventana, text= "Presiona para que se haga la magia", command= saludo)
boton3.pack()

ventana.mainloop()

ventana.mainloop()#esto hay que ponerlo simpre al final cuando se esté usando tkinter.
