import pygame
import os
from game import Game
from helpers import draw_text, get_highest_score

# Constants
WIDTH, HEIGHT = 1200, 800
IMG_PATH = '1.jpg'
SCORE_FILE = 'scores.txt'

# Initialize pygame
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load(IMG_PATH).convert()

