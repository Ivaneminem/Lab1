import pygame
from random import randrange as rnd
from config import BLOCK_WIDTH, BLOCK_HEIGHT

class Block:
    def __init__(self, rows, cols):
        self.blocks = [pygame.Rect(10 + 120 * i, 10 + 70 * j, BLOCK_WIDTH, BLOCK_HEIGHT) for i in range(cols) for j in range(rows)]
        self.colors = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for _ in range(cols * rows)]