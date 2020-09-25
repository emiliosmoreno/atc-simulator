# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, pygame
from pygame.locals import *
from test._test_multiprocessing import DELTA

# Constantes
WIDTH = 800
HEIGHT = 600
DELTA = 50
VELOCIDAD=60

SIZE_WINDOW = (WIDTH, HEIGHT)
SIZE_ESPACIO_AEREO = (WIDTH-DELTA*2, HEIGHT-DELTA*2)

CL_WHITE=(255,255,255)
CL_BLUE=(0,0,255)



def Main():
    clock = pygame.time.Clock()
    escena = pygame.display.set_mode(SIZE_WINDOW)
    pygame.display.set_caption("ATC Simulator by @emiliosmoreno")
    pintar_icono()
   
    
    while True:
        clock.tick(VELOCIDAD)
        
        pintar_espacio_aereo(escena);
        
        gestion_eventos()
        
        pygame.display.update()                
    return 0 

def pintar_icono():
    icono = pygame.image.load('img/icon.png')
    pygame.display.set_icon(icono)

def pintar_espacio_aereo(escena):
    espacio_aereo = pygame.Surface(SIZE_ESPACIO_AEREO)  
    pygame.draw.rect(espacio_aereo, CL_WHITE, espacio_aereo.get_rect())
    escena.blit(espacio_aereo, (50, 50))
    
def gestion_eventos():
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)    
              
if __name__ == "__main__":
    pygame.init()
    Main()
    