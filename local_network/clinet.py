import pygame
import socket
import 
from pygame.locals import *

FPS_LIMIT = 60
MENU_SELECTION = 0
HOST = 1
JOIN = 2 
RETURN = 3
WAITING_PLAYER = 4
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

state_selection = MENU_SELECTION 
menu_pervious_selection = 0
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
host_input = ""

# (width, height, screen)
def play_online_game():
    # [ingame:false, game_started: false, waiting: true, score]
    global state_selection
    game_state = [False, False]
    clock = pygame.time.Clock()  
    clock.tick(FPS_LIMIT)
    while True:
        if state_selection == MENU_SELECTION:
            menu_options = ["Play as Host", "Join a Game", "Exit"]
            handle_menu_selection(menu_options)
            main_menu_render(menu_options)
            if state_selection == RETURN:
                state_selection = MENU_SELECTION
                break
        elif state_selection == HOST:
            host_handle()
            host_render()
        elif state_selection == WAITING_PLAYER:
            waiting_player_handle()
            waiting_player_render()

        pygame.display.flip()
        

def host_render():
    # Clear the screen
    screen.fill(BLACK)  

    # Some init
    font = pygame.font.Font(None, 36)
    prompt = "Please enter 4 digit code"

    prompt = font.render(prompt, True, WHITE)
    promt_rect = prompt.get_rect(center=(width // 2, height // 2))

    # User input
    font = pygame.font.Font(None, 46)
    input_surface = font.render(host_input, True, BLACK)
    
    # Input 
    pygame.draw.rect(screen, WHITE, (width // 2 - 40, height // 2 + 30, 100, 40))  # Input box

    # Display area  (310, 260)
    screen.blit(input_surface, (width // 2 - 25 , height // 2 + 40))
    screen.blit(prompt, promt_rect)
    
def host_handle():
    global state_selection
    global host_input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                state_selection = MENU_SELECTION # Return None to go back to the previous menu
            elif event.key == K_RETURN:
                if valid_return(host_input):
                    state_selection = WAITING_PLAYER
            elif event.key == K_BACKSPACE:
                host_input = host_input[:-1]  # Remove the last character
            else:
                if event.unicode.isdigit():
                    if only_four_digit(host_input):
                        host_input += event.unicode  # Append the pressed key to the input text
   
# copy and paste not sure how to orgnized
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
                    state_selection = HOST
                elif menu_pervious_selection == 1:
                    state_selection = JOIN
                elif menu_pervious_selection == 2:
                    state_selection = RETURN

def title_render():
    title_font = pygame.font.Font(None, 100)
    title_text = title_font.render("PyPong", True, (135, 206, 250))
    title_text_rect = title_text.get_rect(center=(width // 2, height// 3 - 50))
    screen.blit(title_text, title_text_rect)

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

def only_four_digit(input):
    if len(input) < 4: return True
    return False

def valid_return(input):
    if len(input) == 4: return True
    return False



def waiting_player_render():
    # Clear the screen
    screen.fill(BLACK)  
    font = pygame.font.Font(None, 36)
    prompt = "Waiting for Player to Connect"
    prompt2 = "Press ESC to go back menu selection"
    prompt = font.render(prompt, True, WHITE)
    font = pygame.font.Font(None, 16)
    prompt2 = font.render(prompt2, True, WHITE)
    promt_rect = prompt.get_rect(center=(width // 2, height // 2))
    promt_rect2 = prompt.get_rect(center=(width // 2 + 80, height // 2 + 80))

    screen.blit(prompt, promt_rect)
    screen.blit(prompt2, promt_rect2)

def waiting_player_handle():
    global state_selection
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                state_selection = MENU_SELECTION # Return None to go back to the previous menu
    
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)

    