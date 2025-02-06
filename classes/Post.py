import pygame
from constants import *
from Comment import *
from helpers import screen


class Post:
    username = ""           #the poster's name
    location = ""           #the pinged location
    description = ""        #the post's description
    likes_counter = 0       #the counter of likes
    comments_counter = 0    #the counter of comments (for urself)
    comments = []           #the comments for the post
    showAll = False         #if the user is intrested in watching all comments
#----------------------------------------------------------------
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description):
        self.username = str(username)
        self.location = str(location)
        self.description = str(description)
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0
# ----------------------------------------------------------------
    def display(self):
        font = pygame.font.SysFont("chalkduster.ttf", UI_FONT_SIZE)
        # -------------------------------------------------------------------
        user_name = font.render(self.username, True, BLACK)
        screen.blit(user_name, (USER_NAME_X_POS, USER_NAME_Y_POS))
        # -------------------------------------------------------------------
        loc = font.render(self.location, True, BLACK)
        screen.blit(loc, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        # -------------------------------------------------------------------
        like_counter = font.render(str(self.likes_counter), True, BLACK)
        screen.blit(like_counter, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        # -------------------------------------------------------------------
        description = font.render(self.description, True, LIGHT_GRAY)
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        # -------------------------------------------------------------------
        self.display_comments()
#----------------------------------------------------------------
    def display_comments(self):
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,VIEW_MORE_COMMENTS_Y_POS))
    # -------------------------------------------------------------------------------------------------

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            # --------------------------------
            self.comments[position_index].display(i)
            position_index += 1
            # --------------------------------
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        if self.likes_counter == 1:
            self.likes_counter -= 1
        else:
            self.likes_counter += 1
#----------------------------------------------------------------
    def add_comment(self, comment):
        """
        adds a comment to the post
        :param self:
        :param comment: comment to be added
        :return: None
        :no inputs:
        """
        comment = Comment(comment)
        comment.transfer_to_arr()  # Optional: if you need text array processing
        self.comments.append(comment)
        self.comments_counter += 1
#----------------------------------------------------------------
    def show_more_comments(self):
        self.comments_display_index +=1
        if self.comments_display_index >= len(self.comments):
            self.comments_display_index = 0
#----------------------------------------------------------------
