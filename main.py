import pygame
from PPlay import *
pygame.init()
janela = window.Window(800, 600)
tela = pygame.display.set_mode((800, 600))
branco = (255, 255, 255)
preto = (0, 0, 0)
pretin = (100, 100, 100)


def botao(cor, cora, x, y, w, h):
    pygame.draw.rect(tela, cor, (x, y, w, h))
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, cora, (x, y, w, h))
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            return 1


def intro():
    introd = True
    while introd:
        janela.set_background_color(branco)
        x = botao(preto, pretin, janela.width/2-50, janela.height/2-25, 100, 50)
        if x == 1:
            introd = False
        janela.update()
        pygame.display.update()


intro()
