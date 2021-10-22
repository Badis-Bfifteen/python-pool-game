from math import log
import pygame

from constants import DELTA_TIME, DRAG, MAX_FORCE, SPEED_THRESHOLD, WIDTH, HEIGHT
from image_loader import BALL_IMAGE
from utils import Vec2


class Ball(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()

        self.image = BALL_IMAGE
        self.rect = self.image.get_rect()

        self.velocity = Vec2(0, 0)

        self.moving = False

        self.mass = 1

    def add_force(self, force: Vec2 = Vec2(0, 0)):
        acceleration = Vec2.div(force, self.mass)
        acceleration.n_mul(DELTA_TIME)
        
        self.velocity += acceleration

    def update(self):
        self.velocity.n_mul(1 - DRAG)

        self.move(self.velocity)

        if self.velocity.sqrmagnitude() < SPEED_THRESHOLD: 
            self.velocity.set(0, 0)
            self.moving = False

        else:
            self.moving = True


    def move(self, vel: Vec2):
        self.rect.x += vel.x
        self.rect.y += vel.y

    def set_position(self,x: int, y: int):
        self.rect.x, self.rect.y = x, y

    def get_position(self):
        return Vec2(self.rect.x, self.rect.y)

    def get_center_position(self):
        return Vec2(self.rect.x + self.get_radius(), self.rect.y + self.get_radius())

    def get_radius(self):
        return self.rect.width / 2


    def check_collision(self, ball):
        n = self.get_position() - ball.get_position()


        req_dist = self.get_radius() + ball.get_radius()
        dist = n.magnitude()

        if dist > req_dist:
            return


        mtd = (req_dist - dist) // 2

        un = n.normalized()

        self.move(Vec2.mul(un, mtd))
        ball.move(Vec2.mul(un, -mtd))
        

        # tangent vector
        ut = Vec2(-un.y, un.x)

        v1n = un.dot(self.velocity)
        v1t = ut.dot(self.velocity)

        v2n = un.dot(ball.velocity)
        v2t = ut.dot(ball.velocity)

        v1nTag = Vec2.mul(un, v2n)
        v1tTag = Vec2.mul(ut, v1t)

        v2nTag = Vec2.mul(un, v1n)
        v2tTag = Vec2.mul(ut, v2t)

        self.velocity = v1nTag + v1tTag
        ball.velocity = v2nTag + v2tTag
