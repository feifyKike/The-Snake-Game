import pygame
import sys
from snack import Snack
from cube import Cube
import math
import random
from tkinter import*
import time
from obstacle import Obstacle
from mode_buttons import ButtonEasy, ButtonHard
from mode_instruction import Instruction

def check_events(snake, screen, ai_settings, snack, obst_group,
                        easy_button, hard_button):
    """Responding to user input"""
    rows = 20
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(snake, screen, ai_settings, snack, obst_group,
                        easy_button, hard_button, mouse_x, mouse_y)
            
        # If game active you can manipulate the snake
        if ai_settings.status:
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    snake.dirnx = -1
                    snake.dirny = 0
                    snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]

                elif keys[pygame.K_RIGHT]:
                    snake.dirnx = 1
                    snake.dirny = 0
                    snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]
        
                elif keys[pygame.K_UP]:
                    snake.dirnx = 0
                    snake.dirny = -1
                    snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]

                elif keys[pygame.K_DOWN]:
                    snake.dirnx = 0
                    snake.dirny = 1
                    snake.turns[snake.head.pos[:]] = [snake.dirnx, snake.dirny]
                    
    for i, c in enumerate(snake.body):
        p = c.pos[:]
        if p in snake.turns:
            turn = snake.turns[p]
            c.move(turn[0], turn[1])
            if i == len(snake.body)-1:
                snake.turns.pop(p)

        else:
            if c.dirnx == -1 and c.pos[0] <= 0:
                c.pos = (c.rows-1, c.pos[1])

            elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                c.pos = (0, c.pos[1])

            elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                c.pos = (c.pos[0], 0)

            elif c.dirny == -1 and c.pos[1] <= 0:
                c.pos = (c.pos[0], c.rows-1)

            else:
                c.move(c.dirnx, c.dirny)

def check_buttons(snake, screen, ai_settings, snack, obst_group,
                        easy_button, hard_button, mouse_x, mouse_y):
    """Checking which button the user pressed"""
    button_easy_clicked = easy_button.rect.collidepoint(mouse_x, mouse_y)
    button_hard_clicked = hard_button.rect.collidepoint(mouse_x, mouse_y)
    if button_hard_clicked and not ai_settings.status:
        ai_settings.status = True
        ai_settings.show_obst = True
        ai_settings.fps = 10
        ai_settings.delay = 30
        create_groupof_obstacles(snake, screen, ai_settings, snack, obst_group)
        
    elif button_easy_clicked and not ai_settings.status:
        ai_settings.status = True
        create_groupof_obstacles(snake, screen, ai_settings, snack, obst_group)

def update_screen(ai_settings, screen, snake, snack, obst_group,
                  easy_button, hard_button, instruc):
    """Updating the screen to see all the services"""
    # Update the background of the screen
    screen.fill(ai_settings.bg_color)

    # Drawing the Grid
    grid(ai_settings, screen)
    
    # Draw the snake
    snake.draw()

    # Draw the snack
    snack.blitme()

    # Draw the obstacles
    for obstacle in obst_group.sprites():
        obstacle.blitme()

    # Draw the mode buttons
    if not ai_settings.status:
        easy_button.draw_button()
        hard_button.draw_button()
        instruc.draw()
        
    # Make the most recently drawn screen visible
    pygame.display.flip()

def grid(ai_settings, screen):
    """Figuring out how many lines and columns are needed"""
    rows = 20
    w = ai_settings.screen_width
    sizeBtw = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtw
        y = y + sizeBtw

        # Display the grid lines
        pygame.draw.line(screen, (0,0,0), (x,0), (x,w))
        pygame.draw.line(screen, (0,0,0), (0,y), (w,y))
        
def create_obstacle(snake, screen, ai_settings, snack, obst_group):
    """Creating a single bomb"""
    bomb = Obstacle(snake, screen, ai_settings, snack)
    obst_group.add(bomb)

def create_groupof_obstacles(snake, screen, ai_settings, snack, obst_group):
    """Creating multiple bombs"""
    if ai_settings.show_obst:
        counter = 5
        for x in range(counter):
            create_obstacle(snake, screen, ai_settings, snack, obst_group)

def check_snack_snake_collisions(ai_settings, screen, snake, snack):
    """Check for collisions between the snack and the snake"""
    if snake.body[0].pos == snack.pos:
        snake.addTail()
        snack = Snack(ai_settings, screen, snake)

def removeTail(snake, screen, ai_settings, snack, obst_group):
    """Removing the last cube"""
    if snake.body[-1] != snake.body[0]:
        snake.body.remove(snake.body[-1])
    else:
        game_over(snake)
        reset((10,10), snake, screen, ai_settings, snack, obst_group)

def reset(pos, snake, screen, ai_settings, snack, obst_group):
    """Resetings the settings when told to do so"""
    snake.head = Cube(pos)
    snake.body = []
    snake.body.append(snake.head)
    snake.turns = {}
    snake.dirnx = 1
    snake.dirny = 0

    # Removing the old obstacles and adding new ones
    obst_group.empty()
    create_groupof_obstacles(snake, screen, ai_settings, snack, obst_group)
    
def game_over(snake):
    """Display this message if certain gameover criteria are met"""
    print("Game Over!")
    game_message = "Your final Score:" + str(len(snake.body))
    print(game_message + "\n--------------------")
    time.sleep(3)
    
    
def check_snake_collisions(snake, screen, ai_settings, snack, obst_group):
    """Checking for personal collisions"""
    for x in range(len(snake.body)):
        if snake.body[x].pos in list(map(lambda z:z.pos,snake.body[x+1:])):
            game_over(snake)
            reset((10,10), snake, screen, ai_settings, snack, obst_group)
            break

        

        
        
        

    




    

