from datetime import datetime, timedelta
import  tkinter
ventana= tkinter.Tk()
ventana.geometry("400x300")

etiqueta_bienvenida= tkinter.Label(ventana,text="CALCULADORA DE FECHAS", bg= "red")
etiqueta_bienvenida.grid(row=0, column=1)
etiqueta_explicación=tkinter.Label(ventana, text="En esta aplicación podrás calcular el tiempo restante hasta la fecha que indiques.")
etiqueta_explicación.grid(row=1, column=1)
evento_importante= tkinter.Label(ventana,text="Introduce la fecha de un evento importante para ti en la siguiente caja de texto (DD/MM/YYY hh:mm:ss): ")
evento_importante.grid(row=2, column=1)
caja_de_texto= tkinter.Entry(ventana)
caja_de_texto.grid(row=3, column= 1)
respuesta= tkinter.Label(ventana)
respuesta.grid(row=3, column=3)
def saludo():
    texto= caja_de_texto.get()
    formato = "%d/%m/%Y %H:%M:%S"
    texto= datetime.strptime(texto, formato)
    fecha_actual = datetime.today()
    diferencia= texto - fecha_actual
    respuesta["text"]= f"El tiempo restante hasta la fecha indicada es: {diferencia}"
boton1 = tkinter.Button(ventana, text= "Presiona para que se haga la magia", command= saludo)
boton1.grid(row=4, column=1)

ventana.mainloop()