#/usr/bin/env python

# Camera resolution is set to 320x240
# then the image is resize to 80x16
# then the zoom fonction ste it to 40x8
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

WIDTH = 80
HEIGHT = 16
numLEDs = WIDTH*HEIGHT

#initialize the camera and grab a reference to the raw camera capture
with picamera.PiCamera() as camera:

    resolution = (320, 240)
    camera.shutter_speed = 6000000
    camera.iso = 400
    camera.framerate = 20
    camera.led = True
    camera.capture(stream, format='rgb', resize=(WIDTH, HEIGHT), use_video_port=True)

    while True:
        with picamera.array.PiRGBArray(camera, size=(WIDTH, HEIGHT)) as stream:

            ###### AV GAUCHE  channel 0 -> TZXTQOUKWKVZDDUN
            camera.zoom = (0, 0, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            frameAVG = stream.array
            frameAVG = frameAVG.tolist()
            newFrameAVG = np.reshape(frameAVG, (numLEDs, 3))
            newFrameAVG = map(tuple, newFrameAVG)
            client.put_pixels(newFrameAVG, channel=0)

            ###### AV DROITE channel 1 -> UEICYSNDBXIHAJEV
            camera.zoom = (0.5, 0, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            frameAVD = stream.array
            frameAVD = frameAVD.tolist()
            newFrameAVD = np.reshape(frameAVD, (numLEDs, 3))
            newFrameAVD = map(tuple, newFrameAVD)
            client.put_pixels(newFrameAVD, channel=1)

            ###### AR GAUCHE channel 2 -> TXTXWEYKYITTRRYF
            camera.zoom = (0, 0.5, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            frameARG = stream.array
            frameARG = frameARG.tolist()
            newFrameARG = np.reshape(frameARG, (numLEDs, 3))
            newFrameARG = map(tuple, newFrameARG)
            client.put_pixels(newFrameARG, channel=2)

            ###### AR DROITE channel 3 -> TNFLPPXLBXELMHMT
            camera.zoom = (0.5, 0.5, 0.5, 0.5)
            stream.seek(0) # Rewind the stream for reading
            stream.truncate(0)
            frameARD = stream.array
            frameARD = frameARD.tolist()
            newFrameARD = np.reshape(frameARD, (numLEDs, 3))
            newFrameARD = map(tuple, newFrameARD)
            client.put_pixels(newFrameARD, channel=3)

            #print("DONE")