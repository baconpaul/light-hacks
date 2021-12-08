import time
import board
import neopixel
import sys
from rtmidi.midiutil import open_midiinput
from rtmidi import MidiIn
import math


pixel_pin = board.D18
ORDER = neopixel.GRB
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.15, auto_write=False, pixel_order=ORDER
)

try:
    midiin, port_name = open_midiinput(1)
except (EOFError, KeyboardInterrupt):
    sys.exit()

rs = 1
bs = 1
gs = 1
ctr = 0.5

def clmp(f):
    r = int(f)
    if (r < 0 ):
        r = 0
    if (r > 255):
        r = 255
    return r

for i in range(10000):
    for q in range(num_pixels):
        cp = 1.0 * ((q+i) % num_pixels) / num_pixels
        qq = math.fabs(cp - ctr)
        
        # print (q, qq, ctr, cp)
        c = 255 - 255 * qq
        pixels[q%num_pixels] = (clmp(rs * c),clmp(bs * c), clmp(gs * c)) 
    pixels.show()

    msg = midiin.get_message()

    while msg:
        message, deltatime = msg
        ctrl = message[1]
        val = message[2] / 127.0
        if (ctrl == 50):
            rs = val
        if (ctrl == 51):
            bs = val
        if (ctrl == 52):
            gs = val
        if (ctrl == 10):
            ctr = message[2] / 127.0
        msg = midiin.get_message()

    time.sleep(0.05)