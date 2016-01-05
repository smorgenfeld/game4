#terrain.py

from graphics import *
from random import *

def terraingen(win,w,h):
    t = []
    land = []
    landcont = 0
    tt = []
    ttt = []
    for i in range(h):
        t.append([])
        tt.append([])
        ttt.append([])
        for j in range(w):
            tt[i].append([])
            ttt[i].append([])
            if i != 0:
                if j != 0:
                    r = randint(0,40)
                    if t[i][j-1] == 0 and t[i-1][j] == 0:
                        if j!=w-1 and  t[i-1][j-1] == 0 and (t[i-1][j+1]== 0) and r > 1 or r >= 1:
                            t[i].append(0)
                        else:
                            t[i].append(1)
                    if t[i][j-1] == 1 and t[i-1][j] == 1:
                        if j!=w-1 and  t[i-1][j-1] == 1 and (t[i-1][j+1]== 1) and r > 7 or r >= 1:
                            t[i].append(1)
                        else:
                            t[i].append(0)
                    if t[i][j-1] == 0 and t[i-1][j] == 1:
                        if r > 20:
                            t[i].append(0)
                        else:
                            t[i].append(1)
                    if t[i][j-1] == 1 and t[i-1][j] == 0:
                        if r > 20:
                            t[i].append(1)
                        else:
                            t[i].append(0)
                elif j == 0:
                    r = randint(0,10)
                    if t[i-1][j] == 0:
                        if r > 2:
                            t[i].append(0)
                        else:
                            t[i].append(1)
                    if t[i-1][j] == 1:
                        if r > 1:
                            t[i].append(1)
                        else:
                            t[i].append(0)
            elif i == 0:
                if j != 0:
                    r = randint(0,10)
                    if t[i][j-1] == 0:
                        if r > 2:
                            t[i].append(0)
                        else:
                            t[i].append(1)
                    if t[i][j-1] == 1:
                        if r > 1:
                            t[i].append(1)
                        else:
                            t[i].append(0)
                elif j == 0:
                    r = randint(0,1)
                    if r == 0:
                        t[i].append(0)
                    else:
                        t[i].append(1)
    for i in range(h):
        for j in range(w):
            for k in range(10):
                if j != 0 and j != w-1:
                    if i != 0 and i!=h-1:
                        t[i][j] = (t[i][j-1] + t[i][j+1] + t[i][j] + t[i+1][j-1]+t[i+1][j]+t[i+1][j+1] + t[i-1][j-1] + t[i-1][j]+t[i-1][j+1])/9
                    elif i == 0:
                        t[i][j] = (t[i][j-1] + t[i][j+1] + t[i][j] + t[i+1][j-1]+t[i+1][j]+t[i+1][j+1])/6
                    elif i == h-1:
                        t[i][j] = (t[i][j-1] + t[i][j+1] + t[i][j] + t[i-1][j-1] + t[i-1][j]+t[i-1][j+1])/6
                elif j == 0:
                    if i != 0 and i != h-1:
                        t[i][j] = (t[i][j+1] + t[i][j]+t[i+1][j]+t[i+1][j+1] + t[i-1][j]+t[i-1][j+1])/6
                    elif i == 0:
                        t[i][j] = (t[i][j+1] + t[i][j]+t[i+1][j]+t[i+1][j+1])/4
                    elif i == h-1:
                        t[i][j] = (t[i][j+1] + t[i][j] + t[i-1][j]+t[i-1][j+1])/4
                elif j == w-1:
                    if i != 0 and i != h-1:
                        t[i][j] = (t[i][j-1] + t[i][j]+t[i+1][j]+t[i+1][j-1] + t[i-1][j]+t[i-1][j-1])/6
                    elif i == 0:
                        t[i][j] = (t[i][j-1] + t[i][j]+t[i+1][j]+t[i+1][j-1])/4
                    elif i == h-1:
                        t[i][j] = (t[i][j-1] + t[i][j] + t[i-1][j]+t[i-1][j-1])/4
            land.append(Rectangle(Point(j,h-i),Point(j+1,h-1-i)))
            t[i][j],tt[i][j],ttt[i][j] = changeter(t[i][j],tt[i][j],0,0,land,landcont,i,w,h)
            land[landcont].setWidth(0)
            land[landcont].draw(win)
            landcont += 1
    return t,tt,ttt,land
