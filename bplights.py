import time
import board
import neopixel
import sys
from rtmidi.midiutil import open_midiinput
from rtmidi import MidiIn
import math

class BPLights:
    def __init__(self, np) -> None:
        self.npixels = np


        self.pixel_pin = board.D18
        self.order = neopixel.RGB
    
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.npixels, 
            brightness=0.25, auto_write=False, pixel_order=self.order
        )

    def clmp(self, f):
        f = int(f)
        if (f<0):
            f = 0
        if (f>255):
            f = 255;
        return f

    def off(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def constant(self,r,g,b):
        self.pixels.fill((self.clmp(r), self.clmp(g), self.clmp(b)))
        self.pixels.show()

    def setval(self, i, r, g, b):
        self.pixels[i] = (self.clmp(r), self.clmp(g), self.clmp(b))

    def show(self):
        self.pixels.show()


class BPNanoKontrol:
    def __init__(self) -> None:
        try:
            self.midiin, self.port_name = open_midiinput(1)
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        print ("Connected to ", self.port_name)
        self.sliders = [0.0] * 9
        self.knobs = [0.0] * 9
        self.topbutton = [0.0] * 9
        self.bottombutton = [0.0] * 9

    def poll(self):
        msg = self.midiin.get_message()

        while msg:
            message, deltatime = msg
            ct = message[1]
            vl = message[2] / 127.0

            if (ct >= 50 and ct < 60):
                self.sliders[ct-50] = vl
            elif (ct >= 30 and ct < 40):
                self.bottombutton[ct-30] = vl
            elif (ct >= 20 and ct < 30):
                self.bottombutton[ct-20] = vl
            elif (ct >= 10 and ct < 20):
                self.knobs[ct - 10] = vl

            msg = self.midiin.get_message()
