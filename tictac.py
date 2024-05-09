import numpy as np
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

bg_image = pygame.image.load("background.png")
bg_image = pygame.transform.scale(bg_image, (600,600))
o_image = pygame.image.load("o.png")
x_image = pygame.image.load("x.png")
# Colors
WHITE = (255, 255, 255)
PLAYER_O_COLOR = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Board representation
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Fonts
font = pygame.font.Font(None, 100)



def draw_symbols():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            symbol = board[row][col]
            if symbol == 'X':
                draw_x(col, row)
            elif symbol == 'O':
                draw_o(col, row)

def draw_x(col, row):

    screen.blit(x_image,((col * SQUARE_SIZE)+8, (row * SQUARE_SIZE)+8))
def draw_o(col, row):

    screen.blit(o_image,((col * SQUARE_SIZE )+ 8, (row * SQUARE_SIZE) + 8))
def is_winner(player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False

def is_board_full():
    return all(all(cell != '' for cell in row) for row in board)

def get_empty_cells():
    return [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == '']

def minimax(depth, player):
    if is_winner('O'):
        return 1
    elif is_winner('X'):
        return -1
    elif is_board_full():
        return 0

    if player:
        max_eval = float('-inf')
        for cell in get_empty_cells():
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(depth + 1, False)
            board[cell[0]][cell[1]] = ''
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in get_empty_cells():
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(depth + 1, True)
            board[cell[0]][cell[1]] = ''
            min_eval = min(min_eval, eval)
        return min_eval

def best_move():
    best_score = float('-inf')
    best_move = None
    for cell in get_empty_cells():
        board[cell[0]][cell[1]] = 'O'
        move_score = minimax(0, False)
        board[cell[0]][cell[1]] = ''
        if move_score > best_score:
            best_score = move_score
            best_move = cell
    return best_move

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE

            if board[row][col] == '':
                board[row][col] = 'X'

                if not is_winner('X') and not is_board_full():
                    ai_move = best_move()
                    board[ai_move[0]][ai_move[1]] = 'O'

    # Draw the board
    screen.fill(WHITE)
    screen.blit(bg_image, (0, 0))
    draw_symbols()

    # Check for a winner or a tie
    if is_winner('X'):
        text = font.render("Player X wins!", True,(0,0,0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))



    elif is_winner('O'):
        text = font.render("Player O wins!", True,(0,0,0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))





    elif is_board_full():
        text = font.render("It's a tie!", True,(0,0,0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))




    pygame.display.update()
