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

    def off(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def constant(self,rgb):
        self.pixels.fill(rgb)
        self.pixels.show()