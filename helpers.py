import pygame
import os
from config import SCORE_FILE


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, pygame.Color('white'))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def get_highest_score(score_file=SCORE_FILE):
    if not os.path.exists(score_file):
        return 0
    with open(score_file, 'r') as file:
        scores = file.readlines()
        scores = [int(score.strip().split()[-1]) for score in scores if score.strip()]
        return max(scores) if scores else 0
