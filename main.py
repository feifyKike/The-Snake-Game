import pygame
import sys
from settings import Settings
from snake import Snake
import game_func as gf
from snack import Snack
from obstacle import Obstacle
from pygame.sprite import Group
from mode_buttons import ButtonEasy, ButtonHard
from mode_instruction import Instruction

def play_game():
    """Initializing and executing the game"""
    pygame.init()

    # Allowing access to the settings module
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Snake Game")

    # The mode buttons
    easy_button = ButtonEasy(ai_settings, screen, "Easy")
    hard_button = ButtonHard(ai_settings, screen, "Hard")
    # Showing instruction message
    message = "Choose a mode to play in:"
    instruc = Instruction(ai_settings, screen, message)
    
    # Creating the snake
    snake = Snake(ai_settings, screen, (0,0,255), (10,10))

    # Creating the snack
    snack = Snack(ai_settings, screen, snake)

    # Creating a group holder for obstacles, and multiple obstacles
    obst_group = Group()
    gf.create_groupof_obstacles(snake, screen, ai_settings, snack, obst_group)

    # Controlling the FPS of the game
    clock = pygame.time.Clock()
    # Starting the main game loop
    while True:
        # Controlling the FPS and key compute speed
        pygame.time.delay(ai_settings.delay)
        clock.tick(ai_settings.fps)
        gf.check_events(snake, screen, ai_settings, snack, obst_group,
                        easy_button, hard_button)
        
        if ai_settings.status:
            # Checking snake and snack collisions
            if snake.body[0].pos == snack.pos:
                snake.addTail()
                snack = Snack(ai_settings, screen, snake)
            # Check for snake and obstacle collisions
            for single in obst_group.copy():
                if snake.body[0].pos == single.pos:
                    obst_group.remove(single)
                    gf.removeTail(snake, screen, ai_settings, snack, obst_group)
                    break
                
            # Checking for personal collisions
            gf.check_snake_collisions(snake, screen, ai_settings, snack,
                                      obst_group)
        gf.update_screen(ai_settings, screen, snake, snack, obst_group,
                         easy_button, hard_button, instruc)
        
play_game()
