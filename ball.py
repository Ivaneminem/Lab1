import pygame
from random import randrange as rnd
from helpers import detect_collision
from config import WIDTH, HEIGHT, BALL_RADIUS

class Ball:
    def __init__(self, speed):
        ball_diameter = int(BALL_RADIUS * 2 ** 0.5)
        self.rect = pygame.Rect(rnd(ball_diameter, WIDTH - ball_diameter), HEIGHT // 2, ball_diameter, ball_diameter)
        self.dx, self.dy = 1, -1
        self.speed = speed