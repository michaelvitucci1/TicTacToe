import numpy
import pygame

HEIGHT = 3
WIDTH = 3
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
SQUARE_SIZE = 200
MARGIN = 10
WEIGHT = 5
PLAYER_1 = 1
PLAYER_2 = 2
pygame.font.init()
win_font = pygame.font.SysFont('monospace', 75)


def create_board():
    board = numpy.zeros((HEIGHT, WIDTH))
    return board


def draw_board(screen, board):
    screen.fill(BLACK)
    for i in range(HEIGHT - 1):
        pygame.draw.line(screen, BLUE, [0, (SQUARE_SIZE * (i + 1))], [(SQUARE_SIZE * 3), (SQUARE_SIZE * (i + 1))], 5)
        pygame.draw.line(screen, BLUE, [(SQUARE_SIZE * (i + 1)), 0], [(SQUARE_SIZE * (i + 1)), (SQUARE_SIZE * 3)], 5)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if board[col][row] == PLAYER_1:
                draw_player1(screen, row, col)
            if board[col][row] == PLAYER_2:
                draw_player2(screen, row, col)


def player_move(player, board):
    try:
        y = int(input("Player " + str(player) + ": What is the y coordinate for your move (0 - 2)"))
    except ValueError:
        print("Please enter an integer.")
        player_move(player, board)
    try:
        x = int(input("Player " + str(player) + ": What is the x coordinate for your move (0 - 2)"))
    except ValueError:
        print("Please enter an integer.")
        player_move(player, board)

    if board[y][x] == 0:
        board[y][x] = player
        return board
    else:
        print("This location is already taken. Please choose again Player " + str(player) + ".")
        return player_move(player, board)


def player_move_graphic(player, board, click, screen):
    col = int(click[0] / SQUARE_SIZE)
    row = int(click[1] / SQUARE_SIZE)
    if board[row][col] == 0:
        board[row][col] = player
        if player == PLAYER_1:
            draw_player1(screen, col, row)
        if player == PLAYER_2:
            draw_player2(screen, col, row)
        return board


def draw_player1(screen, col, row):
    pygame.draw.circle(screen, RED,
                       [((col * SQUARE_SIZE) + int(SQUARE_SIZE / 2)),
                        ((row * SQUARE_SIZE) + int(SQUARE_SIZE / 2))], int(SQUARE_SIZE / 2) - MARGIN, WEIGHT)


def draw_player2(screen, col, row):
    pygame.draw.line(screen, GREEN,
                     [((SQUARE_SIZE * col) + SQUARE_SIZE - MARGIN), ((SQUARE_SIZE * row) + MARGIN)],
                     [((SQUARE_SIZE * col) + MARGIN), ((SQUARE_SIZE * row) + SQUARE_SIZE - MARGIN)], WEIGHT)
    pygame.draw.line(screen, GREEN, [((SQUARE_SIZE * col) + MARGIN), ((SQUARE_SIZE * row) + MARGIN)],
                     [((SQUARE_SIZE * col) + SQUARE_SIZE - MARGIN),
                      ((SQUARE_SIZE * row) + SQUARE_SIZE - MARGIN)], WEIGHT)


def valid_move(board, click):
    col = int(click[0] / SQUARE_SIZE)
    row = int(click[1] / SQUARE_SIZE)
    if board[row][col] == 0:
        return True
    else:
        return False


def is_winner(player, board):
    # check horizontal
    for i in range(HEIGHT):
        count = 0
        for j in range(WIDTH):
            if int(board[i][j]) == player:
                count += 1
                if count == 3:
                    return True

    # check vertical
    for i in range(HEIGHT):
        count = 0
        for j in range(WIDTH):
            if int(board[j][i]) == player:
                count += 1
                if count == 3:
                    return True
    # check negative diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == player:
        return True

    # check positive diagonal
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] == player:
        return True

    return False


def winner_display(screen, winner, board):
    xpos = 125
    ypos = 150
    scratchx = 190
    scratchy = 150

    if winner == PLAYER_1:
        message = win_font.render("Player " + str(winner) + " Wins!", 1, RED)
        screen.blit(message, (xpos, ypos))
    if winner == PLAYER_2:
        message = win_font.render("Player " + str(winner) + " Wins!", 1, GREEN)
        screen.blit(message, (xpos, ypos))
    if is_scratch(board) and winner is None:
        message = win_font.render("Scratch!", 1, YELLOW)
        screen.blit(message, (scratchx, scratchy))


def is_scratch(board):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if int(board[i][j]) == 0:
                return False
    return True
