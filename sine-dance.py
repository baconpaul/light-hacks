import bplights
import time
import random
import math


l = bplights.BPLights(50)
l.off()

m = bplights.BPNanoKontrol()

dq = math.pi * 2.0 / l.npixels
dt = 0.1
t = 0

for i in range(10000):
    t = t + dt
    if  (t > 2 * math.pi):
        t = t - 2 * math.pi
    
    dt = 0.005 + 0.3 * m.knobs[0]
    
    for q in range(l.npixels):
        vt = q * dq + t
        s = (math.sin(vt) + 1) * 0.5

        r = m.sliders[0] * 255 * s
        g = m.sliders[1] * 255 * s
        b = m.sliders[2] * 255 * s

        l.setval(q, r, g, b)
    l.show()
    m.poll()
    time.sleep(0.02)