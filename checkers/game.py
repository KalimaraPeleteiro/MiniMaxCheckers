import pygame

from .board import Board
from .constants import * 


class Game:
    def __init__(self, window):
        self.selected = None
        self.board = Board()
        self.turn = WHITE_PIECE
        self.valid_moves = {}
        self.window = window

    def update(self):
        self.board.draw_board(self.window)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
    
    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result: 
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True
    

    def change_turn(self):
        if self.turn == WHITE_PIECE:
            self.turn = BLACK_PIECE
        else:
            self.turn = WHITE_PIECE