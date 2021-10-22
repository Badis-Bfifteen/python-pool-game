#!/usr/bin/env python3

import pygame
from collisions import check_ball_collisions, check_table_collisions

from constants import WIDTH, HEIGHT
from ball import Ball
from hole import Hole
from image_loader import TABLE_IMAGE
from table import Table
from utils import Vec2

FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GRASS = (76, 175, 79)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pool")
clock = pygame.time.Clock()     ## For syncing the FPS

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

ball = Ball()
hole = Ball()
table = Table()
hole.set_position(40, 50)

all_sprites.add(table)
all_sprites.add(ball)
all_sprites.add(hole)

ball.set_position(WIDTH // 2, HEIGHT // 2)


## Game loop
running = True
while running:

    #1 Process input/events
    delta_time = clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ball.trigger_mouse(Vec2.to_vec2(event.pos))
            

    
    #2 Update
    all_sprites.update()

    #3 Draw/render
    screen.fill(GRASS)



    ############################
    check_ball_collisions(ball, hole)
    check_table_collisions(ball, hole)
    ############################

    all_sprites.draw(screen)

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()