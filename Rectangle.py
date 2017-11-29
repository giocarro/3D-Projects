#Rectangle

import pygame, sys, time
from pygame.locals import *

Color = (30,250,0)
Colordos = pygame.Color(255,120,9)
black = (0,0,0)
#Center point at 0,0,0
c=[0,0,10]

pygame.init() #obligatorio
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rectangle")

def Rectangle(x1,y1,l,w):
    pygame.draw.rect(screen,Color,(x1,y1,l,w)) #(x1,y1,length,width)

#pygame.draw.circle(screen,Color,(200,200),100)

#pygame.draw.polygon(screen,Color,((300,300),(400,300),(500,400),(400,500),(300,450)))

if __name__=='__main__':
    #Depth
    z=c[2]

    #Center (x,y)=(400,500)
    x=c[0]+400
    y=c[1]+500-4*z

    #(x1,y1)=(200,400) Upper left corner initial parameters
    x1=200+1.6*z
    
    #l=400
    #w=100

    while True:
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        #Variable parameters
        print 'x1=',x1,' y=',y,'  z=',z
        y1=-2*x1+800
        #(x2,y2)=(600,600) Lower right corner initial parameters
        x2=2*x-x1
        y2=2*y-y1
        #length
        l=x2-x1
        #width
        w=y2-y1

        #Rectangle
        Rectangle(x1,y1,l,w)
        z=z+1
        y=y-4
        s=-0.5*x+y
        x1=(0.4)*(800-s)
        
        pygame.display.update() #The window is going to be updating
        time.sleep(0.01)
        screen.fill(black)
