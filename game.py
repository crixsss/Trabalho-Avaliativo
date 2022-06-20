import pygame
import random
pygame.init()
largura = 800
altura = 300
tamanho = (largura, altura)

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
