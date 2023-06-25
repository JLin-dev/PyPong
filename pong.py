import random
import pygame
from objects import Ball
from objects import Paddle
from objects import Wall
# maybe use use individual import so i get to know the origin of a object
# from pygame.locals import *


# pygame set up
pygame.init()
width, height = 640, 480
FPS_LIMIT = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BACKGROUND_COLOR = BLACK
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")


# object attrb and init
paddle_width = 15
paddle_height = 60
paddle_speed = 10
init_paddle_y = height // 2
PADDLE_COLOR = RED

ball_speed = 7
ball_radius = 10
init_ball_x = width //  2  # Shifted to the left by half the ball radius
init_ball_y= height // 2  # Shifted upward by half the ball radius
init_ball_dx = random.choice([-ball_speed, ball_speed])  # Randomly select -1 or 1 for horizontal direction
init_ball_dy = 0  # Randomly select -1 or 1 for vertical direction
init_ball_dy = 0
BALL_COLOR = (255, 255, 255)

wall_height = 1


# object create
ball = Ball(init_ball_x, init_ball_y, ball_radius, init_ball_dx, init_ball_dy, BALL_COLOR)
left_paddle = Paddle(0, init_paddle_y - paddle_height/2 , paddle_width, paddle_height, paddle_speed, PADDLE_COLOR, height)
right_paddle = Paddle(width - paddle_width, init_paddle_y - paddle_height/2, paddle_width, paddle_height, paddle_speed, PADDLE_COLOR, height)
top_wall = Wall(0 , 0 - wall_height, width, wall_height, RED, height)
bot_wall = Wall(0 , height, width, wall_height, RED, height)

#ojbs list
objs_list = [left_paddle, right_paddle, top_wall, bot_wall]
menu_pervious_selection = 0

def main():
    # game event
    running = True
    clock = pygame.time.Clock()
    ball_out_of_bounds_time = 0
    Waiting = False
    respawn_time = 3000
    game_started = False
    score_board = [0,0]
    
    while running:
        cons_time = clock.tick(FPS_LIMIT)

        # Draw main menu
        main_menu()

        # # Fill screen with color
        # screen.fill(BACKGROUND_COLOR)
        # if not game_started:
        #     press_space_start(screen)

        # elif not Waiting:
        #     draw_score(screen, score_board)
        #     draw_and_update_pos(ball, left_paddle, right_paddle, top_wall, bot_wall, screen, cons_time)        
        #     check_ball_collides(ball, objs_list)
        #     if check_out_bound(ball, score_board):
        #         ball_out_of_bounds_time = pygame.time.get_ticks()
        #         ball.dx = 0
        #         ball.dy = 0
        #         Waiting = True
        # else:
        #     draw_score(screen, score_board)
        #     draw_and_update_pos(ball, left_paddle, right_paddle, top_wall, bot_wall, screen, cons_time)
        #     current_time = pygame.time.get_ticks()  # Get the current time
        #     elapsed_time = current_time - ball_out_of_bounds_time  # Calculate the elapsed time
            
        #     count_down_text(screen, respawn_time - elapsed_time)
        #     if elapsed_time >= respawn_time:
        #         ball.dx = random.choice([-ball_speed, ball_speed])
        #         ball.dy = 0
        #         ball.x = init_ball_x
        #         ball.y = init_ball_y
        #         Waiting = False
        
        # # Update screen
        # pygame.display.flip()

    pygame.quit()

# Two component selection handle and render
def main_menu():

    menu_options = ["Play Local", "Play Online", "Exit"]
    handle_menu_selection(menu_options)
    main_menu_render(menu_options)
    

def handle_menu_selection(menu_options):
    global menu_pervious_selection 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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
                    play_local_game()
                elif menu_pervious_selection == 1:
                    play_online_game()
                elif menu_pervious_selection == 2:
                    pygame.quit()



def main_menu_render(menu_options):
    screen.fill(BLACK)  # Clear the screen
    
    # Title 
    title_font = pygame.font.Font(None, 100)
    title_text = title_font.render("PyPong", True, (135, 206, 250))
    title_text_rect = title_text.get_rect(center=(width // 2, height// 3 - 50))
    screen.blit(title_text, title_text_rect)

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
    pygame.display.flip()  # Update the screen



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



    
    
    
    


def play_local_game():
    print("Not yet develope")


def play_online_game():
    print("Not yet develope")

if __name__ == "__main__":
    main()

