from constants import *
import pygame
import main_entity

class Enemy(main_entity.Main_entity):

    """
        # TODO:

    """
    def __init__(self, x, y):


        super().__init__(x, y)
        self.color = (255, 0, 0)
        self.image.fill(self.color)

    def update(self):
        pass
