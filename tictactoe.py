#Tictactoe.py

import pygame, sys
import numpy as np

# initializines pygame
pygame.init()

# --------
# CONTANTS
# --------
WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH =15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//2 - SQUARE_SIZE//6
CIRCILE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4
#rgb : red green blue
RED = (225, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCILE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
#print(board)

#pygame.draw.line( screen, RED, (10, 10), (300, 300), 10 )

def draw_lines():
    # 1 horizontal
    pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
    # 2 hoeizontal
    pygame.draw.line( screen, LINE_COLOR, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH )

    # 1 vertical
    pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    # 2 vertical
    pygame.draw.line( screen, LINE_COLOR, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row] [col] == 1:
                pygame.draw.circle( screen, CIRCILE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCILE_WIDTH )
            elif board[row] [col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE ), CROSS_WIDTH )

def mark_square(row, col, player):
    board[row] [col] = player

def available_square(row, col):
    return board [row] [col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row] [col] == 0:
                return False

    return True

def check_player_win(player):

    # vertical win check
    for col in range(BOARD_COLS):
        if board[0] [col] == player and board[1] [col] == player and board[2] [col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row] [0] == player and board[row] [1] == player and board[row] [2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2] [0] == player and board[1][1] == player and board[0] [2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal win check
    if board[0] [0] == player and board[1] [1] == player and board[2] [2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCILE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCILE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15 )

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCILE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15,HEIGHT - 15 ), (WIDTH - 15, 15), 15 )

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCILE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line( screen, color, (15,15), (WIDTH -15, HEIGHT -15), 15 )

def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row] [col] = 0

draw_lines()

player = 1
game_over = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square( clicked_row, clicked_col ):
                mark_square( clicked_row, clicked_col, player )
                if check_player_win( player ):
                    game_over = True
                player = player % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()