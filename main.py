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


def main_menu():
    highest_score = get_highest_score()
    while True:
        sc.blit(img, (0, 0))
        draw_text(sc, "Arkanoid", 100, WIDTH / 2, HEIGHT / 4)
        draw_text(sc, f"Highest Score: {highest_score}", 32, WIDTH / 2, HEIGHT / 2 - 50)
        draw_text(sc, "Press 1 for Easy, 2 for Hard, or Q to Quit", 24, WIDTH / 2, HEIGHT / 2 + 50)
        pygame.display.flip()

        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_1:
                        Game('easy').run()
                        return
                    if event.key == pygame.K_2:
                        Game('hard').run()
                        return
        except Exception as e:
            print(f"Error processing events: {e}")


if __name__ == "__main__":
    if not os.path.exists(SCORE_FILE):
        open(SCORE_FILE, 'w').close()
    main_menu()
    pygame.quit()
