# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, pygame, math, random
from pygame.locals import *

# Constantes 
class Constantes:
    
    DEBUG = False
  
    CL_BLUE=(0,0,255)
    CL_BLACK=(0,0,0)
    CL_WHITE=(255,255,255) 
    CL_RED=(255,0,0) 
    
    WIDTH=800
    HEIGHT=600
    DELTA=50
    VELOCIDAD=1
    
    SIZE_WINDOW = (WIDTH, HEIGHT)
    SIZE_ESPACIO_AEREO = (WIDTH-DELTA*2, HEIGHT-DELTA*2)
    CL_BLUE=(0,0,255)
    CL_BLACK=(0,0,0)
    CL_WHITE=(255,255,255)
    AIRLINES=["IB","AFL","AFR","VLG"]
    
class Avion:
    
    def __init__(self, escena, x, y, velocidad, altura, direccion):
        self.id=Constantes.AIRLINES[random.randint(1,3)]+str(random.randint(0,99))
        self.posx=x
        self.posy=y
        self.posz=altura
        self.escena=escena
        self.velocidad = velocidad / 100
        self.direccion=direccion #Valores permitidos: 1-360 (grados)s
        self.font = pygame.font.SysFont("Arial", 12)

    def avanzar(self):
       
        desplazamiento_x=0
        desplazamiento_y=0
        if (self.direccion>=0 and self.direccion<=90): 
            #1er cuadrante
            desplazamiento_x=math.cos(math.radians(self.direccion-90))*self.velocidad
            desplazamiento_y=math.sin(math.radians(self.direccion-90))*self.velocidad
        else:
            if (self.direccion>90 and self.direccion<=180):
                #2do cuadrante
                desplazamiento_x=math.sin(math.radians(180-self.direccion))*self.velocidad
                desplazamiento_y=math.cos(math.radians(180-self.direccion))*self.velocidad
            else:
                if (self.direccion>180 and self.direccion<=270):
                    #3er cuadrante
                    desplazamiento_x=math.cos(math.radians(self.direccion-90))*self.velocidad
                    desplazamiento_y=math.sin(math.radians(self.direccion-90))*self.velocidad
                else:
                    if (self.direccion>270 and self.direccion<=360):
                        #4to cuadrante
                        desplazamiento_x=math.cos(math.radians(self.direccion-90))*self.velocidad
                        desplazamiento_y=math.sin(math.radians(self.direccion-90))*self.velocidad   
            
        self.posx = self.posx + desplazamiento_x
        self.posy = self.posy + desplazamiento_y
        
    def pintar(self):
        self.airplane=[]
        
        #print(self.id+" - v="+str(self.velocidad))
        traza=self.velocidad
        tamanyo=3
        distancia=5
        self.airplane.append(pygame.Rect(self.posx, self.posy, tamanyo, tamanyo))
        
        

        #while (traza>0):
        #    self.airplane.append(pygame.Rect(self.posx+distancia, self.posy+distancia, tamanyo, tamanyo))
        #    tamanyo=tamanyo-0.5
        #    distancia=distancia+5
        #    traza=traza-0.5
        
        for traza_avion in self.airplane:  
            pygame.draw.rect(self.escena, Constantes.CL_WHITE, traza_avion) 
            
    def pintar_datos_avion(self):
        
        if (len(self.id)<2):
            self.desp=0
        else:
            if (len(self.id)>2 and len(self.id)<5):
                self.desp=1
            else:
                self.desp=2
        
               
        #Identificador del avión
        self.escena.blit(self.font.render(str(self.id),-1,Constantes.CL_WHITE),
                         (self.posx-self.desp, self.posy-45))
        
        #Altura
        self.escena.blit(self.font.render(str(self.posz),-1,Constantes.CL_WHITE),
                         (self.posx-self.desp, self.posy-30))
 
        #Velocidad
        self.escena.blit(self.font.render(str(int(self.velocidad*100)),-1,Constantes.CL_WHITE),
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
        self.num_aviones=0
        
        #Cuadrante 1
        new_avion = Avion(self.escena, 400,300, 100,2000, 45)
        self.aviones.append(new_avion)
        
        #Cuadrante 2
        new_avion = Avion(self.escena, 400,300, 150,2000, 135)
        #new_avion = Avion(self.escena, 400,300, 100,2000, 180)
        self.aviones.append(new_avion)
        
        #Cuadrante 3
        #new_avion = Avion(self.escena, 400,300, 100,2000, 190)
        new_avion = Avion(self.escena, 400,300, 100,2000, 225)
        #new_avion = Avion(self.escena, 400,300, 100,2000, 270)
        self.aviones.append(new_avion)
        
        #Cuadrante 4
        new_avion = Avion(self.escena, 400,300, 150,2000, 315)
        #new_avion = Avion(self.escena, 400,300, 100,2000, 360)
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
    if Constantes.DEBUG:
        print("\n")
    for avion in self.aviones:
        avion.avanzar()
        avion.pintar()
        avion.pintar_datos_avion()
    
# Método encargado de gestionar el aviso de pausa en el juego
def pintar_pausa_juego(self):
    
        if (self.en_pausa): 
            self.escena.blit(self.font.render("PAUSA",-1,Constantes.CL_WHITE),
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
    