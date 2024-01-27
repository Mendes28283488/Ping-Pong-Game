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


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (15, 15), 15)
        self.rect = self.image.get_rect(center=(400, 300))
        self.speedy = 5
        self.speedx = 5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1

        if pygame.sprite.spritecollide(self, paddles, False):
            self.speedx *= -1

#Groups:
            
paddles = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

player_paddle = Paddle(770, 250, 5)
ball = Ball()

paddles.add(player_paddle)
ball_group.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    paddles.update()
    ball_group.update()

    screen.fill(BLACK)
    paddles.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)