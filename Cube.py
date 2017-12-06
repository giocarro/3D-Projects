#Cube

import pygame, sys, time
from pygame.locals import *

GREEN = (30,250,0)
BLACK = (0,0,0)
RED = (255,56,66)
SKY_BLUE = (204,255,229)
WHITE = (255,255,255)
PINK = (233,38,204)
BLUE = (38,44,233)
YELLOW = (250,255,88)
ORANGE = (255,205,0)
BROWN = (107,92,34)

pygame.init() #obligatorio
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cube")
screen.fill(SKY_BLUE)

v=400
w=0
zmax=5
F=[v,w,zmax] #Focus

x=400
y=400
z=0
C=[x,y,z] #3D Origin

uic=[-100,100] #user initial coords from 3D origin

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

    #Rectangle lower left corner
    x3=x1
    y3=y2
    #Rectangle upper right corner
    x4=x2
    y4=y1
    print 'x1=',x1,'  y1=',y1
    print 'x2=',x2,'  y2=',y2
    print 'x3=',x3,'  y3=',y3
    print 'x4=',x4,'  y4=',y4
    print 'len=',len_rect,'  wid=',wid_rect,'  ratio=',ratio
    Rul=[x1,y1] #Rectangle upper left corner
    Rlr=[x2,y2] #Rectangle lower right corner
    Rll=[x3,y3] #Rectangle lower left corner
    Rur=[x4,y4] #Rectangle upper left corner
    variables=[Rul,Rlr,Rll,Rur,len_rect,wid_rect,ratio] #[[x1,y1],[x2,y2],[x3,y3],[x4,y4],len_rect,wid_rect,ratio]
    return variables

def Cube(v1_list,v2_list):
    #Front Face
    FRF = pygame.draw.polygon(screen, WHITE, [[v1_list[0][0],v1_list[0][1]],[v1_list[2][0],v1_list[2][1]],[v1_list[1][0],v1_list[1][1]],[v1_list[3][0],v1_list[3][1]]],0)
    #Back Face
    BKF = pygame.draw.polygon(screen, BLACK, [[v2_list[0][0],v2_list[0][1]],[v2_list[2][0],v2_list[2][1]],[v2_list[1][0],v2_list[1][1]],[v2_list[3][0],v2_list[3][1]]],0)
    #Upper Face
    UPF = pygame.draw.polygon(screen, BLUE, [[v1_list[0][0],v1_list[0][1]],[v2_list[0][0],v2_list[0][1]],[v2_list[3][0],v2_list[3][1]],[v1_list[3][0],v1_list[3][1]]],0)
    #Lower Face
    LOF = pygame.draw.polygon(screen, GREEN, [[v1_list[2][0],v1_list[2][1]],[v2_list[2][0],v2_list[2][1]],[v2_list[1][0],v2_list[1][1]],[v1_list[1][0],v1_list[1][1]]],0)
    #Right Side Face
    RGT = pygame.draw.polygon(screen, PINK, [[v1_list[3][0],v1_list[3][1]],[v2_list[3][0],v2_list[3][1]],[v2_list[1][0],v2_list[1][1]],[v1_list[1][0],v1_list[1][1]]],0)
    #Left Side Face
    LFT = pygame.draw.polygon(screen, YELLOW, [[v1_list[0][0],v1_list[0][1]],[v2_list[0][0],v2_list[0][1]],[v2_list[2][0],v2_list[2][1]],[v1_list[2][0],v1_list[2][1]]],0)

    #pygame.draw.polygon(screen, RED, [[x1,y1],[x3,y3],[x2,y2],[x4,y4]],0)

if __name__=='__main__':
    z0=z
    Rl_0=[x0,y0,z0] #initial rectangle

    x1=x0
    y1=y0
    ratio=0

    v1_list=Points(x1,y1,z0,ratio)
    #[[x1,y1],[x2,y2],[x3,y3],[x4,y4],len_rect,wid_rect,ratio]
    #[[00,01],[10,11],[20,21],[30,31],    4   ,    5   ,  6  ]
    z0=z0+1
    ratio=v1_list[6]
    v2_list=Points(x1,y1,z0,ratio)
    Cube(v1_list,v2_list)

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() #The window is going to be updating
        time.sleep(0.5)
        #screen.fill(black)
                
