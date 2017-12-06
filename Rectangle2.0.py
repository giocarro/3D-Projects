#Rectangle 2.0

import pygame, sys, time
from pygame.locals import *

GREEN = (30,250,0)
black = (0,0,0)
RED = (255,56,66)
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

clock = pygame.time.Clock()

def Points(x1,y1,z0,ratio):
    #x1=x1+z0*abs(x-x0)/zmax
    x1=x1+z0*abs(w-x0)/zmax
    #x2=2*(x+z0*abs(x-x0)/zmax)-x1
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
    variables=[Rl,Rr,len_rect,wid_rect,ratio] #[[x1,y1,z0],[x2,y2,z0],ratio]
    return variables

def Rectangle(v_list):
    pygame.draw.rect(screen,RED,(v_list[0][0],v_list[0][1],v_list[2],v_list[3])) #(x1,y1,len_rect,wid_rect)

if __name__=='__main__':

    z0=z
    Rl_0=[x0,y0,z0] #initial rectangle

    x1=x0
    y1=y0
    ratio=0

    while True:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        v_list=Points(x1,y1,z0,ratio)
        #[[x1,y1,z0],[x2,y2,z0],len_rect,wid_rect,ratio]
        #[[00,01,02],[10,11,12],    2   ,   3    ,  4  ]
        z0=z0+1
        ratio=v_list[4]
        print '(x1,y1)=(',v_list[0][0],',',v_list[0][1],')  (x2,y2)=(',v_list[1][0],',',v_list[1][1],')'
        Rectangle(v_list)

        pygame.display.update() #The window is going to be updating
        #time.sleep(0.01)
        screen.fill(black)
                
