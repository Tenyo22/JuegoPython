import sys
import pygame
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Imagen y Posiciones al Azar')
colorFondo = (1, 150, 70)
colorRectangulo = (255, 60, 40)
# Cargar imagen
imagen = pygame.image.load('./Imagenes/DeluxeCofee.png')
# Posicion de imagen
posX, posY = (10, 40)
while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen, (posX, posY))
    for i in range(5):
        posXRect, posYRect = randint(50, 700), randint(50, 500)
        r,g,b = randint(0, 255), randint(0, 255), randint(0, 255)
        colorRectangulo = (r,g,b)
        pygame.draw.rect(ventana, colorRectangulo, (posXRect, posYRect, 40, 40))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()