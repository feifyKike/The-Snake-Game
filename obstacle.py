import pygame
import random
from pygame.sprite import Sprite

class Obstacle(Sprite):
    """Creating a snake obstacle: bomb in this case"""
    w = 500
    rows = 20
    def __init__(self, snake, screen, ai_settings, snack):
        """Initializing obstacle attributes"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.snake = snake
        self.positions = self.snake.body
        self.positions_snack = snack.pos

        while True:
            x = random.randrange(self.rows)
            y = random.randrange(self.rows)
            
            # X spawn on top of the snake
            if len(list(filter(lambda z:z.pos == (x,y), self.positions))) > 0:
                continue
            # X collision with snake at spawn
            elif y == 10:
                continue
            elif (x, y) == snack.pos:
                continue
            
            else:
                self.pos = (x, y)
                self.create_obstacle(self.pos)
                break
            
    def create_obstacle(self, pos):
        """Outlining the object and its parameters"""
        self.dis = self.w // self.rows
        self.i = self.pos[0]
        self.j = self.pos[1]

        self.image = pygame.image.load('bomb.bmp')
        self.small_image = pygame.transform.scale(self.image, (self.dis-2,
                                                               self.dis-2))

    def blitme(self):
        """Translate the image to the screen"""
        self.screen.blit(self.small_image, (self.i*self.dis+1,
                                            self.j*self.dis+1))
