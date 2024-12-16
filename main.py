import pygame

from checkers.board import Board
from checkers.constants import WIDTH, HEIGHT, FPS


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Damas")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_board(WINDOW)
        pygame.display.update()

    pygame.quit()

main()