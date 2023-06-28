import pygame

FPS_LIMIT = 60
MENU_SELECTION = 0
HOST = 1
JOIN = 2 
RETURN = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

state_selection = MENU_SELECTION 
menu_pervious_selection = 0
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# (width, height, screen)
def play_online_game():
    # [ingame:false, game_started: false, waiting: true, score]
    global state_selection
    game_state = [False, False]
    clock = pygame.time.Clock()  
    clock.tick(FPS_LIMIT)
    while True:
        print(state_selection, menu_pervious_selection)
        if state_selection == MENU_SELECTION:
            menu_options = ["Play as Host", "Join a Game", "Exit"]
            handle_menu_selection(menu_options)
            main_menu_render(menu_options)
            if state_selection == RETURN:
                state_selection = 0
                break
        if state_selection == HOST:
            
        pygame.display.flip()
        


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

def render_selection():
    print("Not yet develope")
    
    # clock = pygame.time.Clock()
    # while game_state[0]:
    #     cons_time = clock.tick(FPS_LIMIT)
    #     for event in pygame.event.get():   
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 exit()
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     game_state[1] = True
    #                     game_state[2] = False