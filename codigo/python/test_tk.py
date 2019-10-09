from Tkinter import*

from time import sleep
import picamera
WAIT_TIME = 30

camera = picamera.PiCamera() 
camera.resolution = (1024, 768)
for filename in camera.capture_continuous('/home/pi/time-lapse/img{timestamp:%H-%M-%S-%f}.jpg'):
        sleep(WAIT_TIME)


ventana=Tk()

# funciones que envian valor al puerto serie
# en funcion del boton pulsado
# para hacer parpadear el led de arduino
def dos():
    return

def cinco():
    return

def siete():
    return
# para cada boton se llama a las funciones anteriores
ventana.title("Comunicacion Raspberry Arduino")
Label(text="Escoge los parpadeos para Arduino", fg="#0A116B").pack()
Button(text="2 parpadeos", command=dos,background="#33D63B", fg="#FFFFFF").pack()
Button(text="5 parpadeos", command=cinco,background="#1DE4F2", fg="#FFFFFF").pack()
Button(text="7 parpadeos", command=siete,background="#DC0F16", fg="#FFFFFF").pack()

ventana.mainloop()
