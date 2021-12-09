import bplights
import time
import random


l = bplights.BPLights(300)
l.off()

idx = 0
while True:
   
    for i in range(10):
        v = (9-i)/10.0
        c = 120 * v
        l.setval((idx+i+1)%l.npixels, c, c, 0)
        l.setval((idx-i-1)%l.npixels, c, c, 0)
    l.setval(idx, 255,0,0)

    l.show()
    idx = (idx + 1) % l.npixels
    time.sleep(0.01)
