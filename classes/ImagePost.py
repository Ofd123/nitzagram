import pygame
from classes.Post import Post
from constants import *
from helpers import screen

class ImagePost(Post):
    image_path = "images/noUserPic.png"
    # image , rect , center
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)
        try:
            self.image_path = image_path
            self.temp_image = pygame.image.load(image_path)
        except FileNotFoundError:
            self.image_path = "images/noUserPic.png"
            # self.image = pygame.image.load("images/noUserPic.png")
        # --------------------------------
        # self.rect = self.image.get_rect()
        # self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    def display(self):
        try:
            image = pygame.image.load(self.image_path)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            image = pygame.image.load("images/noUserPic.png")

        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
        super().display()
        pygame.display.update()
