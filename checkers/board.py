import pygame

from .constants import *
from .piece import Piece


class Board:
    def __init__(self) -> None:
        self.board = []
        self.black_left = self.white_left = 12        # Número Inicial de Peças
        self.black_kings = self.white_kings = 0      # Número Inicial de Damas (Em inglês, é chamado de 'King')
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
                        self.board[row].append(Piece(row, col, BLACK_PIECE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE_PIECE))
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
    

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE_PIECE:
                self.white_kings += 1
            else:
                self.black_kings += 1
    

    def get_piece(self, row, col):
        return self.board[row][col]
    

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1

        if piece.color == WHITE_PIECE or piece.king:
            pass

        if piece.color == BLACK_PIECE or piece.king:
            pass

    
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board.get_piece(r, left)
            if current == 0:
                if skipped and not last:
                    break
            left -= 1


    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        pass