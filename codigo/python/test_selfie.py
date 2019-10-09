from gpiozero import Button
from picamera import PiCamera
from time import gmtime, strftime
from guizero import App, PushButton, Text, Picture



def next_overlay():
    print("Next overlay")
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)

def take_picture():
    print("Take a picture")
    camera = PiCamera()
    camera.resolution = (800, 480)
    camera.hflip = True
    camera.start_preview(alpha=128)
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)         # Add this line
    output_overlay(output, overlay) # Add this line

def new_picture():
    camera.start_preview(alpha=128)
    preview_overlay(camera, overlay)

output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())

next_overlay_btn = Button(23)
take_pic_btn = Button(25)

next_overlay_btn.when_pressed = next_overlay
take_pic_btn.when_pressed = take_picture


app = App("The All-Seeing Pi", 800, 480)
message = Text(app, "I spotted you!")
new_pic = PushButton(app, new_picture, text="New picture")
app.display()
