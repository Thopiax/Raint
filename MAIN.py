import pygame
from pygame.locals import *
from sys import exit
from pygame.image import*
from pygame.font import*
from pygame.mouse import*
from pygame.draw import*

pygame.init()

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

# Timer:

clock=pygame.time.Clock()

# Font:

pygame.font.init()
font=pygame.font.Font(None,15)
font_tiny=pygame.font.Font(None,13)


def select(w,z):
    pygame.draw.rect(screen,rose, Rect((w,z),(d,d)),1)

def write(name,font,w,y):
    msg=font.render(name, True, black)
    mrect=msg.get_rect()
    pygame.draw.rect(screen, white, Rect((w,y),((d*2)-2,(d-2))))
    dx=(((d*2)-2)/2)-(mrect[2]/2)
    dy=((d-2)/2)-(mrect[3]/2)
    screen.blit(msg,(w+dx,y+dy))
    
def save_data(save):
    pygame.draw.rect(screen, white, Rect((0,0),(wi,d)))
    pygame.draw.rect(screen, white, Rect((0,0),(d,he)))
    pygame.image.save(screen,(save))
    root.destroy()
    
def open_data(opne):
    background = pygame.image.load(opne)
    screen.fill(white, None, 0)
    screen.blit(background,(0,0))
    root.destroy()
