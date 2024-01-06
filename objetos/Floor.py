import pygame
from main import altura_tela, largura_tela
from objetos.Obstaculo import Obstaculo
from objetos.jogador import Jogador
class Floor:
    def __init__(self):
        self.rect = pygame.Rect(0, altura_tela - 40, largura_tela, 40)
        self.color = (0, 255, 0)