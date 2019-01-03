import pygame
import StartGame
import sys

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ans_font = pygame.font.SysFont("monospace", 40)
ask_font = pygame.font.SysFont("monospace", 75)
win_font = pygame.font.SysFont('monospace', 75)


def end_of_game_display(screen):
    pygame.draw.rect(screen, BLACK, (100, 100, 400, 400), 0)
    pygame.draw.rect(screen, BLUE, (100, 100, 400, 400), 5)
    play_again_display(screen)


def play_again_display(screen):
    pygame.draw.rect(screen, BLACK, (150, 400, 100, 50), 0)
    pygame.draw.rect(screen, BLUE, (150, 400, 100, 50), 3)
    pygame.draw.rect(screen, BLACK, (350, 400, 100, 50), 0)
    pygame.draw.rect(screen, BLUE, (350, 400, 100, 50), 3)
    yes = ans_font.render("Yes", 1, YELLOW)
    no = ans_font.render("No", 1, YELLOW)
    play = ask_font.render("Play Again?", 1, YELLOW)
    screen.blit(play, [160, 300])
    screen.blit(yes, [175, 415])
    screen.blit(no, [380, 415])


def highlight_box(screen, pos):
    if 250 > pos[0] > 150 and 450 > pos[1] > 400:
        pygame.draw.rect(screen, YELLOW, (150, 400, 100, 50), 0)
        pygame.draw.rect(screen, BLUE, (150, 400, 100, 50), 3)
        yes = ans_font.render("Yes", 1, BLUE)
        screen.blit(yes, [175, 415])

    if 450 > pos[0] > 350 and 450 > pos[1] > 400:
        pygame.draw.rect(screen, YELLOW, (350, 400, 100, 50), 0)
        pygame.draw.rect(screen, BLUE, (350, 400, 100, 50), 3)
        no = ans_font.render("No", 1, BLUE)
        screen.blit(no, [380, 415])


def play_again(click):
    if 250 > click[0] > 150 and 450 > click[1] > 400:
        return True
    if 450 > click[0] > 350 and 450 > click[1] > 400:
        return False
    else:
        return
