import pygame
from config import WIDTH, HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, left, right):
        if left and self.rect.left > 0:
            self.rect.left -= PADDLE_SPEED
        if right and self.rect.right < WIDTH:
            self.rect.right += PADDLE_SPEED