import pygame
from image_loader import TABLE_IMAGE
from constants import WIDTH, HEIGHT

class Table(pygame.sprite.Sprite):



    def __init__(self) -> None:
        super().__init__()


        self.image = pygame.transform.scale(TABLE_IMAGE, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()