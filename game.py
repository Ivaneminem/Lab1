import pygame
from paddle import Paddle
from ball import Ball
from block import Block
from helpers import draw_text
from config import WIDTH, HEIGHT, IMG_PATH, SCORE_FILE, FPS, EASY_BALL_SPEED, HARD_BALL_SPEED, EASY_BLOCK_ROWS, EASY_BLOCK_COLS, HARD_BLOCK_ROWS, HARD_BLOCK_COLS

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load(IMG_PATH).convert()

class Game:
