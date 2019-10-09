# http://gpiozero.readthedocs.io/en/stable/api_output.html#servo

from gpiozero import Servo
from time import sleep

servoVertical = 19
servoHorizontal = 17


servo = Servo( servoHorizontal )
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
