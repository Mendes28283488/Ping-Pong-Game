import pygame
import time
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

#Classes:

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

#Groups:
            
paddles = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

player_paddle = Paddle(770, 250, 5)

paddles.add(player_paddle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    paddles.update()

    screen.fill(BLACK)
    paddles.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)