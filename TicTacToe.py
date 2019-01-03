import pygame
import StartGame
import sys

print("Hello, let's play some TicTacToe!")


GAME_START = True
NEW_GAME = True

PLAYER_1 = 1
PLAYER_2 = 2
TURN = 0

while NEW_GAME:
    board = StartGame.create_board()
    print(board)
    while GAME_START:

    # player 1 make a move
        if TURN == 0:
            board = StartGame.player_move(PLAYER_1, board)
            if StartGame.is_winner(PLAYER_1, board):
                winner = PLAYER_1
                print("Player " + str(PLAYER_1) + " Wins!")
                GAME_START = False
            print(board)

        # player 2 make a move
        if TURN == 1:
            board = StartGame.player_move(PLAYER_2, board)
            if StartGame.is_winner(PLAYER_2, board):
                winner = PLAYER_2
                print("Player " + str(PLAYER_2) + " Wins!")
                GAME_START = False
            print(board)

        if StartGame.is_scratch(board):
            GAME_START = False
            print("The game is a Scratch!")

        # alternate turns
        TURN = (TURN + 1) % 2
    restart = input("Do you want to play again?").upper()

    if restart != "YES":
        NEW_GAME = False
    else:
        GAME_START = True
