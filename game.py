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
    def __init__(self, difficulty):
        if difficulty == 'easy':
            self.ball_speed = EASY_BALL_SPEED
            self.block_rows = EASY_BLOCK_ROWS
            self.block_cols = EASY_BLOCK_COLS
        else:
            self.ball_speed = HARD_BALL_SPEED
            self.block_rows = HARD_BLOCK_ROWS
            self.block_cols = HARD_BLOCK_COLS

        self.paddle = Paddle()
        self.ball = Ball(self.ball_speed)
        self.block = Block(self.block_rows, self.block_cols)
        self.fps = FPS
        self.score = 0

    def save_score(self):
        with open(SCORE_FILE, 'a') as file:
            file.write(f'Score: {self.score}\n')