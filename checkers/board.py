import pygame

from .constants import *
from .piece import Piece


class Board:
    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12        # Número Inicial de Peças
        self.red_kings = self.white_kings = 12      # Número Inicial de Damas (Em inglês, é chamado de 'King')
        self.create_board()


    # Desenhando o tabuleiro em formato de damas.
    @staticmethod
    def draw_squares(window):
        window.fill(BLACK_BOARD_SQUARE)

        for row in range(ROWS):
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(window, WHITE_BOARD_SQUARE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    # Definindo as posições das peças em tabuleiro. 0 representa nenhuma peça na casa.
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE_PIECE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK_PIECE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    # Desenhando o tabuleiro COM as peças.
    def draw_board(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)