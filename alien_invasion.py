# creating a pygame window and responding to user input
import sys
import pygame
# importing settings from setting.py
from settings import Settings
from ship import Ship

def run_game():
    '''initialize game and create a screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    '''setting the background color'''
    bg_color = (230,230,230)
    '''make a ship'''
    ship = Ship(screen)

    '''start the main loop for the game'''
    while true:
        '''watch for the keyboard and mouse'''
        '''redraw the screen'''
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        '''making the screen visible'''
        pygame.display.flip()
run_game()