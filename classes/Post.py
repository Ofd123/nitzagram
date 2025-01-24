import pygame

from constants import *
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


    def display(self):#############################################################################
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!

#----------------------------------------------------------------
    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """

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
#----------------------------------------------------------------
def add_like(self): #############################################################################
    """
    adds to the post 1 like
    :return: None
    :no inputs:
    """
    self.likes_counter += 1
#----------------------------------------------------------------
def add_comment(self, comment):
    """
    adds a comment to the post
    :param comment: comment to be added
    :return: None
    :no inputs:
    """
    self.comments.append(comment)
    self.comments_counter += 1
#----------------------------------------------------------------

#----------------------------------------------------------------
