import pygame
import pytest
from paddle import Paddle
from ball import Ball
from block import Block
from game import Game
from config import WIDTH, HEIGHT, BALL_RADIUS, BLOCK_WIDTH, BLOCK_HEIGHT
from helpers import detect_collision, get_highest_score


@pytest.fixture(scope="module")
def pygame_init():
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def paddle(pygame_init):
    return Paddle()


def test_paddle_initial_position(paddle):
    assert paddle.rect.x == WIDTH // 2 - paddle.rect.width // 2


def test_paddle_move_left(paddle):
    initial_x = paddle.rect.x
    paddle.move(True, False)  # Move left
    assert paddle.rect.x < initial_x


def test_paddle_move_right(paddle):
    initial_x = paddle.rect.x
    paddle.move(False, True)  # Move right
    assert paddle.rect.x > initial_x


def test_paddle_no_move(paddle):
    initial_x = paddle.rect.x
    paddle.move(False, False)  # No move
    assert paddle.rect.x == initial_x


@pytest.fixture
def ball(pygame_init):
    return Ball(speed=4)


def test_ball_initial_position(ball):
    assert BALL_RADIUS <= ball.rect.x <= WIDTH - BALL_RADIUS
    assert ball.rect.y == HEIGHT // 2


def test_ball_move(ball):
    initial_position = ball.rect.topleft
    ball.move()
    assert ball.rect.topleft != initial_position


@pytest.fixture
def block(pygame_init):
    return Block(rows=3, cols=10)


def test_block_initialization(block):
    assert len(block.blocks) == 30  # 3 rows * 10 cols
    assert all(b.width == BLOCK_WIDTH and b.height == BLOCK_HEIGHT for b in block.blocks)


def test_detect_collision():
    ball_rect = pygame.Rect(50, 50, 20, 20)
    paddle_rect = pygame.Rect(50, 70, 100, 20)
    dx, dy = detect_collision(1, 1, ball_rect, paddle_rect)
    assert dx == 1 and dy == -1


def test_get_highest_score(tmp_path):
    score_file = tmp_path / "scores.txt"
    score_file.write_text("Score: 10\nScore: 20\nScore: 5\n")
    assert get_highest_score(score_file) == 20


@pytest.fixture
def game(pygame_init, tmp_path):
    score_file = tmp_path / "scores.txt"
    game_instance = Game(difficulty='easy')
    game_instance.score_file = score_file  # Додаємо атрибут score_file для зберігання шляху
    return game_instance


def test_game_initialization(game):
    assert game.ball_speed == 4
    assert game.block_rows == 3
    assert game.block_cols == 10
    assert game.score == 0


def test_game_save_score(tmp_path, game):
    score_file = tmp_path / "scores.txt"
    game.score = 15
    game.save_score(score_file)
    with open(score_file, 'r') as f:
        scores = f.readlines()
    assert scores[-1].strip() == "Score: 15"
