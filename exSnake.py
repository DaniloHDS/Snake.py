# pip install pygame

import pygame
import random
import sys

pygame.init()
tela = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Jogo da Cobrinha!")

PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

fonte = pygame.font.SysFont('Arial', 20)

def novo_jogo():
    return {
        'cobra' : [(100, 50)],
        'direcao' : (10, 0),
        'comida' : (random.randrange(0, 600, 10), random.randrange(0, 400, 10)),
        'ponto' : 0,
        'rodando' : True
    }

def desenhar(cobra, comida, ponto):
    tela.fill(PRETO)
    for parte in cobra:
        pygame.draw.rect(tela, VERDE, (*parte, 10, 10))
    pygame.draw.rect(tela, VERMELHO, (*comida, 10, 10))

    texto_pontos = fonte.render(f"Pontos: {ponto}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))
    pygame.display.update()

def tela_game_over(ponto):
    tela.fill(PRETO)
    texto_game_over = fonte.render("GAME OVER!", True, VERMELHO)
    texto_pontos_finais = fonte.render(f"Pontuação Final: {ponto}", True, BRANCO)
    texto_reiniciar = fonte.render("Precionar R para reiniciar", True, BRANCO)

    tela.blit(texto_game_over, (350 - texto_game_over.get_width() // 2, 150))
    tela.blit(texto_pontos_finais, (350 - texto_pontos_finais.get_width() // 2, 180))
    tela.blit(texto_reiniciar, (350 - texto_reiniciar.get_width() // 2, 210))
    pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    jogo = novo_jogo()
    relogio = pygame.time.Clock()

    while True:
        while jogo['rodando']:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP and jogo['direcao'] != (0, 10):
                        jogo['direcao'] = (0, -10)
                    elif evento.key == pygame.K_DOWN and jogo['direcao'] != (0, -10):
                        jogo['direcao'] = (0, 10)
                    elif evento.key == pygame.K_LEFT and jogo['direcao'] != (10, 0):
                        jogo['direcao'] = (-10, 0)
                    elif evento.key == pygame.K_RIGHT and jogo['direcao'] != (-10, 0):
                        jogo['direcao'] = (10, 0)

            nova_cabeca = (
                jogo['cobra'][0][0] + jogo['direcao'][0],
                jogo['cobra'][0][1] + jogo['direcao'][1]
            )
            jogo ['cobra'].insert(0, nova_cabeca)

            if nova_cabeca == jogo['comida']:
                jogo['comida'] = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
                jogo['ponto'] +=10
            else :
                jogo['cobra'].pop()

            if (nova_cabeca in jogo['cobra'][1:] or
                nova_cabeca[0] < 0 or nova_cabeca[0] >= 700 or
                nova_cabeca[1] < 0 or nova_cabeca[1] >= 400):
                jogo['rodando'] = False


            desenhar(jogo['cobra'], jogo['comida'], jogo['ponto'])
            relogio.tick(15)

        if tela_game_over(jogo['ponto']):
            jogo = novo_jogo()
        else:
            pygame.quit


if __name__ == "__main__":
    main()
    pygame.quit()