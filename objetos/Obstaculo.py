import pygame
from Floor import Floor
from Obstaculo import Obstaculo

class Obstaculo:
    def __init__(self):
        self.image = pygame.image.load("static/obstaculo1.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0