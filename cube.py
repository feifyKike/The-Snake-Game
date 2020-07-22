import pygame

class Cube():
    """Creating individual snake objects"""
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(0,0,255)):
        self.pos = start
        self.dirnx = 1
        self.dirny =0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

    def draw(self, screen):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(screen, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
