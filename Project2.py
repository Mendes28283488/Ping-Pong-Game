import pygame
import time
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
player_score = 0
opponent_score = 0
winning_score = 1
font = pygame.font.Font(None, 72)
win_text = font.render("PL1 WIN", True, BLACK)
lose_text = font.render("PL2 WIN", True, BLACK)
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

#Classes:

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 5

class OpponentPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += 5


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
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
opponent_paddle = OpponentPaddle(10, 250, 5)
ball = Ball()

paddles.add(player_paddle, opponent_paddle)
ball_group.add(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    paddles.update()
    ball_group.update()

    if ball.rect.left <= 0:
        opponent_score += 1
        if opponent_score >= winning_score:
            screen.blit(lose_text, (300, 250))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
        else:
            ball.rect.center = (400 , 300)

    if ball.rect.right >= WIDTH:
        player_score += 1
        if player_score >= winning_score:
            screen.blit(win_text, (300, 250))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
        else:
            ball.rect.center = (400 , 300)

    screen.fill(WHITE)
    paddles.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)