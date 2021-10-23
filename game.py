import pygame
from pygame.constants import SCRAP_SELECTION

from collisions import *

from ball import Ball
from cue import Cue
from table import Table

from constants import HEIGHT, WIDTH, FPS

class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pool")

        self.clock = pygame.time.Clock()

        self.table = Table()


        self.player_ball = Ball()
        self.ball0 = Ball()
        self.ball1 = Ball()
        self.ball2 = Ball()


        self.ball0.set_position(50, 50)
        self.ball1.set_position(60, 60)
        self.ball2.set_position(100, 100)
        self.balls = [
            self.player_ball,
            self.ball0,
            self.ball1,
            self.ball2
        ]

        self.cue = Cue(self.player_ball)


        self.sprites = pygame.sprite.Group()
        
        self.sprites.add(self.table)
        self.sprites.add(self.player_ball)
        self.sprites.add(self.ball0)
        self.sprites.add(self.ball1)
        self.sprites.add(self.ball2)


        self.player_ball.set_position(WIDTH // 4, HEIGHT // 2)


        self.running = False


    def run(self):
        running = True

        while running:
            delta_time = self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #self.cue.trigger_mouse(Vec2.to_vec2(event.pos))
                    self.cue.start_mouse_hold()

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.cue.stop_mouse_hold()


            self.sprites.update()


            ##############
            check_ball_collisions(self.balls)
            check_table_collisions(self.balls)
            ##############


            self.sprites.draw(self.screen)

            if not any(map(lambda x:x.moving, self.balls)):
                self.cue.update()
                self.screen.blit(self.cue.image, self.cue.rect)


            pygame.display.flip()
    
        pygame.quit()