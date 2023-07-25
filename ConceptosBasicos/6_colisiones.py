import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Movimiento con Raton y Colisiones')
colorFondo = (1, 150, 70)
colorCuadro0 = (255, 255, 0)
colorCuadro1 = (0, 255, 255)

# Variables para movimiento
velocidad = 15
direccion = True
posX0, posY0 = randint(1, 400), randint(1, 300)
posX1, posY1 = randint(1, 400), randint(1, 300)
lado = 40

while True:
    ventana.fill(colorFondo)
    cuadro0 = pygame.draw.rect(ventana, colorCuadro0, (posX0, posY0, lado, 40))
    cuadro1 = pygame.draw.rect(ventana, colorCuadro1, (posX1, posY1, lado, 40))
    
    # Deteccion de colision
    if cuadro0.colliderect(cuadro1):
        print(f'Colision!!! en coordenada: {posX0}, {posY0}')
        posX1, posY1 = randint(1, 400), randint(1, 300)
        cuadro1.left = posX1 - (lado / 2)
        cuadro1.top = posX1 - (lado / 2)
        
    
    # Deteccion de movimiento con Raton
    posX0, posY0 = pygame.mouse.get_pos()
    posX0 = posX0 - (lado / 2)
    posY0 = posY0 - (lado / 2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        
    # Se actualiza
    pygame.display.update()
    