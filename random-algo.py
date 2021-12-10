import sys
sys.path.append("/home/pi/light-hacks")

import bplights
from lightalgos import *
import time
import random


l = bplights.BPLights(300)
l.off()

lastalgo = -1
while True:
    r = random.randint(0, len(allalgos)-1)
    if (r != lastalgo):
        algo = allalgos[r]
        k = globals()[algo]
        s = k(l)
        s.runfor(60)
    lastalgo = r   
   
