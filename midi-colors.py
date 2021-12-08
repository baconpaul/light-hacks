import bplights
import time
import random


l = bplights.BPLights(50)
l.off()

m = bplights.BPNanoKontrol()

for i in range(10000):
    r = m.sliders[0] * 255
    g = m.sliders[1] * 255
    b = m.sliders[2] * 255

    l.constant(r,g,b)
    m.poll()
    time.sleep(0.02)