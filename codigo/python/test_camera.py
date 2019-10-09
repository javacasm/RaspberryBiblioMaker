from picamera import PiCamera

camera = PiCamera()
camera.resolution = (800, 480)
camera.hflip = True
camera.start_preview(alpha=128)
