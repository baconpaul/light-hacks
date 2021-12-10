# basically implement 'runfor' which runs for that many seconds
import time
import math
import random

allalgos = ["snowfall", "roundsweep", "smoothconstant", 
            "snake", "downsweep", "swellandclear", "burst", "candycane"]

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

       
class snake:
    def __init__(self, lights) -> None:
        self.lights = lights

    def runfor(self, seconds):
        ct = 0
        slpt = 0.1

        l = self.lights
        l.off()
        
        while ct * slpt < seconds:
            for i in range(20):
                frac = i/19
                q = (ct + i) % l.npixels
                l.setval(q,frac*100,frac*100,frac*255)
            
            for i in range(10):
                frac = i/9
                q = (ct + i + 100) % l.npixels
                l.setval(q,frac*250,frac*140,frac*0)
            
            for i in range(15):
                frac = i/14
                q = (ct + i + 200) % l.npixels
                l.setval(q,frac*0,frac*240,frac*0)
            
            ct = ct + 1
            l.show()
            time.sleep(slpt)

class burst:
    def __init__(self, lights) -> None:
        self.lights = lights
        self.grid = []
        self.ngrid = []
        for i in range(12):
            q = []
            v = []
            for j in range(25):
                q.append([0,0,0])
                v.append([0,0,0])
            self.grid.append(q)
            self.ngrid.append(v)
        
    def runfor(self, seconds):
        ct = 0
        slpt = 0.1

        l = self.lights
        l.off()

        tdiff = 0.97
        ndiff = 0.8
        
        while ct * slpt < seconds:
            if (random.randint(0,50) > 20):
                ir = random.randint(0,11)
                jr = random.randint(0,24)
                if (random.randint(0,8) > 5):
                    self.grid[ir][jr][0] = 255
                    self.grid[ir][jr][1] = 100
                    self.grid[ir][jr][2] = 100
                else:
                    self.grid[ir][jr][2] = random.randint(100,255)
                    self.grid[ir][jr][1] = random.randint(100,150)
                    self.grid[ir][jr][0] = self.grid[ir][jr][1]

            for i in range(12):
                ip1 = (i+12+1)%12
                im1 = (i+12-1)%12
                for j in range(25):
                    jp1 = (i+25+1)%25
                    jm1 = (j+25-1)%25
                    for k in range(3):
                        avg = self.grid[ip1][j][k] + self.grid[im1][j][k] + self.grid[i][jp1][k] + self.grid[i][jm1][k]
                        avg = avg * 0.25
                        nv = self.grid[i][j][k] * ndiff + avg * (1-ndiff)
                        
                        self.ngrid[i][j][k] = nv * tdiff

            self.grid = self.ngrid.copy()
           
            for i in range(12):
                for j in range(25):
                    l.setchunk(i, j, self.grid[i][j][0], self.grid[i][j][1], self.ngrid[i][j][2])


            ct = ct + 1
            l.show()
            time.sleep(slpt)


class candycane:
    def __init__(self, lights) -> None:
        self.lights = lights
         
    def runfor(self, seconds):
        ct = 8
        slpt = 0.1

        l = self.lights
        
        sh = 0
        dsh = 0.2716
        while ct * slpt < seconds:
            ct = ct + 1

            wrote = []
            for i in range(12):
                wrote.append([])
                for j in range(25):
                    wrote[i].append(False)

            for c in range(12):
                for q in range(25):
                    (fr,i) = math.modf(sh)
                    if (int(q+sh)%12 == c):  
                        wrote[c][q] = True
                        l.setchunk(c,q,255,0,0)
                        fr = 1 - fr
                        if (q+1 < 25):
                            wrote[c][q+1] = True
                            l.setchunk(c,q+1,255*fr+120*(1-fr),120*(1-fr),120*(1-fr))
                        fr = 1 - fr
                        if (q-1 >0):
                            wrote[c][q-1] = True
                            l.setchunk(c,q-1,255*fr+120*(1-fr),120*(1-fr),120*(1-fr))


            for c in range(12):
                for q in range(25):
                    if (not wrote[c][q]):
                        l.setchunk(c,q,120,120,120)         
            l.show()
            sh = sh + dsh
            time.sleep(slpt) 