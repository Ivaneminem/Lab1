import pygame
from config import WIDTH, HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)