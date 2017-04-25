#/usr/bin/env python

# Scale to 80/59
# croped to 40/8
# config file : /usr/local/bin/fcserver.json 

import opc
import time
import picamera
import picamera.array
import numpy as np

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)

if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
    print('WARNING: could not connect to %s' % ADDRESS)

WIDTH = 40
HEIGHT = 8
numLEDs = WIDTH*HEIGHT


#initialize the camera and grab a reference to the raw camera capture
with picamera.PiCamera() as camera:

    #camera.stop_preview()
    resolution = (320, 240)
    camera.shutter_speed = 6000000
    camera.iso = 400
    camera.framerate = 20
    camera.led = True
    #camera.contrast = 2
    #camera.brightness = 40
    #print "Setup done"
    #camera.start_preview()
    #print "Start preview"

    while True:
        with picamera.array.PiRGBArray(camera, size=(WIDTH, HEIGHT)) as stream:

            ###### AV GAUCHE  channel 0 -> TXTXWEYKYITTRRYF
            camera.zoom = (0, 0, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            camera.capture(stream, format='rgb', resize=(WIDTH, HEIGHT), use_video_port=True)
            frameAVG = stream.array
            frameAVG = frameAVG.tolist()
            newFrameAVG = np.reshape(frameAVG, (numLEDs, 3))
            newFrameAVG = map(tuple, newFrameAVG)
            client.put_pixels(newFrameAVG, channel=0)
            
            ###### AV DROITE channel 1 -> UEICYSNDBXIHAJEV
            camera.zoom = (0.5, 0, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            camera.capture(stream, format='rgb', resize=(WIDTH, HEIGHT), use_video_port=True)
            frameAVD = stream.array
            frameAVD = frameAVD.tolist()
            newFrameAVD = np.reshape(frameAVD, (numLEDs, 3))
            newFrameAVD = map(tuple, newFrameAVD)
            client.put_pixels(newFrameAVD, channel=1)
            
            ###### AR GAUCHE channel 2 -> TXTXWEYKYITTRRYF
            camera.zoom = (0, 0.5, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            camera.capture(stream, format='rgb', resize=(WIDTH, HEIGHT), use_video_port=True)
            frameARG = stream.array
            frameARG = frameARG.tolist()
            newFrameARG = np.reshape(frameARG, (numLEDs, 3))
            newFrameARG = map(tuple, newFrameARG)
            client.put_pixels(newFrameARG, channel=2)
            
            ###### AR DROITE channel 3 -> TZXTQOUKWKVZDDUN
            camera.zoom = (0.5, 0.5, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            camera.capture(stream, format='rgb', resize=(WIDTH, HEIGHT), use_video_port=True)
            frameARD = stream.array
            frameARD = frameARD.tolist()
            newFrameARD = np.reshape(frameARD, (numLEDs, 3))
            newFrameARD = map(tuple, newFrameARD)
            client.put_pixels(newFrameARD, channel=3)

            #print("DONE")
