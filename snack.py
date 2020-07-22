import pygame
import random

class Snack():
    """Creating a food for the snake"""
    w = 500
    rows = 20
    def __init__(self, ai_settings, screen, snake):
        positions = snake.body
        self.ai_settings = ai_settings
        self.screen = screen

        while True:
            x = random.randrange(self.rows)
            y = random.randrange(self.rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                continue
            else:
                self.pos = (x, y)
                self.create_snack(self.pos)
                break


    def create_snack(self, pos):
        """Drawing the snack if the random spawn is created"""
        self.dis = self.w // self.rows
        self.i = self.pos[0]
        self.j = self.pos[1]

        self.image = pygame.image.load('apple_image.bmp')
        self.small_image = pygame.transform.scale(self.image, (self.dis-2,
                                                               self.dis-2))
        
    def blitme(self):
        """Updating the image on screen"""
        self.screen.blit(self.small_image, (self.i*self.dis+1, self.j*self.dis+1))
