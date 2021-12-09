import bplights
import time
import random


l = bplights.BPLights(300)
l.off()

cd = 0
while True:
    for q in range(l.chunks):
        for c in range(4):
            if (cd - c - 1 > 0):
                l.setchunk(q, cd-c - 1, 200 - 70 * c, 200-70*c, 200-70*c)
        l.setchunk(q, cd, 255, 255, 255)
    
    cd = (cd + 1) % l.chunklen
    l.show()
    time.sleep(0.1)
