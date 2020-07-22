class Settings():
    """Creating defualt settings to be used throughout the project"""
    def __init__(self):
        """Intializing necessary settings"""
        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (0, 200, 0)

        # Snake settings
        self.snake_color = 0, 0, 255
        
        # Game status
        self.status = False

        # Showing obstacles flag
        self.show_obst = False

        # The game default game fps
        self.fps = 7

        # The game default input delay
        self.delay = 10
        
