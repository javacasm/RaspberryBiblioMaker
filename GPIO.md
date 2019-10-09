# Curso Raspberry Pi Basico

## CEP Priego-Montilla

Abril 2019

![CC](./images/Licencia_CC.png)

## José Antonio Vacas  @javacasm

## [https://github.com/javacasm/RaspberryPriego](https://github.com/javacasm/RaspberryPriego)

## GPIO

Vamos a describir las posibilidades de conexión de RaspBerry. Este artículo forma parte de un <a href="http://cevug.ugr.es/raspberry_pi">curso online de Raspberry</a> que imparto (próxima edición en octubre de 2014).

Por medio del  conector situado junto a la tarjeta SD podemos acceder a los GPIO o pines de entrada/salida.

<img class="alignleft" style="margin-left: 20px; margin-right: 20px;" title="Conector GPIO" src="https://learn.adafruit.com/system/guides/images/000/000/166/medium800/gpio.jpg?1396720373" alt="" width="350" />

Desde el GPIO, entradas/salidas de propósito general (General Porpouse Inputs/Outputs)  podremos hacer varias cosas:

<ul>
    <li>Encender apagar LEDs (no podemos aspirar a encender nada de mayor potencia directamente). Estas son las salidas digitales, capaces de estar en estado alto o bajo. Algunos de estos pines pueden generar PWM (modulación por ancho de pulso), algo parecido a una modulación de la potencia o PPM (modulación por posición de pulso), protocolo que usan los servos.</li>
    <li>Detectar pulsaciones de botones/interruptores. Estas son las entradas digitales.</li>
    <li>Acceso al puerto serie por los terminales TX/TX</li>
    <li>Acceso al bus I2C, bus de comunicaciones usado por muchos dispositivos</li>
    <li>Acceso al bus SPI, bus de comunicaciones similar al I2C pero con diferentes especificaciones</li>
</ul>

Podemos ver los pines de este conector en el siguiente esquema de adafruit

<p style="text-align: center;"><img class="aligncenter" title="conector" src="https://learn.adafruit.com/system/assets/assets/000/003/059/medium800/learn_raspberry_pi_gpio-srm.png?1396790782" alt="" width="500" /></p>

También están disponibles las líneas de alimentación de 5v y 3.3v y por supuesto tierra.

Todos los pines se pueden configurar tanto de entrada como de salida.

Algunos de los pines tienen una segunda función como por ejemplo los etiquetados como SCL y SDA utilizados para I2C y los MOSI, MISO y SCKL utilizados para conectar con dispositivos SPI.

Hay que tener muy claro que todos los pines usan niveles lógicos de 3.3V y no es seguro conectarlos directamente a 5V, porque las entradas han de ser menores de 3.3V. Igualmente no podemos esperar salidas superiores a 3.3V. En caso de querer conectar con lógica de 5v tendremos que usar una electrónica para adaptar niveles.


Veamos ahora un programa de ejemplo que manipula los GPIO

	import RPi.GPIO as GPIO
	# Usamos la numeración de los GPIO no el numero de los pines
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(7, GPIO.IN) # establecemos el GPIO 7 como entrada
	GPIO.setup(8, GPIO.OUT) # establecemos el GPIO 8 como salida
	input_value = GPIO.input(7) # recuperamos el valor de entreda
	GPIO.output(8, True) # establecemos la salida en alto


Veamos un ejemplo más avanzado

	import RPi.GPIO as GPIO
	import time
	# Usamos la posición en el conector
	GPIO.setmode(GPIO.BOARD)
	# pin 11 (GPIO17) como output
	GPIO.setup(11, GPIO.OUT)
	var=1
	print "Empezamos el bucle infinito"
	while var==1 :
	print "Output False"
	GPIO.output(11, False)
	time.sleep(1) # esperamos un tiempo
	print "Output True"
	GPIO.output(11, True)
	time.sleep(1)
