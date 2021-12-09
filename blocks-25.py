import bplights
import time
import random


l = bplights.BPLights(300)
l.off()


chunks = 300 / 25

i = 0
r = [0] * 25
g = [0] * 25
b = [0]*25

for q in range(25):
    r[q] = q * 10
    g[q] = 240 - q * 10

while True:
    which = int(i % chunks)
    i = i + 1
    l.off()
    print(which, l.mapchunk(which))
    l.fillchunk(which, r, g, b)
    l.show()
    time.sleep(4)
