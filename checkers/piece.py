import pygame

from .constants import *


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False       # Damas no jogo em inglês é 'King'

        if self.color == WHITE_PIECE:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calculate_position()


    # Utilizado para centralizar a peça no quadrado em que está.
    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def kinging(self):
        self.king = True

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING 
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

    def __repr__(self) -> str:
        return str(self.color)