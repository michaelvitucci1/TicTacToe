import pygame
import StartGame
import EndSequence
from copy import deepcopy
import sys

NEW_GAME = True
PLAYER_1 = 1
PLAYER_2 = 2
TURN = 0
HEIGHT = 3
WIDTH = 3
SQUARE_SIZE = 200
YELLOW = (255, 255, 0)
win_font = pygame.font.SysFont('monospace', 75)

while NEW_GAME:
    board = StartGame.create_board()
    pygame.init()
    screen_width = WIDTH * SQUARE_SIZE
    screen_height = HEIGHT * SQUARE_SIZE
    size = (screen_height, screen_width)
    screen = pygame.display.set_mode(size)
    StartGame.draw_board(screen, board)
    pygame.display.update()
    winner = None
    GAME_START = True
    INVALID_MOVE = False
    GAME_END = False
    while GAME_START:

        for event in pygame.event.get():

            if GAME_END:
                EndSequence.end_of_game_display(screen)
                StartGame.winner_display(screen, winner, board)
                pygame.display.update()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if not GAME_END:
                    temp_board = deepcopy(board)
                    StartGame.draw_board(screen, board)
                    if TURN == 0:
                        StartGame.player_move_graphic(PLAYER_1, temp_board, event.pos, screen)
                        pygame.display.update()
                    if TURN == 1:
                        StartGame.player_move_graphic(PLAYER_2, temp_board, event.pos, screen)
                        pygame.display.update()
                if GAME_END:
                    EndSequence.highlight_box(screen, event.pos)
                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = event.pos

                if GAME_END:
                    NEW_GAME = EndSequence.play_again(click)
                    if NEW_GAME is not None:
                        GAME_START = False

                if not StartGame.valid_move(board, click) and GAME_START and not GAME_END:
                    message = win_font.render("Please choose a", 1, YELLOW)
                    message2 = win_font.render("valid location.", 1, YELLOW)
                    screen.blit(message, [100, 250])
                    screen.blit(message2, [130, 300])
                    pygame.display.update()
                    INVALID_MOVE = True
                    StartGame.draw_board(screen, board)
                    continue

                # player 1 make a move
                if TURN == 0 and GAME_START and not GAME_END:
                    board = StartGame.player_move_graphic(PLAYER_1, board, click, screen)
                    pygame.display.update()

                    if StartGame.is_winner(PLAYER_1, board):
                        winner = PLAYER_1
                        GAME_END = True

                # player 2 make a move
                if TURN == 1 and GAME_START and not GAME_END:
                    board = StartGame.player_move_graphic(PLAYER_2, board, click, screen)
                    pygame.display.update()
                    if StartGame.is_winner(PLAYER_2, board):
                        winner = PLAYER_2
                        GAME_END = True

                if StartGame.is_scratch(board) and GAME_START and not GAME_END:
                    GAME_END = True

                # alternate turns
                TURN = (TURN + 1) % 2

pygame.quit()
