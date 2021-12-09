import bplights
import time
import math


l = bplights.BPLights(300)
l.off()


chunks = 300 / 25

i = 0
r = [0] * 25
g = [0] * 25
b = [0]*25


t = 0
dt = 0.02
tau =  2.0 * 3.14159268
while True:
    for which in range(l.chunks):
        fwhich = which * 1.0 / l.chunks
        s = math.sin(2 * tau * ( t + fwhich)) * 0.45 + 0.5


        for q in range(25):
            r[q] = q * 10 * s
            g[q] = (240 - q * 10) * s

        l.fillchunk(which, r, g, b)
    l.show()
    t = t + dt
    time.sleep(0.1)
