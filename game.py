import pygame

from collisions import *

from ball import Ball
from cue import Cue
from image_loader import BALL_IMAGE, BALL_RED_IMAGE, BALL_YELLOW_IMAGE
from table import Table

from constants import HEIGHT, WIDTH, FPS, RED_BALL_PLACEMENT, YELLOW_BALL_PLACEMENT

class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()


        self.debut = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Pool")

        self.clock = pygame.time.Clock()

        self.table = Table()

        self.sprites = pygame.sprite.Group()

        self.player_ball = Ball(BALL_IMAGE)
        
        self.balls = [
            self.player_ball,
        ]

        
        self.sprites.add(self.table)
        self.sprites.add(self.player_ball)


        for b in RED_BALL_PLACEMENT:
            ball = Ball(BALL_RED_IMAGE)

            ball.set_position(b[0], b[1])

            self.balls.append(ball)
            self.sprites.add(ball)
            
        for b in YELLOW_BALL_PLACEMENT:
            ball = Ball(BALL_YELLOW_IMAGE)

            ball.set_position(b[0], b[1])

            self.balls.append(ball)
            self.sprites.add(ball)
            

        self.cue = Cue(self.player_ball)

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


            for ball in self.balls:
                if ball.potted:
                    if ball == self.player_ball:
                        ball.set_position(WIDTH // 4, HEIGHT // 2)
                        ball.potted = False
                        ball.velocity.set(0, 0)
                        continue
                    self.balls.remove(ball)
                    self.sprites.remove(ball)

            self.sprites.update()


            ##############
            check_ball_collisions(self.balls)
            check_table_collisions(self.balls)
            check_holes_collision(self.balls)
            ##############




            self.sprites.draw(self.screen)

            if not any(map(lambda x:x.moving, self.balls)):
                self.cue.update()
                self.screen.blit(self.cue.image, self.cue.rect)


            if self.debut:
                holes = [
                    Vec2(TABLE_OFFSET + 10, TABLE_OFFSET + 10),
                    Vec2(TABLE_OFFSET + 10, HEIGHT - TABLE_OFFSET - 10),
                    Vec2(WIDTH - TABLE_OFFSET - 10, TABLE_OFFSET + 10),
                    Vec2(WIDTH - TABLE_OFFSET - 10, HEIGHT - TABLE_OFFSET - 10),
                    Vec2(WIDTH // 2, TABLE_OFFSET - 10),
                    Vec2(WIDTH // 2, HEIGHT - TABLE_OFFSET + 10),
                ]
                for hole in holes:
                    pygame.draw.circle(self.screen, (0, 255, 0), hole.values(), 30)
            

            pygame.display.flip()

    
        pygame.quit()