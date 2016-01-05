#cell.py
from graphics import *
import random, time

def cell(win,w,h):
    w = w//2
    h = h//2
    backdrop = Rectangle(Point(0,0),Point(1920,1080))
    backdrop.setFill('lightgrey');backdrop.setWidth(0);backdrop.draw(win)
    load = Text(Point(w,h),'Loading...')
    load.setSize(36);load.draw(win)
    win.update()
    cells = []
    a = []
    for i in range(h):
        cells.append([])
        a.append([])
        for j in range(w):
            cells[i].append(Rectangle(Point(j*2,h*2-i*2),Point(j*2+2,h*2-2-i*2)))
            cells[i][j].setFill('white');cells[i][j].setWidth(0);cells[i][j].draw(win)
            if random.randint(0,1):
                a[i].append(1)
            else:
                a[i].append(0)
    load.undraw()
    win.update()
    #ti = time.time()
    while True:
        keey = win.checkKey()
        if keey == 'r':
            for i in range(40):
                randw = random.randint(0,w-1)
                randh = random.randint(0,h-1)
                a[randh][randw] = 1
                cells[randh][randw].setFill('green')
        elif keey == 'q':
            break
        elif keey == 's':
            shop(win,w,h)
        elif keey == 'p':
            win.getMouse()
        elif keey == '':
            sums = []
            for i in range(h):
                sums.append([])
                for j in range(w):
                    if i != 0 and i != h-1 and j != 0 and j != w-1:
                        sums[i].append(a[i][j-1]+a[i][j+1]+a[i+1][j+1]+a[i+1][j-1]+a[i+1][j]+a[i-1][j-1]+a[i-1][j]+a[i-1][j+1])
                    else:
                        sums[i].append(0)
                        a[i][j] = 0
            for i in range(1,h-1):
                for j in range(1,w-1):
                    if sums[i][j] == 3 and a[i][j] == 0:
                        a[i][j] = 1
                    elif (sums[i][j] == 2 or sums[i][j] == 3) and a[i][j] == 1:
                        a[i][j] = 1
                    else:
                        a[i][j] = 0
                    #print(aa[i][j],a[i][j])
                    #win.getMouse()
                if sums[i][j] != 0:
                    if a[i][j] == 0:
                        cells[i][j].setFill('white')
                    else:
                        cells[i][j].setFill('green')
            win.update()
        #tii = time.time()
        #if tii - ti < 0.016:
            #time.sleep(0.016-(tii-ti))
            #ti = time.time()
    bbackdrop = Rectangle(Point(0,0),Point(1920,1080))
    bbackdrop.setFill('lightgrey');bbackdrop.setWidth(0);bbackdrop.draw(win)
    lload = Text(Point(w,h),'Loading...')
    lload.setSize(36);lload.draw(win)
    win.update()
    for i in range(h):
        for j in range(w):
            cells[i][j].undraw()
    backdrop.undraw()
    bbackdrop.undraw()
    lload.undraw()
    win.update()

def step(a,cells,win,w,h):
    sums = []
    for i in range(h):
        sums.append([])
        for j in range(w):
            if i != 0 and i != h-1 and j != 0 and j != w-1:
                sums[i].append(a[i][j-1]+a[i][j+1]+a[i+1][j+1]+a[i+1][j-1]+a[i+1][j]+a[i-1][j-1]+a[i-1][j]+a[i-1][j+1])
            else:
                sums[i].append(0)
                a[i][j] = 0
    aa = a
    for i in range(1,h-1):
        for j in range(1,w-1):
            if sums[i][j] == 3 and a[i][j] == 0:
                a[i][j] = 1
            elif (sums[i][j] == 2 or sums[i][j] == 3) and a[i][j] == 1:
                a[i][j] = 1
            else:
                a[i][j] = 0
            if aa[i][j] != a[i][j]:
                if a[i][j] == 0:
                    cells[i][j].setFill('white')
                else:
                    cells[i][j].setFill('green')
    win.update()
    
