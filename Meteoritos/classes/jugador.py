import pygame
from classes import disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load('img/nave.png')
        self.imagenExplota = pygame.image.load('img/naveExplota.png')
        
        # Rectangulo de la imagen
        self.rect = self.imagenNave.get_rect()
        
        # Situarla en la posicion inicial
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 1
        self.vida = True
        self.listaDisparo = []
        self.sonidoDisparo = pygame.mixer.Sound('sound/disparo.aiff')
        self.sonidoDisparo.set_volume(0.2)
        
    def mover(self):
        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 490:
                self.rect.right = 490
        
    
    def disparar(self, x, y):
        # print('Pium Pium')
        if self.vida:
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()
    
    def dibujar(self, superficie):
        if self.vida:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplota, self.rect)