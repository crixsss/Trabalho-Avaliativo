import os
import pygame
import random
from assets.funcoes import clean
pygame.init()
largura = 1024
altura = 510
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Dragon Ball Z")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/icone.ico")
pygameDisplay.set_icon(gameIcon)

bg = pygame.image.load("assets/fundo3.jpg")

bg_destruido = pygame.image.load("assets/nameke.png")

gameOverSom = pygame.mixer.Sound("assets/pacman.wav")
gameOverSom.set_volume(0.5)

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event

def dead(pontos):
    gameDisplay.blit(bg_destruido, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(gameOverSom)
    fonte = pygame.font.Font("freesansbold.ttf", 55)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 30)
    texto = fonte.render("Você perdeu com " +str(pontos) + " pontos!", True, white)
    textoContinue = fonteContinue.render("Aperte enter para continuar...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()

def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 1
    posicaoXGoku = 500
    posicaoYGoku = 100
    movimentoXGoku = 0
    movimentoYGoku = 0
    pontos = 0
    goku = pygame.image.load("assets/goku.png")
    freeza = pygame.image.load("assets/freeza.png")
    pygame.mixer.music.load("assets/trilha.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    alturaGoku = 100
    larguraGoku = 60
    alturaFreeza = 100
    larguraFreeza = 60
    dificuldade = 29
    jogando = True
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXGoku = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXGoku = 10
                elif event.key == pygame.K_UP:
                    movimentoYGoku = - 10
                elif event.key == pygame.K_DOWN:
                    movimentoYGoku = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXGoku = 0
                    movimentoYGoku = 0
        
        if jogando == True:
            posicaoXGoku = posicaoXGoku + movimentoXGoku
            posicaoYGoku = posicaoYGoku + movimentoYGoku
            if posicaoXGoku < 0:
                posicaoXGoku = 0
            elif posicaoXGoku >= largura - larguraGoku:
                posicaoXGoku = largura - larguraGoku
            
            if posicaoYGoku < 0:
                posicaoYGoku = 0
            elif posicaoYGoku >= altura - alturaGoku:
                posicaoYGoku = altura - alturaGoku

            gameDisplay.blit(bg, (0, 0))
                
            
            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    pontos = pontos + 1
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    pontos = pontos + 1
            gameDisplay.blit(freeza, (posicaoX, posicaoY))
            gameDisplay.blit(goku, (posicaoXGoku, posicaoYGoku))
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

            pixelsYGoku = list(range(posicaoYGoku, posicaoYGoku + alturaGoku + 1))
            pixelsXGoku = list(range (posicaoXGoku, posicaoXGoku + larguraGoku + 1))

            pixelYFreeza = list(range(posicaoY, posicaoY + alturaFreeza + 1))
            pixelXFreeza = list(range(posicaoX, posicaoX + larguraFreeza + 1))

            if len(list(set(pixelYFreeza) & set(pixelsYGoku))) > dificuldade:
                if len (list(set(pixelXFreeza) & set(pixelsXGoku))) > dificuldade:
                    jogando = False
                    dead(pontos)
        pygameDisplay.update()
        clock.tick(60)
        
while True:
    try:
        print ("\n")
        arquivo = open("arquivo.txt", "a")
        arquivo.write(input("Digite seu nome: ") + "\n")
        arquivo.write(input("Digite seu email:  ") + "\n")
        arquivo.close()

        arquivo = open("arquivo.txt", "r")
        clean()
        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()
        print()
        break
    except:
        arquivo = open("arquivo.txt", "w")
        arquivo.close()

jogo()
