import bplights
import time
import random


l = bplights.BPLights(50)
l.off()

for i in range(100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    l.constant(r,g,b)
    time.sleep(1)