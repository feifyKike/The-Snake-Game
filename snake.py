import pygame
from cube import Cube
from game_func import reset, game_over

class Snake():
    """Creating the snake"""
    # Keeping track of where we turn 
    body = []
    turns = {}
    def __init__(self, ai_settings, screen, color, pos):
        """Initializing the snake attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.color = color
        self.pos = pos
        self.head = Cube(self.pos)
        self.body.append(self.head)

        # The snake direction keys
        self.dirnx = 0
        self.dirny = 1

    def addTail(self):
        """Adding to the snakes tail"""
        self.tail = self.body[-1]
        dx, dy = self.tail.dirnx, self.tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((self.tail.pos[0]-1, self.tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((self.tail.pos[0]+1, self.tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((self.tail.pos[0], self.tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((self.tail.pos[0], self.tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

            
    def draw(self):
        """Drawing the snake by its separate pieces"""
        for i, c in enumerate(self.body):
            if i >= 0:
                c.draw(self.screen)
                
        
