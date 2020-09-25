# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 640
HEIGHT = 480

def Main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0 
  
if __name__ == "__main__":
    pygame.init()
    Main()
    