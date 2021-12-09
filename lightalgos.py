# basically implement 'runfor' which runs for that many seconds
import time
import math
import random

allalgos = ["snowfall", "roundsweep", "smoothconstant", "downsweep", "swellandclear"]

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


class roundsweep:
    def __init__(self, lights) -> None:
        self.lights = lights

    def runfor(self, seconds):
        ct = 0
        slpt = 0.1
        i = 0
        r = [0] * 25
        g = [0] * 25
        b = [0]*25

        l = self.lights
       
        t = 0
        dt = 0.02
        tau =  2.0 * 3.14159268
        while ct * slpt < seconds:
            ct = ct + 1
            for which in range(l.chunks):
                fwhich = which * 1.0 / l.chunks
                s = math.sin(2 * tau * ( t + fwhich)) * 0.45 + 0.5

                for q in range(25):
                    r[q] = q * 10 * s
                    g[q] = (240 - q * 10) * s

                l.fillchunk(which, r, g, b)
            l.show()
            t = t + dt
            time.sleep(slpt)

class downsweep:
    def __init__(self, lights) -> None:
        self.lights = lights

    def runfor(self, seconds):
        ct = 0
        slpt = 0.1

        i = 0
        r = [0] * 25
        g = [0] * 25
        b = [0]*25

        l = self.lights

        t = 0
        dt = 0.07
        tau =  2.0 * 3.14159268
        while ct * slpt < seconds:
            ct = ct + 1
            for q in range(25):
                s = math.sin(tau * ( t + q / 25)) * 0.5 + 0.5

                r[q] = 180 * s + 40
                g[q] = 180 * s + 40
                b[q] = 220

            for which in range(l.chunks):
                l.fillchunk(which, r, g, b)

            l.show()
            t = t + dt
            time.sleep(slpt)
    

class swellandclear:
    def __init__(self, lights) -> None:
        self.lights = lights

    def runfor(self, seconds):
        ct = 0
        slpt = 0.1

        i = 0
        r = [0] * 25
        g = [0] * 25
        b = [0] * 25

        l = self.lights

        mode = 0  # 0 is swell 1 is clear
        swellOver = 50
        clearOver = 25
        sc = 0
        dc = 0
        
        while ct * slpt < seconds:
            ct = ct + 1

            if (mode == 0):
                if (sc == 0):
                    rt = random.randint(0,100)
                    gt = random.randint(0,100)
                    bt = random.randint(100,200)
                frac = 1.0 * sc / swellOver
                l.constant(rt * frac, gt * frac, bt * frac)
                sc = sc + 1
                if (sc == swellOver):
                    mode = 1
            if (mode == 1):
                sc = 0
                for c in range(l.chunks):
                    l.setchunk(c, dc, 255,255,255)
                    if (dc > 0):
                        l.setchunk(c,dc-1, 0,0,0)
                dc = dc + 1
                if (dc == 25):
                    dc = 0
                    sc = 0
                    mode = 0
            l.show()
            time.sleep(slpt)

       