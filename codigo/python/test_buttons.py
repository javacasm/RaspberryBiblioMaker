from gpiozero import Button
button23 = Button(23)
button25 = Button(22)

button23.wait_for_press()
print('You pushed 23 button')

button25.wait_for_press()
print('You pushed 25 button')

