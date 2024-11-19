from datetime import datetime, timedelta

'''
Crear un script en Python que calcule el tiempo que falta para la fecha de tu próximo evento importante (puede ser el fin de las vacaciones, tu cumpleaños, o cualquier otra fecha especial).

El reto consiste en:
Solicitar la fecha del evento al usuario. Puede ser ingresada en cualquier formato común (dd/mm/aaaa o mm/dd/aaaa).
Calcular la diferencia de tiempo entre la fecha actual y la fecha del evento.
Mostrar el resultado en días, horas, minutos y segundos que faltan para el evento.

Bonus:
Añadir validación de la entrada del usuario.
Crear una pequeña interfaz gráfica utilizando Tkinter para hacer la experiencia más interactiva.
Utilizar la libreria datetime
'''
try:
    evento_importante= (input("Introduce la fecha de un evento importante (DD/MM/YYY hh:mm:ss): "))#10/1/2025 18:40:30
    formato = "%d/%m/%Y %H:%M:%S"
    evento_importante= datetime.strptime(evento_importante, formato)
    fecha_actual = datetime.today()
    diferencia= evento_importante - fecha_actual
    print(diferencia)
except Exception:
    print("FORMATO DE FECHA MAL INTRODUCIDO, VUELVA A INTENTARLO POR FAVOR.")












