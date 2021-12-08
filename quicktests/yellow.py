import time
import board
import neopixel

pixel_pin = board.D18
ORDER = neopixel.GRB
num_pixels = 50

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
for i in range(10000):
   for q in range(num_pixels):
      p = i + q
      c = 255 - (p * 4) % 255
      pixels[q%num_pixels] = (c,0,c) 
   pixels.show()
   time.sleep(0.02)

