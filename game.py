from turtle import pos
import pygame
import random
pygame.init()
largura = 800
altura = 300
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Kuduairo")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/icone.jpg")
pygameDisplay.set_icon(gameIcon)

bg = pygame.image.load("assets/fundo.jpg")

bg_destruido = pygame.image.load("assets/perdeu.jpg")

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event

def dead(pontos):
    gameDisplay.blit(bg_destruido, (0, 0))
    pygame.mixer.music.stop()
    fonte = pygame.font.Font("freesansbold.ttf", 40)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 20)
    texto = fonte.render("Voiçuir perdui com" +str(pontos) + " pontos!", True, white)
    textoContinue = fonteContinue.rende("Apierte enter paira continuaire...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()

def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 1
    posicaoXKuduairo = 500
    posicaoYKuduairo = 100
    movimentoXKuduairo = 0
    movimentoYKuduairo = 0
    pontos = 0
    kuduairo = pygame.image.load("assets/kuduairo.png")
    brasil = pygame.image.load("assets/brasil.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    alturaKuduairo = 483
    larguraKuduairo = 638
    alturaBrasil = 400
    larguraBrasil = 400
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
                    movimentoXKuduairo = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXKuduairo = 10
                elif event.key == pygame.UP:
                    movimentoYKuduairo = - 10
                elif event.key == pygame.K_DOWN:
                    movimentoYKuduairo = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXKuduairo = 0
                    movimentoYKuduairo = 0
        
        if jogando == True:
            posicaoXKuduairo = posicaoXKuduairo + movimentoXKuduairo
            posicaoYKuduairo = posicaoYKuduairo + movimentoYKuduairo
            if posicaoXKuduairo < 0:
                posicaoXKuduairo = 0
            elif posicaoXKuduairo >= largura - larguraKuduairo:
                posicaoXKuduairo = largura - larguraKuduairo
            
            if posicaoYKuduairo < 0:
                posicaoYKuduairo = 0
            elif posicaoYKuduairo >= altura - alturaKuduairo:
                posicaoYKuduairo = altura - alturaKuduairo
            
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
            gameDisplay.blit(brasil, (posicaoX, posicaoY))
            gameDisplay.blit(kuduairo, (posicaoXKuduairo, posicaoYKuduairo))
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Poaintos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

            pixelsYKuduairo = list(range(posicaoYKuduairo, posicaoYKuduairo + alturaKuduairo + 1))
            pixelsXKuduairo = list(range (posicaoXKuduairo, posicaoXKuduairo + larguraKuduairo + 1))

            pixelsYBrasil = list(range(posicaoY, posicaoY + alturaBrasil + 1))
            pixelsXBrasil = list(range(posicaoX, posicaoX + larguraBrasil + 1))

            if len(list(set(pixelsYBrasil) & set(pixelsXKuduairo))) > dificuldade:
                if len (list(set(pixelsXBrasil) & set(pixelsYBrasil))) > dificuldade:
                    jogando = False
                    dead(pontos)
        pygameDisplay.update()
        clock.tick(60)

jogo()
