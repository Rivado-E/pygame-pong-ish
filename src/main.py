import pygame
from sys import exit
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('This game')
clock = pygame.time.Clock()

bar_y_cord = 0
left_bar_x_cord = 5
right_bar_x_cord = 785
bar_width = 10
bar_height = 60

left_bar_surf = pygame.Surface((bar_width, bar_height))
left_bar_surf.fill('red')
left_bar_rect = left_bar_surf.get_rect(topleft=(left_bar_x_cord, bar_y_cord))

right_bar_surf = pygame.Surface((bar_width, bar_height))
right_bar_rect = right_bar_surf.get_rect(topleft=(right_bar_x_cord, bar_y_cord))
right_bar_surf.fill('red')



move_up = False
move_down = False

while True:

    screen.fill('black')
    # closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False
            if event.key == pygame.K_DOWN:
                move_up = False
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    screen.blit(left_bar_surf, (left_bar_x_cord, bar_y_cord))
    screen.blit(right_bar_surf, (right_bar_x_cord, bar_y_cord))
    # y_cord += 1
    if move_up and bar_y_cord >= 0:
        bar_y_cord -= 4
    elif move_down and bar_y_cord <= 340:
        bar_y_cord += 4

    pygame.display.update()
    clock.tick(60)

