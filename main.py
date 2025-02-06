# from random import random, randint
import pygame
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from helpers import screen, mouse_in_button, read_comment_from_user
from buttons import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
#---------------------------------------------------------------------------
#like
# like_screen = pygame.display.set_mode(like_button.x_pos,like_button.y_pos)
like = pygame.image.load("Images/like.png")
like_img = pygame.transform.scale(like, (LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT))
# like_pos = (randint(0, int(WINDOW_WIDTH - LIKE_BUTTON_WIDTH)), randint(0, int(WINDOW_HEIGHT - LIKE_BUTTON_HEIGHT)))
# like_screen.blit(like,(like_button.width,like_button.height))
#---------------------------------------------------------------------------

imgpst = ImagePost("firstUser","Tel Aviv","loves nitzagram","no path")
img1 = ImagePost("head","haifa","hello","Images/noa_kirel.jpg")
txtpst = TextPost("secUser","Eilat","better than first user","bla bla bla")
# ------------------

image_posts = [imgpst]
text_posts = []
posts = [img1,imgpst]
#--------------------------------------------------------------------------------
def main():
    likes_limit = False
    current_img = 0
    # --------------------
    pygame.init() # Set up the game display, clock and headline
    pygame.display.set_caption('Nitzagram') # Change the title of the window
    clock = pygame.time.Clock()
    # ---------------------------------------------------------------------------
    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))
    # ---------------------------------------------------------------------------
    image_posts[current_img].display()
    # ---------------------------------------------------------------------------
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # -------------------------------------------
                    if mouse_in_button(like_button,pos):
                        posts[current_img].add_like()
                    #-------------------------------------------
                    elif(mouse_in_button(comment_button,pos)):
                        comment = read_comment_from_user()
                        posts[current_img].add_comment(comment)
                    # -------------------------------------------
                    elif(mouse_in_button(click_post_button,pos)):
                        current_img += 1
                        if current_img >= len(posts):
                            current_img = 0
                        posts[current_img].display()
                    # -------------------------------------------
                    elif(mouse_in_button(view_more_comments_button,pos)):
                        posts[current_img].show_more_comments()
        # ------------------------------------------------------------------------
        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        # Update display - without input update everything
        pygame.display.update()
        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
        # -----------------------------------------------------------------------
    pygame.quit()
    quit()
#--------------------------------------------------------------------------------

main()
