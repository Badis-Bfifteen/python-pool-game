import pygame

from math import atan, pi
from pygame.constants import SRCALPHA

from ball import Ball
from constants import CUE_HEIGHT, CUE_WIDTH, DELTA_TIME, HEIGHT, MAX_FORCE, MIN_FORCE, POWER_MULTIPLIER, WIDTH

from image_loader import CUE_IMAGE
from utils import Vec2

class Cue(pygame.sprite.Sprite):


    def __init__(self, ball: Ball) -> None:
        super().__init__()

        self.org_image = pygame.transform.scale(CUE_IMAGE, (CUE_WIDTH, CUE_HEIGHT))
        self.org_image = pygame.transform.rotate(self.org_image, 180)

        self.image = self.org_image.copy()

        self.rect = self.image.get_rect()

        self.ball = ball


        self.force_vector = Vec2(0, 0)


        self.mouse_down = False
        self.mouse_start_pos = Vec2(0, 0)

        self.power = 0

    def start_mouse_hold(self):
        self.mouse_down = True

    def stop_mouse_hold(self):
        self.mouse_down = False

        #power = self.force_vector.magnitude()
        normal = self.force_vector.normalized()

        self.ball.add_force(Vec2.mul(normal, self.power))

        self.force_vector.set(0, 0)
        self.power = 0



    def trigger_mouse(self, position: Vec2):
        if not self.mouse_down:
            self.mouse_down = True
            self.mouse_start_pos = position
        
        else:
            self.mouse_down = False

            power = self.force_vector.magnitude()
            normal = self.force_vector.normalized()
            
            power = power * (MAX_FORCE - MIN_FORCE) / 600 + MIN_FORCE

            self.ball.add_force(Vec2.mul(normal, power))

            self.force_vector.set(0, 0)

    def update(self):
        mouse_pos = Vec2.to_vec2(pygame.mouse.get_pos())
        
        dir_vec = mouse_pos - self.ball.get_center_position()

        if dir_vec.x == 0:
            angle = 90
        else:
            angle = atan(dir_vec.y / dir_vec.x) * 180 / pi

        if dir_vec.x > 0: angle += 180
        self.rotate(-angle)

        if self.mouse_down:
            self.power += DELTA_TIME * POWER_MULTIPLIER
            self.power = MIN_FORCE + min(self.power, MAX_FORCE - MIN_FORCE)

            self.force_vector = dir_vec

        n_dir = dir_vec.normalized()
        n_dir.n_mul(CUE_WIDTH // 2 + self.ball.get_radius() + self.power * DELTA_TIME * 2)

        self.rect.x -= n_dir.x
        self.rect.y -= n_dir.y



    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.org_image, angle)
        self.rect = self.image.get_rect()

        center = self.ball.get_center_position()


        self.rect.center = center.values()
        


