import pygame, sys
from pygame.locals import *
from random import randint
from time import time

# Clases
from classes import jugador
from classes import asteroide

# Variable
ancho = 480
alto = 700

playing = True
listaAsteoride = []
puntos = 0
colorFuente = (120, 200, 40)

def cargarAsteroide(x, y):
    meteorito = asteroide.Asteroide(x, y)
    listaAsteoride.append(meteorito)

def retry(nave):
    global playing
    global puntos
    playing = True
    puntos = 0
    pygame.mixer.music.play(-1)
    nave.vida = True

def gameOver():
    global playing
    playing = False
    for meteoritos in listaAsteoride:
        listaAsteoride.remove(meteoritos)
        
# Funcion principal
def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    contador = 0
    
    # Imagen de fondo
    fondo = pygame.image.load('img/fondo.png')
    
    # Titulo
    pygame.display.set_caption('Meteoritos')
    
    # Instancia de nave
    nave = jugador.Nave()
    
    # Sonidos
    pygame.mixer.music.load('sound/fondo.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    sonidoColision = pygame.mixer.Sound('sound/colision.aiff')
    
    # Marcador
    fuenteMarcador = pygame.font.SysFont('Arial', 20)
    
    while True:
        ventana.blit(fondo, (0, 0))
        nave.dibujar(ventana)
        
        tiempo = time()
        
        # Marcador
        global puntos
        textoMarcador = fuenteMarcador.render('Puntos: ' + str(puntos), 0, colorFuente)
        ventana.blit(textoMarcador, (0, 0))

        if playing:
            # Generar meteorito
            if tiempo - contador >= 1:
                contador = tiempo
                posX = randint(2, 478)
                cargarAsteroide(posX, 0)
            
            # Comprobacion de lista de los asteorides
            if len(listaAsteoride) > 0:
                for x in listaAsteoride:
                    if playing:
                        x.dibujar(ventana)
                        x.recorrido()
                    if x.rect.top > alto:
                        listaAsteoride.remove(x)
                    else:
                        # Colision de asteroide con nave
                        if x.rect.colliderect(nave.rect):
                            listaAsteoride.remove(x)
                            # print('GameOver')
                            sonidoColision.play()
                            nave.vida = False
                            gameOver()
            
            # Disparo de proyectil
            if len(nave.listaDisparo) > 0:
                for x in nave.listaDisparo:
                    x.dibujar(ventana)
                    x.recorrido()
                    if x.rect.top < -10:
                        nave.listaDisparo.remove(x)
                    else:
                        # Proyectil con Asteroide
                        for meteoritos in listaAsteoride:
                            if x.rect.colliderect(meteoritos):
                                listaAsteoride.remove(meteoritos)
                                nave.listaDisparo.remove(x)
                                puntos += 1
                                # print('Colision misil con meteorito')
            nave.mover()
            
            
            # Eventos movimiento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                #     if event.key == K_LEFT:
                #         nave.rect.left -= nave.velocidad
                #     elif event.key == K_RIGHT:
                #         nave.rect.right += nave.velocidad
                    if event.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparar(x, y)
            
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                nave.rect.left -= nave.velocidad
            elif key[pygame.K_RIGHT]:
                nave.rect.right += nave.velocidad
            # elif key[pygame.K_SPACE]:
            #     x, y = nave.rect.center
            #     nave.disparar(x, y)
        
        # Game Over
        else:
            fuenteGameOver = pygame.font.SysFont('Arial', 40)
            textoGameOver = fuenteGameOver.render('Game Over', 0, colorFuente)
            ventana.blit(textoGameOver, (ventana.get_width() // 2 - textoGameOver.get_width() // 2,
                                         ventana.get_height() // 2 - textoGameOver.get_height() // 2))
            pygame.mixer.music.fadeout(2000)
            
            textoRetry = fuenteGameOver.render('Retry', 0 , colorFuente)
            retry_rect = pygame.Rect(ventana.get_width() // 2 - textoRetry.get_width() // 2,
                                ventana.get_height() // 2 + textoGameOver.get_height() // 2 - textoRetry.get_height() // 2 + 20,
                                textoRetry.get_width(), textoRetry.get_height())
            pygame.draw.rect(ventana, (0, 0, 0, 0), retry_rect)
            ventana.blit(textoRetry, (ventana.get_width() // 2 - textoRetry.get_width() // 2,
                                      ventana.get_height() // 2 + textoGameOver.get_height() // 2 - textoRetry.get_height() // 2 + 20))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # print('Press ' + str(pos))
                    if retry_rect.collidepoint(pos):
                        retry(nave)
        
        pygame.display.update()

meteoritos()