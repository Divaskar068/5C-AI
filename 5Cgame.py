import pygame
import sys
import math
from random import randint

from constants import *
from c4 import Connect4
from c4AI import Connect4AI


PLAYER1 = 1
PLAYER2 = 2

import pygame

pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



# Load the background image
background_image = pygame.image.load("CC5bg.png")

# Resize the background image to match the window dimensions
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


# Set the font for the text
font = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 58)
font2 = pygame.font.Font(None, 90)

# Create the text objects
#title_text1 = font2.render("    CONNECT 5", True, (0, 0, 0))
#title_text = font.render("WELCOME TO CHRIS CONNECT!", True, (0, 0, 0))
#start_text = font.render("Press 1 - Multiplayer", True, (0, 0, 0))
#start_text2 = font.render("Press 2 - AI", True, (0, 0, 0))

# Position the text objects on the screen

#title_text1_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, 100))
#title_text_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, 200))
#start_text_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, 300))
#start_text2_rect = start_text.get_rect(center=(WINDOW_WIDTH/2, 400))

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Start the game
                game_type = "HUMAN"
                running = False
            if event.key == pygame.K_2:
                game_type="AI"   
                running = False
    
    # Draw the background and text
    screen.blit(background_image, (0, 0))
    #screen.blit(title_text1, title_text1_rect)
    #screen.blit(title_text, title_text_rect)
    #screen.blit(start_text, start_text_rect)
    #screen.blit(start_text2, start_text2_rect)
    
    # Update the screen
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()


pygame.init()
screen = pygame.display.set_mode(size)

if game_type == "HUMAN":
    game = Connect4(screen, PLAYER1, PLAYER2)
else:
    game = Connect4AI(screen, PLAYER1, PLAYER2)
board = game.create_board()
game_over = False
game.draw_board(board)
pygame.display.update()

turn = PLAYER1

myfont = pygame.font.SysFont("monospace", int(SQUARESIZE*0.75))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

            posx = event.pos[0]
            if turn == PLAYER1:
                pygame.draw.circle(
                    screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            elif turn == PLAYER2:
                pygame.draw.circle(
                    screen, WHITE, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

            # Ask for Player1 Input
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))
            if turn == PLAYER1:
                if game.is_valid_location(board, col):
                    row = game.get_next_open_row(board, col)
                    game.drop_piece(board, row, col, PLAYER1)

                    if game.winning_move(board, PLAYER1):
                        label = myfont.render("----DRAW----", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn = (turn % 2) + 1

                    game.draw_board(board)
            # Ask for Player 2 Input
            elif turn == PLAYER2 and game_type == "HUMAN":
                if game.is_valid_location(board, col):
                    row = game.get_next_open_row(board, col)
                    game.drop_piece(board, row, col, PLAYER2)

                    if game.winning_move(board, PLAYER2):
                        label = myfont.render("----DRAW----", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn = (turn % 2) + 1

                    game.draw_board(board)

            # AI Plays as Player2
            if turn == PLAYER2 and game_type == "AI" and not game_over:
                # col = randint(0, COLUMN_COUNT-1)
                # while not game.is_valid_location(board, col):
                #     col = randint(0, COLUMN_COUNT-1)

                # col = game.pick_best_move(board, PLAYER2)
                col, minimax_score = game.minimax(board, 5, -math.inf, math.inf, True)

                if game.is_valid_location(board, col):
                    # pygame.time.wait(500)
                    row = game.get_next_open_row(board, col)
                    game.drop_piece(board, row, col, PLAYER2)

                    if game.winning_move(board, PLAYER2):
                        label = myfont.render("-PLAYER 2 WINS-", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True

                    game.draw_board(board)

                    turn = (turn % 2) + 1

    if game_over:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()