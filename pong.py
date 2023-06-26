import random
import pygame
from objects import Ball
from objects import Paddle
from objects import Wall
# maybe use use individual import so i get to know the origin of a object
# from pygame.locals import *

# GLOBAL VAR 
FPS_LIMIT = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BACKGROUND_COLOR = BLACK
PADDLE_COLOR = RED
MENU_SELECTION = 0
LOCAL_SELECTION = 1
PVP = 2
PVE = 3
ONLINE = 4
menu_pervious_selection = 0
sub_menu_pervious_selection = 0
state_selection = MENU_SELECTION

# pygame set up
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
# Toggle fullscreen mode
# pygame.display.toggle_fullscreen()

# All this secion below should be able to put into main
# Paddle
paddle_width = 15
paddle_height = 60
paddle_speed = 10
init_paddle_y = height // 2
left_paddle = Paddle(0, init_paddle_y - paddle_height/2 , paddle_width, paddle_height, paddle_speed, PADDLE_COLOR, height)
right_paddle = Paddle(width - paddle_width, init_paddle_y - paddle_height/2, paddle_width, paddle_height, paddle_speed, PADDLE_COLOR, height)

# Ball
ball_speed = 7
ball_radius = 10
init_ball_x = width //  2  # Shifted to the left by half the ball radius
init_ball_y = height // 2  # Shifted upward by half the ball radius
ball = Ball(init_ball_x, init_ball_y, dx = random.choice([-ball_speed, ball_speed]))

# Wall
wall_height = 1
top_wall = Wall(0 , 0 - wall_height, width, wall_height, RED, height)
bot_wall = Wall(0 , height, width, wall_height, RED, height)

def main():
    # game event
    running = True
    clock = pygame.time.Clock()    
    while running:
        clock.tick(FPS_LIMIT)
        # Draw main menu
        main_menu()

# Two component selection handle and render
def main_menu():
    global state_selection
    if state_selection == MENU_SELECTION:
        menu_options = ["Play Local", "Play Online", "Exit"]
        handle_menu_selection(menu_options)
        main_menu_render(menu_options)
    elif state_selection == LOCAL_SELECTION:
        # Need to handle and render select pve or pvp
        menu_options = ["Player vs Player", "Player vs Bot", ]
        handle_local_selection(menu_options)
        render_local_selection(menu_options)
    elif state_selection == PVP:
        # ingame, game_started, waiting, score_board, ball_out_of_bounds_time, respaen_time
        objs_list = [left_paddle, right_paddle, top_wall, bot_wall]
        game_state = [True, False, True, [0,0], 0, 3000]
        clock2 = pygame.time.Clock()
        while game_state[0]:
            cons_time = clock2.tick(FPS_LIMIT)
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state[1] = True
                        game_state[2] = False
            player_vs_player(game_state, cons_time, objs_list)

    elif state_selection == PVE:
        while True:
            player_vs_bot()
    elif state_selection == ONLINE:
        while True:
            play_online_game()
    else:
        print("main menu func something wrong")
    pygame.display.flip()
    
def player_vs_player(game_state, cons_time, objs_list):
    screen.fill(BACKGROUND_COLOR)
    # game state = [(0)ingame, (1)game_started, (2)waiting, (3)score_board, (4)ball_out_of_bounds_time, (5)respawn_time]
    # Handle
    if not game_state[1]:
        press_space_start(screen)

    elif not game_state[2]:
        draw_score(screen, game_state[3])
        draw_and_update_pos(ball, left_paddle, right_paddle, top_wall, bot_wall, screen, cons_time)        
        check_ball_collides(ball, objs_list)
        if check_out_bound(ball, game_state[3]):
            game_state[4] = pygame.time.get_ticks()
            ball.dx = 0
            ball.dy = 0
            game_state[2] = True
    else:
        draw_score(screen, game_state[3])
        draw_and_update_pos(ball, left_paddle, right_paddle, top_wall, bot_wall, screen, cons_time)
        current_time = pygame.time.get_ticks()  # Get the current time
        elapsed_time = current_time - game_state[4]  # Calculate the elapsed time
        
        count_down_text(screen, game_state[5] - elapsed_time)
        if elapsed_time >= game_state[5]:
            ball.dx = random.choice([-ball_speed, ball_speed])
            ball.dy = 0
            ball.x = init_ball_x
            ball.y = init_ball_y
            game_state[2] = False
    pygame.display.flip()

