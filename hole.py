import pygame

from image_loader import HOLE_IMAGE

class Hole(pygame.sprite.Sprite):


    def __init__(self) -> None:
        super().__init__()

        self.image = HOLE_IMAGE
        self.rect = self.image.get_rect()




