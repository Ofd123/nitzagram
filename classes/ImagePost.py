import Pygame
from Post import *

from constants import *
from helpers import screen


class ImagePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)
        self.image = Pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)