import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Movimiento Automatico')
colorFondo = (1, 150, 70)
colorFigura = (255, 255, 255)

# Variables para movimiento
velocidad = 0.15
direccion = True
posX, posY = randint(1, 400), randint(1, 300)

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posX, posY, 40, 40))
    
    # movimiento
    if direccion == True:
        if(posX < 500 - 40):
            posX += velocidad
        else:
            direccion = False
    else:
        if posX > 1:
            posX -= velocidad
        else:
            direccion = True
            
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    # Se actualiza
    pygame.display.update()
    