import pygame

# Jogo
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FPS = 60


# Cores
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
WHITE_PIECE = (234, 180, 143)
BLACK_PIECE = (82, 58, 58)
BLACK_BOARD_SQUARE = (186, 103, 70)
WHITE_BOARD_SQUARE = (253, 227, 185)


# Assets
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))