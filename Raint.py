#!/usr/local/bin/python
import pygame, sys, os
from pygame.locals import *

a="Pencil.png"

pygame.init()

dl=1
wi=700*dl
he=400*dl

screen=pygame.display.set_mode((wi,he),0,32)
pygame.display.set_caption("Raint 2.0.2")
pencil=pygame.image.load(a).convert_alpha()
mpencil=pencil
pencil=pygame.transform.scale(pencil,(15,15))

# Color Scheme:

grey=(200,200,200)
dgrey=(160,160,160)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
rose=(255,67,67)

color=black
dtype=pencil
line=1
l=1

# Timer:

clock=pygame.time.Clock()

# Font:

pygame.font.init()
font=pygame.font.Font(None,15)
font_tiny=pygame.font.Font(None,13)

# Variables:


b,f=1,1
er=10
nf=1
n,x=0,0
d=20
c=True
e=False
control=False
points=[]
pointsline=[]
screen.fill(white, None, 0)

# Samples:
py=he/2-d
p_1=(wi-(d+5))
pp=(wi-60)
p_2=wi-5
thick=3

def select(w,z):
    pygame.draw.rect(screen,rose, Rect((w,z),(d,d)),1)

def set_color(name):
    msg=font.render(name, True, black)
    mrect=msg.get_rect()
    pygame.draw.rect(screen, white, Rect((pos[0],pos[1]-mrect[3]),(mrect[2]+6,mrect[3])))
    screen.blit(msg,(pos[0]+3,pos[1]-mrect[3]))

def write(name,font,w,y):
    msg=font.render(name, True, black)
    mrect=msg.get_rect()
    pygame.draw.rect(screen, white, Rect((w,y),((d*2)-2,(d-2))))
    dx=(((d*2)-2)/2)-(mrect[2]/2)
    dy=((d-2)/2)-(mrect[3]/2)
    screen.blit(msg,(w+dx,y+dy))

def samples():
    pp=(wi-55)
    pygame.draw.rect(screen,grey,Rect((pp,py),(50,50)))
    pygame.draw.line(screen,color,(pp,py+5),(p_2,py+5),1)
    pygame.draw.line(screen,color,(pp,py+15),(p_2,py+15),2)
    pygame.draw.line(screen,color,(pp,py+25),(p_2,py+25),3)
    pygame.draw.line(screen,color,(pp,py+35),(p_2,py+35),4)
    pygame.draw.line(screen,color,(pp,py+45),(p_2,py+45),5)

def eraser():
    py=he/2-85
    pygame.draw.rect(screen,grey,Rect((pp+5,py),(50,175)))
    pygame.draw.rect(screen,black,Rect((pp+5,py+5),(10,10)))
    pygame.draw.rect(screen,black,Rect((pp+5,py+20),(20,20)))
    pygame.draw.rect(screen,black,Rect((pp+5,py+45),(30,30)))
    pygame.draw.rect(screen,black,Rect((pp+5,py+80),(40,40)))
    pygame.draw.rect(screen,black,Rect((pp+5,py+125),(50,50)))

def save_data(save):
    pygame.draw.rect(screen, white, Rect((0,0),(wi,d)))
    pygame.draw.rect(screen, white, Rect((0,0),(d,he)))
    pygame.image.save(screen,(save))


def open_data(opne):
    background = pygame.image.load(opne)
    screen.fill(white, None, 0)
    screen.blit(background,(0,0))

def bar(d):
    toprect=pygame.draw.rect(screen,grey,Rect((0,0),(wi,d)))
    rightrect=pygame.draw.rect(screen,grey,Rect((pp,0),(60,he)))
    dtoprect=pygame.draw.rect(screen,dgrey,Rect((2.5,2.5),(wi-5,d-5)))
    drightrect=pygame.draw.rect(screen,dgrey,Rect((pp+3,2.5),(54,he-5)))
    screen.blit(pencil,(5,2))
    linerect=pygame.draw.rect(screen,grey, Rect((25,2),(d-2,d-2)))
    line=pygame.draw.line(screen,black,(25,10),(43,10))
    rectrect=pygame.draw.rect(screen,grey, Rect((50,2),(d-2,d-2)))
    rectangle=pygame.draw.rect(screen,black, Rect((52,2),(d-6,d-6)),2)
    krect=pygame.draw.rect(screen,black, Rect((pp+5,4),(d,d)))
    rrect=pygame.draw.rect(screen,red, Rect((pp+35,4),(d,d)))
    brect=pygame.draw.rect(screen,blue, Rect((pp+5,28),(d,d)))
    grect=pygame.draw.rect(screen,green, Rect((pp+35,28),(d,d)))
    yrect=pygame.draw.rect(screen,yellow, Rect((pp+5,52),(d,d)))
    eraser=pygame.draw.rect(screen,black, Rect((pp+35,52),(d,d)),1)
    eraser_inside=pygame.draw.rect(screen,white, Rect((pp+36,53),(d-2,d-2)))
    write("Save",font,d*6+2,2)
    write("Load",font,d*8+2,2)

