import bplights
from lightalgos import *
import sys
import time
import random


l = bplights.BPLights(300)
l.off()

while True:
    r = random.randint(0, len(allalgos)-1)
    algo = allalgos[r]
    print( "Running " , algo )
    k = globals()[algo]
    s = k(l)
    s.runfor(60)