def changeter(t,tt,tempmod,heightmod,land,landcont,i,w,h):
        if i < h/2:
            temp = i-(h/2)-randint(-3,3)+tempmod
        else:
            temp = (h/2)-i-randint(-3,3)+tempmod
        r = randint(0,6)
        if (t > .9999 and heightmod >= 0) or (t > .9999 - heightmod/9001 and heightmod < 0): #IT'S OVER 9000!!!!!
            tt = 'mont'
            if temp < -10:
                ttt = 'ice_m'
            elif temp > 10:
                ttt = 'desert_m'
            else:
                ttt = 'norm_m'
        elif t > .9 - heightmod/5:
            tt = 'hill'
            if temp < -40:
                ttt = 'ice_h'
            elif temp < -30:
                ttt = 'tundra_h'
            elif temp < -20:
                ttt = 'forest_h'
            elif temp < -10:
                ttt = 'grass_h'
            else:
                ttt = 'desert_h'
        elif t > .8 - heightmod/2:
            tt = 'plane'
            if temp < -40:
                ttt = 'ice_p'
            elif temp < -30:
                ttt = 'tundra_p'
            elif temp < -20:
                ttt = 'forest_p'
            elif temp < -10:
                ttt = 'grass_p'
            else:
                ttt = 'desert_p'
        elif t > .6 - heightmod:
            tt = 'beach'
            if temp < -40:
                ttt = 'ice_b'
            else:
                ttt = 'norm_b'
        elif t> .2 - heightmod:
            tt = 'ssea'
            if temp < -40:
                ttt = 'ice_ss'
            else:
                ttt = 'norm_ss'
        else:
            if temp < -40:
                ttt = 'ice_ds'
            else:
                ttt = 'norm_ds'
            tt = 'dsea'
        if tt == 'dsea':
            if ttt == 'ice_ds':
                land[landcont].setFill('white')
            elif ttt == 'norm_ds':
                land[landcont].setFill('#000066')
        elif tt == 'ssea':
            if ttt == 'ice_ss':
                land[landcont].setFill('#CCCCFF')
            elif ttt == 'norm_ss':
                land[landcont].setFill('#0066CC')
        elif tt == 'beach':
            if ttt == 'ice_b':
                land[landcont].setFill('#d3d3d3')
            elif ttt == 'norm_b':
                land[landcont].setFill('#FFFF66')
        elif tt == 'hill':
            if ttt == 'ice_h':
                land[landcont].setFill('#CCCCCC')
            elif ttt == 'tundra_h':
                land[landcont].setFill('#333300')
            elif ttt == 'forest_h':
                land[landcont].setFill('#003300')
            elif ttt == 'grass_h':
                land[landcont].setFill('#006600')
            elif ttt == 'desert_h':
                land[landcont].setFill('#CC9933')
        elif tt == 'plane':
            if ttt == 'ice_p':
                land[landcont].setFill('#FFFFCC')
            elif ttt == 'tundra_p':
                land[landcont].setFill('#666633')
            elif ttt == 'forest_p':
                land[landcont].setFill('#336600')
            elif ttt == 'grass_p':
                land[landcont].setFill('#339900')
            elif ttt == 'desert_p':
                land[landcont].setFill('#FFCC66')
        elif tt == 'mont':
            if ttt == 'ice_m':
                land[landcont].setFill('#999999')
            elif ttt == 'desert_m':
                land[landcont].setFill('#996600')
            elif ttt == 'norm_m':
                land[landcont].setFill('#333333')
        else:
            land[landcont].setFill('red')
        return t,tt,ttt
def getTiles(ttt,h):
    lol = []
    lool = []
    for i in range(h):
        lol.append(ttt[i].count('ice_ds'))#0
        lol.append(ttt[i].count('norm_ds'))#1
        lol.append(ttt[i].count('ice_ss'))#2
        lol.append(ttt[i].count('norm_ss'))#3
        lol.append(ttt[i].count('ice_b'))#4
        lol.append(ttt[i].count('norm_b'))#5
        lol.append(ttt[i].count('ice_h'))#6
        lol.append(ttt[i].count('tundra_h'))#7
        lol.append(ttt[i].count('forest_h'))#8
        lol.append(ttt[i].count('grass_h'))#9
        lol.append(ttt[i].count('desert_h'))#10
        lol.append(ttt[i].count('ice_p'))#11
        lol.append(ttt[i].count('tundra_p'))#12
        lol.append(ttt[i].count('forest_p'))#13
        lol.append(ttt[i].count('grass_p'))#14
        lol.append(ttt[i].count('desert_p'))#15
        lol.append(ttt[i].count('ice_m'))#16
        lol.append(ttt[i].count('desert_m'))#17
        lol.append(ttt[i].count('norm_m'))#18
    for j in range(19):
        lool.append(0)
        for i in range(h):
            lool[j] += lol[i*19+j]
    return lool