while True:
    if len(pointsline)==1:
        pygame.draw.line(screen, white, pointsline[0],pos,thick)

    pos=pygame.mouse.get_pos()
    rel=pygame.mouse.get_rel()

    # Draw the rects:

    bar(d)

    # Events:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pos[1]<=d:
                if pos[0]>=5 and pos[0]<20:
                    dtype=pencil
                if pos[0]>=25 and pos[0]<45:
                    dtype=line
                if pos[0]>=50 and pos[0]<70:
                    dtype=rectangle
                if pos[0]>d*6 and pos[0]<d*8:
                    save_data("Save.jpg")
                if pos[0]>d*8 and pos[0]<d*10:
                    open_data("Save.jpg")
            if pos[0]>=wi-60:
                c=True
                if pos[1]>=4 and pos[1]<=24 and pos[0]>=pp+5 and pos[0]<=pp+25:
                    color=black
                    n=0
                if pos[1]>=4 and pos[1]<=24 and pos[0]>=pp+35 and pos[0]<=pp+55:
                    color=red
                    n=0
                if pos[1]>=28 and pos[1]<=48 and pos[0]>=pp+5 and pos[0]<=pp+25:
                    color=blue
                    n=0
                if pos[1]>=28 and pos[1]<=48 and pos[0]>=pp+35 and pos[0]<=pp+55:
                    color=green
                    n=0
                if pos[1]>=52 and pos[1]<=72 and pos[0]>=pp+5 and pos[0]<=pp+25:
                    color=yellow
                    n=0
                if pos[1]>=52 and pos[1]<=72 and pos[0]>=pp+35 and pos[0]<=pp+55:
                    color=white
                if n==0:
                    if pos[1]>py and pos[1]<=py+10:
                        thick=1
                    if pos[1]>py+10 and pos[1]<=py+20:
                        thick=2
                    if pos[1]>py+20 and pos[1]<=py+30:
                        thick=3
                    if pos[1]>py+30 and pos[1]<=py+40:
                        thick=4
                    if pos[1]>py+40 and pos[1]<=py+50:
                        thick=5
                if n==1:
                    py=he/2-85
                    if pos[1]>py and pos[1]<=py+15:
                        er=10
                    if pos[1]>py+15 and pos[1]<=py+40:
                        er=20
                    if pos[1]>py+40 and pos[1]<=py+75:
                        er=30
                    if pos[1]>py+75 and pos[1]<=py+120:
                        er=40
                    if pos[1]>py+120 and pos[1]<=py+175:
                        er=50
            else:
                if dtype==line:
                    pointsline.append(event.pos)
                    e=True
                c=False
        if event.type == MOUSEBUTTONUP:
            c=True
            del points
            points=[]
        if event.type == KEYDOWN:
            if event.key == K_LCTRL:
                control=True
            if event.key == K_RETURN:
                screen.fill(white, None, 0)
            if event.key == K_s:
                if control==True:
                    pygame.draw.rect(screen, white, Rect((0,0),(screen.get_width(),d/3)))
                    pygame.image.save(screen,("Save.jpg"))
            if event.key == K_o:
                if control==True:
                    background = pygame.image.load("Save.jpg")
                    screen.fill(white, None, 0)
                    screen.blit(background,(0,0))
            if event.key == K_PLUS:
                if control==True:
                    er=er-10
            if event.key == K_MINUS:
                if control==True:
                    er=er+10
        if event.type == KEYUP:
            if event.type == K_LCTRL:
                control=False

    #Select:

    if color==black:
        select(pp+5,4)
    if color==red:
        select(pp+35,4)
    if color==blue:
        select(pp+5,28)
    if color==green:
        select(pp+35,28)
    if color==yellow:
        select(pp+5,52)
    if color==white:
        select(pp+35,52)

    # Mouse:

    if pos[1]>=4 and pos[1]<=24 and pos[0]>=pp+5 and pos[0]<=pp+25:
        set_color("Black")
        n=0
    if pos[1]>=4 and pos[1]<=24 and pos[0]>=pp+35 and pos[0]<=pp+55:
        set_color("Red")
        n=0
    if pos[1]>=28 and pos[1]<=48 and pos[0]>=pp+5 and pos[0]<=pp+25:
        set_color("Blue")
        n=0
    if pos[1]>=28 and pos[1]<=48 and pos[0]>=pp+35 and pos[0]<=pp+55:
        set_color("Green")
        n=0
    if pos[1]>=52 and pos[1]<=72 and pos[0]>=pp+5 and pos[0]<=pp+25:
        set_color("Yellow")
        n=0
    if pos[1]>=52 and pos[1]<=72 and pos[0]>=pp+35 and pos[0]<=pp+55:
        set_color("Eraser")
        n=1
        eraser()
    if pos[1]<=d and pos[0]>=5 and pos[0]<20:
        set_color("Pencil")
    if pos[1]<=d and pos[0]>=25 and pos[0]<45:
        set_color("Line")
    if pos[1]<=d and pos[0]>=50 and pos[0]<70:
        set_color("Rectangle")

    if n==0:
        if color!=white:
            samples()
    if n==1:
        if color==white:
            eraser()
    if e==True:
        if len(pointsline)==1:
            sn=pygame.draw.line(screen, color, pointsline[0],pos,thick)
        if len(pointsline)==2:
            ln=pygame.draw.line(screen, color, pointsline[0],pointsline[1],thick)
            pointsline=[]
    if c==False:
            xa,ya=pos
            points.append(pos)
            if n==1:
                if color==white:
                    xb=xa-er/2
                    yb=ya-er/2
                    pygame.draw.rect(screen,color, Rect((xb,yb),(er,er)))
            if dtype==pencil:
                if len(points)>1:
                        pygame.draw.lines(screen, color, True, points, thick)
                        del points[0]

    pygame.display.update()
