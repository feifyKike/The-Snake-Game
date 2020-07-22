import pygame
import pygame.font

class ButtonEasy():
    """Creating Mode buttons"""
    def __init__(self, ai_settings, screen, msg):
        """Initializing button attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Customizing dimensions + appearance
        self.width, self.height = 100, 50
        self.button_color = (230, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        # Determining the alignment values
        dis = self.ai_settings.screen_width - (self.width * 4)

        # Build the button's rects objects and center them
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = self.screen_rect.left + dis
        self.rect.centery = self.screen_rect.centery

        # Prepping the message on the buttons
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converting the text to an image in order to allign"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        # Centering the image
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Drawing the button on screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class ButtonHard():
    """Creating Mode buttons"""
    def __init__(self, ai_settings, screen, msg):
        """Initializing button attributes"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Customizing dimensions + appearance
        self.width, self.height = 100, 50
        self.button_color = (230, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        # Determining the alignment values
        dis = self.ai_settings.screen_width - (self.width * 4)

        # Build the button's rects objects and center them
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right - dis
        self.rect.centery = self.screen_rect.centery

        # Prepping the message on the buttons
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converting the text to an image in order to allign"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        # Centering the image
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Drawing the button on screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
