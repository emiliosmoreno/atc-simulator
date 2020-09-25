# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, pygame, math
from pygame.locals import *

# Constantes
class Constantes:
    
    CL_BLUE=(0,0,255)
    CL_BLACK=(0,0,0)
    CL_WHITE=(255,255,255) 
    CL_RED=(255,0,0) 
    
    WIDTH=800
    HEIGHT=600
    DELTA=50
    VELOCIDAD=5
    
    SIZE_WINDOW = (WIDTH, HEIGHT)
    SIZE_ESPACIO_AEREO = (WIDTH-DELTA*2, HEIGHT-DELTA*2)
    CL_BLUE=(0,0,255)
    CL_BLACK=(0,0,0)
    CL_WHITE=(255,255,255)
    
class Avion:
    def __init__(self, escena, x, y, velocidad, altura):
        self.velocidad = velocidad
        self.posx=x
        self.posy=y
        self.altura=altura
        self.escena=escena
        self.direccion=180 #Valores permitidos: 1-360 (grados)s
        self.font = pygame.font.SysFont("Arial", 12)
        self.id=100
        
    def avanzar(self):
       
        if (self.posx < 0):
            self.posx = -self.posx + math.cos(math.radians(self.direccion))
        
        if (self.posx > 0):
            self.posx = self.posx + math.cos(math.radians(self.direccion))
        
        self.posy = self.posy + math.sin(math.radians(self.direccion))
        print(str(self.posx)+","+str(self.posy))
        
    def pintar(self):
        self.rect= pygame.Rect(self.posx, self.posy, 5, 5)
        pygame.draw.rect(self.escena, Constantes.CL_WHITE, self.rect)
        
    def pintar_id(self):
        
        if (self.id<100):
            self.desp=0
        if (self.id>=100 and self.id<1000):
            self.desp=1    
        self.escena.blit(self.font.render(str(self.id),
                                         -1,
                                         (255, 255, 255)),
                            (self.posx-self.desp, self.posy-15))
        
# Clase principal del juego
class ATCsimulator:

    # Método de inicialización 
    def __init__(self):
        
      
        
        
        
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 50)
        self.escena = pygame.display.set_mode(Constantes.SIZE_WINDOW)
        
        pygame.display.set_caption("ATC Simulator by @emiliosmoreno")
        pintar_icono(self)
        self.en_pausa=False 
    
        self.aviones =[]
        
        new_avion = Avion(self.escena, 900,300, 0.1,2000)
        self.aviones.append(new_avion)
        
    # Ejecución del juego      
    def run(self):
        
        while True:
            while not self.en_pausa:
                self.clock.tick(Constantes.VELOCIDAD)
                
                pintar_espacio_aereo(self)
                
                pintar_aviones(self)
                
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
    self.escena.fill(Constantes.CL_BLUE)
    self.espacio_aereo = pygame.Surface(Constantes.SIZE_ESPACIO_AEREO)  
    pygame.draw.rect(self.espacio_aereo, Constantes.CL_BLACK, self.espacio_aereo.get_rect())
    self.escena.blit(self.espacio_aereo, (50, 50))

# Método encargado de pintar los aviones en el espacio aéreo
def pintar_aviones(self):
    for avion in self.aviones:
        avion.avanzar()
        avion.pintar()
        avion.pintar_id()
    
# Método encargado de gestionar el aviso de pausa en el juego
def pintar_pausa_juego(self):
    
        if (self.en_pausa): 
            self.escena.blit(self.font.render("PAUSA",
                                         -1,
                                         (255, 255, 255)),
                            (Constantes.WIDTH/2 - 50, 50))

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
    