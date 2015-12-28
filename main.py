#maine
from graphics import *
import terrain

def main(win,t_height,t_type,t_biome,land,w,h):
    tmod = 0
    hmod = 0
    yyay = terrain.getTiles(t_biome,h)
    iceyyay = (yyay[0]/10+yyay[2]/20+yyay[4]/30+yyay[6]/10+yyay[11]/3+yyay[16])
    while True:
        keey = win.getKey()
        if keey == 'h':
            cont = 0
            tmod += 3
            for i in range(h):
                for j in range(w):
                    t_height[i][j],t_type[i][j],t_biome[i][j] = terrain.changeter(t_height[i][j],t_type[i][j],tmod,0,land,cont,i,w,h)
                    cont += 1
        elif keey == 'c':
            cont = 0
            tmod -= 3
            for i in range(h):
                for j in range(w):
                    t_height[i][j],t_type[i][j],t_biome[i][j] = terrain.changeter(t_height[i][j],t_type[i][j],tmod,0,land,cont,i,w,h)
                    cont += 1
        elif keey == 'q':
            win.quit()
            sys.exit()
        yay = terrain.getTiles(t_biome,h)
        difyay = ((yay[0]/10+yay[2]/20+yay[4]/30+yay[6]/10+yay[11]/3+yay[16])-iceyyay)/2000
        print(difyay)
        cont = 0
        for i in range(h):
            for j in range(w):
                t_height[i][j],t_type[i][j],t_biome[i][j] = terrain.changeter(t_height[i][j],t_type[i][j],tmod,difyay,land,cont,i,w,h)
                cont += 1
        win.update()
        yay = terrain.getTiles(t_biome,h)
        print(yay)
def start():
    w=192
    h=108
    win = GraphWin('game4',w*10,h*10,fullscreen=True,autoflush=False)
    win.setCoords(0,0,w,h)
    loading = Text(Point(w/2,h/2),'Generating Map...');loading.setSize(36);loading.draw(win)
    win.update()
    t_height,t_type,t_biome,land = terrain.terraingen(win,w,h)
    loading.undraw()
    win.update()
    main(win,t_height,t_type,t_biome,land,w,h)
start()
