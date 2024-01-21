import pygame
from pygame.locals import KEYDOWN, K_SPACE
from time import sleep, time

largura_tela = 800
altura_tela = 600
gravidade = 0.4
impulso_pulo = -8


class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(10, altura_tela - 100, 15, 30)
        self.color = (255, 0, 0)
        self.velocidade = 4
        self.velocidade_vertical = 0
        self.pulando = False
        self.vidas = 3
        self.coracao = pygame.transform.scale(pygame.image.load("static/coracao.png"), (20, 20))
        self.tempo_ultima_morte = 0
        self.moedas_coletadas = 0

    def mover(self, keys):
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_d] and self.rect.x < largura_tela - self.rect.width:
            self.rect.x += self.velocidade

        if keys[pygame.K_w] and not self.pulando:
            self.velocidade_vertical = impulso_pulo
            self.pulando = True

        if not self.esta_no_chao():
            self.velocidade_vertical += gravidade
        else:
            self.velocidade_vertical = 0
            self.pulando = False

        self.rect.y += self.velocidade_vertical

    def coletada(self):
        self.moedas_coletadas += 1

    def reset_moedas(self):
        self.moedas_coletadas = 0

    def esta_no_chao(self):
        return self.rect.colliderect(floor.rect) and self.velocidade_vertical >= 0

    def morte(self):
        if self.rect.colliderect(obstaculo1.rect):
            self.vidas -= 1
            if self.vidas <= 0:
                self.game_over()
                self.resetar_posicao()
            else:
                self.resetar_posicao()

    def resetar_posicao(self):
        self.rect.y = altura_tela - 100
        self.rect.x = largura_tela - 790
        self.velocidade_vertical = 0

    def game_over(self):
        fonte = pygame.font.Font(None, 36)
        mensagem = fonte.render("Game Over", True, (0, 0, 0))
        mensagem_rect = mensagem.get_rect(center=(largura_tela // 2, altura_tela // 2))
        screen.blit(mensagem, mensagem_rect)
        pygame.display.flip()
        sleep(2)
        self.vidas = 3  # Restaura as vidas ao reiniciar o jogo
        self.reset_moedas()

    def show_coins(self):
        fonte = pygame.font.Font(None, 36)
        mensagem = fonte.render(f"{self.moedas_coletadas}", True, (0, 0, 0))
        mensagem_rect = mensagem.get_rect(topright=(largura_tela - 10, 10))
        screen.blit(mensagem, mensagem_rect)
        pygame.display.flip()

    def desenhar_coracoes(self):
        coracao_rect = self.coracao.get_rect()
        for i in range(self.vidas):
            coracao_rect.x = 10 + i * (coracao_rect.width + 5)
            coracao_rect.y = 10
            screen.blit(self.coracao, coracao_rect)


class Floor:
    def __init__(self):
        self.rect = pygame.Rect(0, altura_tela - 40, largura_tela, 40)
        self.color = (0, 255, 0)


class Obstaculo:
    def __init__(self):
        self.image = pygame.image.load("static/TESTE.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = altura_tela - 55


class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load("static/COIN.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x # largura_tela - 90
        self.rect.y = y # altura_tela - 95

    def start(self):
        if self.rect.colliderect(jogador1.rect):
            jogador1.coletada()
            print("coletou")


# Inicialização
pygame.init()
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("JOGO AI")
fundo = pygame.image.load("static/landscape.jpg")
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

jogador1 = Jogador()
floor = Floor()
obstaculo1 = Obstaculo()
HUB_COINS = Coin(largura_tela - 60, 12)
COIN1 = Coin(largura_tela - 90, altura_tela - 65)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))
    screen.blit(fundo, (0, 0))
    pygame.draw.rect(screen, floor.color, floor.rect)  # desenha o chão
    pygame.draw.rect(screen, jogador1.color, jogador1.rect)  # desenha o player
    screen.blit(obstaculo1.image, obstaculo1.rect)  # desenha o obstaculo
    screen.blit(HUB_COINS.image, HUB_COINS.rect)
    screen.blit(COIN1.image, COIN1.rect)


    keys = pygame.key.get_pressed()
    jogador1.mover(keys)
    jogador1.morte()
    jogador1.desenhar_coracoes()
    jogador1.show_coins()
    COIN1.start()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
