import pygame
import pygame.font

class Instruction():
    """Showing instructions on pressing a button"""
    def __init__(self, ai_settings, screen, message):
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.msg_image = self.font.render(message, True, self.text_color)
        
        # Centering the image
        self.msg_image_rect = self.msg_image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.msg_image_rect.centerx = self.screen_rect.centerx
        self.msg_image_rect.centery = self.screen_rect.centery - 50
        
    def draw(self):
        """Draw the text on screen"""
        self.screen.blit(self.msg_image, self.msg_image_rect)
