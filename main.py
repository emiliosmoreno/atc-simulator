# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, pygame
from pygame.locals import *
from test._test_multiprocessing import DELTA

# Clase principal del juego
class ATCsimulator:

    # Método de inicialización 
    def __init__(self):
        
        # Constantes
        self.WIDTH = 800
        self.HEIGHT = 600
        self.DELTA = 50
        self.VELOCIDAD=60
        
        self.SIZE_WINDOW = (self.WIDTH, self.HEIGHT)
        self.SIZE_ESPACIO_AEREO = (self.WIDTH-self.DELTA*2, self.HEIGHT-self.DELTA*2)
        self.CL_BLUE=(0,0,255)
        self.CL_BLACK=(0,0,0)
        self.CL_WHITE=(255,255,255)
        
        
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 50)
        self.escena = pygame.display.set_mode(self.SIZE_WINDOW)
        self.escena.fill(self.CL_BLUE)
        pygame.display.set_caption("ATC Simulator by @emiliosmoreno")
        pintar_icono(self)
        self.en_pausa=False 
    
    # Ejecución del juego      
    def run(self):
        
        while True:
            while not self.en_pausa:
                self.clock.tick(self.VELOCIDAD)
                
                pintar_espacio_aereo(self);
                
                gestion_eventos(self)
                
                pintar_pausa_juego(self)
                    
                pygame.display.update()     
            
            gestion_eventos(self)   
            
            pintar_pausa_juego(self)
                    
            pygame.display.update()                
        return 0 

# Método encargado de configurar el icono del juego
def pintar_icono(self):
    self.icono = pygame.image.load('img/icon.png')
    pygame.display.set_icon(self.icono)

# Método encargado de pintar el espacio aéreo
def pintar_espacio_aereo(self):
    self.espacio_aereo = pygame.Surface(self.SIZE_ESPACIO_AEREO)  
    pygame.draw.rect(self.espacio_aereo, self.CL_BLACK, self.espacio_aereo.get_rect())
    self.escena.blit(self.espacio_aereo, (50, 50))

# Método encargado de gestionar el aviso de pausa en el juego
def pintar_pausa_juego(self):
    
        if (self.en_pausa): 
            self.escena.blit(self.font.render("PAUSA",
                                         -1,
                                         (255, 255, 255)),
                            (self.WIDTH/2 - 50, 50))

# Método que gestiona los eventos del juego           
def gestion_eventos(self):
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if (evento.key == K_p):
                self.en_pausa = not self.en_pausa
        if evento.type == QUIT:
            sys.exit(0)    

# Llamada principal          
if __name__ == "__main__":
    pygame.init()
    ATCsimulator().run()
    