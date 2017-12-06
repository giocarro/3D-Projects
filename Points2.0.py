#Points 2

import pygame, sys, time
from pygame.locals import *

GREEN = (30,250,0)
black = (0,0,0)
color1 = (40,24,66)
color2 = (10,234,59)
color3 = (6,4,2)

pygame.init() #obligatorio
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Dots")

v=400
w=0
zmax=50
F=[v,w,zmax] #Focus

x=400
y=500
z=0
C=[x,y,z] #3D Origin

uic=[-200,100] #user initial coords from 3D origin

x0=x+uic[0] #x0=200
y0=y-uic[1] #y0=400

def Points(x1,y1,z0,ratio):
    x1=x1+z0*abs(x-x0)/zmax
    x2=2*x-x1
    len_rect=x2-x1

    if ratio==0:
        y1=y1-z0*abs(y-w)/zmax
        y2=2*(y-z0*abs(y-w)/zmax)-y1
        wid_rect=y2-y1
        ratio=len_rect/wid_rect #ratio similarity
    else:
        wid_rect=len_rect/ratio
        y1=y-z0*abs(y-w)/zmax-wid_rect/2
        y2=y-z0*abs(y-w)/zmax+wid_rect/2
    
    print 'x1=',x1,'  y1=',y1
    print 'x2=',x2,'  y2=',y2
    print 'len=',len_rect,'  wid=',wid_rect,'  ratio=',ratio
    Rl=[x1,y1,z0] #Rectangle upper left corner
    Rr=[x2,y2,z0] #Rectangle lower right corner
    pygame.draw.circle(screen,GREEN,[x1,y1],5,0)
    pygame.draw.circle(screen,GREEN,[x2,y2],5,0)

    return ratio

if __name__=='__main__':
    z0=z
    Rl_0=[x0,y0,z0] #initial rectangle

    x1=x0
    y1=y0
    ratio=0

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        r=Points(x1,y1,z0,ratio)
        z0=z0+1
        ratio=r

        pygame.display.update() #The window is going to be updating
        time.sleep(0.1)
        screen.fill(black)
                
