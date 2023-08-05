import pygame
from sys import exit

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('This game')
clock = pygame.time.Clock()

# constant
bar_y_cord = 0
left_bar_x_cord = 5
right_bar_x_cord = 785
bar_width = 10
bar_height = 60

# left bar
left_bar_surf = pygame.Surface((bar_width, bar_height))
left_bar_surf.fill('red')
left_bar_rect = left_bar_surf.get_rect(topleft=(left_bar_x_cord, bar_y_cord))

# right bar
right_bar_surf = pygame.Surface((bar_width, bar_height))
right_bar_rect = right_bar_surf.get_rect(topleft=(right_bar_x_cord, bar_y_cord))
right_bar_surf.fill('red')

# ball
ball_dims, ball_x, ball_y = 10, 400, 200
ball_surf = pygame.Surface((ball_dims, ball_dims))
ball_surf.fill('white')
ball_rect = ball_surf.get_rect(center=(ball_x, ball_y))

# moving variables
move_up = False
move_down = False
playing = False
x_speed = -2
y_speed = 0
start_time = pygame.time.get_ticks() // 1000
score = None

# intro screen
def display_score():
    current_time = int(pygame.time.get_ticks()/500) - start_time
    score_surf = my_font.render(f'Score: {current_time}', False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


def reset_game():
    ball_rect.center = (ball_x, ball_y)
    left_bar_rect.center = (left_bar_x_cord, bar_y_cord)
    right_bar_rect.center = (right_bar_x_cord, bar_y_cord)

while True:

    if playing:
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

        screen.blit(left_bar_surf, left_bar_rect)
        screen.blit(right_bar_surf, right_bar_rect)
        screen.blit(ball_surf, ball_rect)
        # y_cord += 1
        if move_up and left_bar_rect.y >= 0:
            right_bar_rect.y -= 4
            left_bar_rect.y -= 4
        elif move_down and left_bar_rect.y <= 340:
            left_bar_rect.y += 4
            right_bar_rect.y += 4

        ball_rect.x += x_speed
        ball_rect.y += y_speed
        collision = pygame.Rect.colliderect(left_bar_rect, ball_rect)

        if left_bar_rect.colliderect(ball_rect):
            x_speed = 4
            if move_down:
                y_speed = 2
            if move_up:
                y_spped = -2

        elif right_bar_rect.colliderect(ball_rect):
            x_speed = -4
            if move_down:
                y_speed = 2
            elif move_up:
                y_speed = -2
        else:
            if ball_rect.x < left_bar_rect.x or ball_x > right_bar_rect.x:
                playing = False
                score = current_time = int(pygame.time.get_ticks()/500) - start_time

 

        if ball_rect.y <= 0:
            y_speed = 2
        elif ball_rect.y >= SCREEN_HEIGHT:
            y_speed = -2
        display_score()

    else:
        screen.fill('gray')
        reset_game()
        playing = False

        if score is not None:
            score_surf = my_font.render(f'You lost!. Your score is: {score}.', False, (255,0,0))
            score_rect = score_surf.get_rect(center=(400, 50))
            screen.blit(score_surf, score_rect) 
        
        play_message = my_font.render(f'Press SPACE to start a new game.', False, (255, 0, 0))
        play_message_rect = play_message.get_rect(center=(400, 100))
        screen.blit(play_message, play_message_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    playing = True

    pygame.display.update()
    clock.tick(60)
