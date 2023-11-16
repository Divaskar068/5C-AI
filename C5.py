import numpy as np
import pygame

from constants import *


class Connect4:
    def __init__(self, screen, player1, player2):
        self.screen = screen
        self.player1 = player1
        self.player2 = player2

    def create_board(self):
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def winning_move(self, board, piece):
        # Check horizontal locations
        for c in range(COLUMN_COUNT-4):
            for r in range(ROW_COUNT):
                #if all([board[r][c+i] == piece for i in range(WINDOW_LENGTH)]):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4] == piece:
                    return True

        # Check vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-4):
                #if all([board[r+i][c] == piece for i in range(WINDOW_LENGTH)]):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT-4):
            for r in range(ROW_COUNT-4):
                #if all([board[r+i][c+i] == piece for i in range(WINDOW_LENGTH)]):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT-4):
            for r in range(4, ROW_COUNT):
                #if all([board[r-i][c+i] == piece for i in range(WINDOW_LENGTH)]):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                    return True

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == self.player1:
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == self.player2:
                    pygame.draw.circle(self.screen, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()
