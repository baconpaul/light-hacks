# basically implement 'runfor' which runs for that many seconds
import time
import math
import random

class snowfall:
    def __init__(self, lights) -> None:
        self.lights = lights

    def runfor(self, seconds):
        l = self.lights
        dt = 0.1
        cd = 0
        ct = 0
        while ct * dt < seconds:
            ct = ct + 1
            for q in range(l.chunks):
                for c in range(4):
                    if (cd - c - 1 > 0):
                        l.setchunk(q, cd-c - 1, 200 - 70 * c, 200-70*c, 200-70*c)
                l.setchunk(q, cd, 255, 255, 255)
    
            cd = (cd + 1) % l.chunklen
            l.show()
            time.sleep(dt)

class smoothconstant:
    def __init__(self, lights) -> None:
        self.lights = lights
        self.r = 0
        self.g = 0
        self.b = 0
        self.rt = 0
        self.gt = 0
        self.bt = 0
        

    def runfor(self, seconds):
        l = self.lights
        dt = 0.1
        n = 50
        cd = 0
        ct = 0
        while ct * dt < seconds:
            along = ct % n
            if (along == 0):
                self.r = self.rt
                self.g = self.gt
                self.b = self.bt
                self.rt = random.randint(20,255)
                self.gt = random.randint(20,255)
                self.bt = random.randint(100,255)

            ct = ct + 1
            
            frac = along / n
            r = frac * self.rt + (1-frac) * self.r
            g = frac * self.gt + (1-frac) * self.g
            b = frac * self.bt + (1-frac) * self.b
            l.constant(r,g,b)
            l.show()
            time.sleep(dt)