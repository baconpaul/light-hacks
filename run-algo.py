import bplights
from lightalgos import *
import sys

cn = sys.argv[1]
tn = float(sys.argv[2])

l = bplights.BPLights(300)
l.off()
k = globals()[cn]
s = k(l)
s.runfor(tn)