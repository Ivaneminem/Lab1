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

    def move(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('white'), self.rect.center, BALL_RADIUS)

    def check_collision(self, paddle, blocks, colors):
        if self.rect.centerx < BALL_RADIUS or self.rect.centerx > WIDTH - BALL_RADIUS:
            self.dx = -self.dx
        if self.rect.centery < BALL_RADIUS:
            self.dy = -self.dy

        if self.rect.colliderect(paddle.rect) and self.dy > 0:
            self.dx, self.dy = detect_collision(self.dx, self.dy, self.rect, paddle.rect)

        hit_index = self.rect.collidelist(blocks)
        if hit_index != -1:
            hit_rect = blocks.pop(hit_index)
            hit_color = colors.pop(hit_index)
            self.dx, self.dy = detect_collision(self.dx, self.dy, self.rect, hit_rect)
            hit_rect.inflate_ip(self.rect.width * 3, self.rect.height * 3)
            return hit_rect, hit_color
        return None, None