def handle_menu_selection(menu_options):
    global menu_pervious_selection, state_selection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Handle menu option selection
                menu_pervious_selection = (menu_pervious_selection - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                # Handle menu option selection
                menu_pervious_selection = (menu_pervious_selection + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                # Handle menu option execution
                if menu_pervious_selection == 0:
                    state_selection = 1
                elif menu_pervious_selection == 1:
                    play_online_game()
                elif menu_pervious_selection == 2:
                    pygame.quit()
                    exit()

def main_menu_render(menu_options):
    screen.fill(BLACK)  # Clear the screen
    # Title 
    title_render()
    # Render menu options
    menu_font = pygame.font.Font(None, 36)
    for i, option in enumerate(menu_options):
        text = menu_font.render(option, True, WHITE)
        text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
        hint_y = text_rect.bottom
        screen.blit(text, text_rect)
        # Render an arrow based on the selected options (global var)
        if i == menu_pervious_selection:
                arrow_text = menu_font.render("->", True, WHITE)
                arrow_rect = arrow_text.get_rect(midright=(text_rect.left - 10, text_rect.centery))
                screen.blit(arrow_text, arrow_rect)

    # Print Hint of use arrow key to select options
    menu_font = pygame.font.Font(None, 25)
    hint_text = menu_font.render("Hint: Press arrow keys to select and ENTER to Choose", True, WHITE)
    hint_text_rect = hint_text.get_rect(center=(width // 2, hint_y + 50))
    screen.blit(hint_text, hint_text_rect)
    # pygame.display.flip()  # Update the screen

def title_render():
    title_font = pygame.font.Font(None, 100)
    title_text = title_font.render("PyPong", True, (135, 206, 250))
    title_text_rect = title_text.get_rect(center=(width // 2, height// 3 - 50))
    screen.blit(title_text, title_text_rect)

def handle_local_selection(menu_options):
    global sub_menu_pervious_selection 
    global state_selection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Handle menu option selection
                sub_menu_pervious_selection = (sub_menu_pervious_selection - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                # Handle menu option selection
                sub_menu_pervious_selection = (sub_menu_pervious_selection + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                # Handle menu option execution
                if sub_menu_pervious_selection == 0:
                    state_selection = PVP
                elif sub_menu_pervious_selection == 1:
                    state_selection = PVE
            elif event.key == pygame.K_ESCAPE:
                state_selection = 0
    
def render_local_selection(menu_options):
    screen.fill(BLACK)  # Clear the screen
    # Title 
    title_render()
    # Render menu options
    menu_font = pygame.font.Font(None, 36)
    for i, option in enumerate(menu_options):
        text = menu_font.render(option, True, WHITE)
        text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
        hint_y = text_rect.bottom
        screen.blit(text, text_rect)
        # Render an arrow based on the selected options (global var)
        if i == sub_menu_pervious_selection:
                arrow_text = menu_font.render("->", True, WHITE)
                arrow_rect = arrow_text.get_rect(midright=(text_rect.left - 10, text_rect.centery))
                screen.blit(arrow_text, arrow_rect)

    # Print Hint of use arrow key to select options
    menu_font = pygame.font.Font(None, 25)
    hint_text = menu_font.render("Hint: Press ESC to back out", True, WHITE)
    hint_text_rect = hint_text.get_rect(center=(width // 2, hint_y + 50))
    screen.blit(hint_text, hint_text_rect)
    # pygame.display.flip()  # Update the screen

def draw_and_update_pos(ball, l_paddle, r_paddle, t_wall, b_wall, surface, cons_time):
    ball.draw(surface)
    l_paddle.draw(surface)
    r_paddle.draw(surface)
    t_wall.draw(surface)
    b_wall.draw(surface)

    ball.update_new_pos()
    r_paddle.update_newpos(pygame.K_UP, pygame.K_DOWN)
    l_paddle.update_newpos(pygame.K_w, pygame.K_s)
    r_paddle.cal_velocity(cons_time)
    l_paddle.cal_velocity(cons_time)

def check_ball_collides(ball, list_of_objs):
    for obj in list_of_objs:
        obj.colliderect(ball)

def check_out_bound(ball, score_board):
    if ball.x - ball_radius - 50 > width:
        score_board[1] += 1
        return True
    elif  ball.x + ball_radius + 50 < 0:
        score_board[0] += 1
        return True
    return False

def count_down_text(screen, countdown_time_remaining):
    countdown_time_remaining /= 1000
    if countdown_time_remaining >= 0:
        countdown_font = pygame.font.Font(None, 100)
        countdown_text = countdown_font.render("{:.1f}".format(countdown_time_remaining), True, (255, 255, 255))
        countdown_text_rect = countdown_text.get_rect(center=(width // 2, height // 2))
        screen.blit(countdown_text, countdown_text_rect)

def press_space_start(screen):
    start_font = pygame.font.Font(None, 40)
    start_text = start_font.render("Press SPACE to start the game", True, WHITE)
    start_text_rect = start_text.get_rect(center=(width // 2, height // 2))
    screen.blit(start_text, start_text_rect)

def draw_score(screen, score_board):
    score_font = pygame.font.Font(None, 36)
    score_positions = [(width // 2 + 50, 20), (width // 2 - 50, 20)]

    for i, score in enumerate(score_board):
        score_text = score_font.render(str(score), True, WHITE)
        score_text_rect = score_text.get_rect(center=score_positions[i])
        screen.blit(score_text, score_text_rect)

def player_vs_bot():
    print("")

def play_online_game():
    print("Not yet develope")

if __name__ == "__main__":
    main()

