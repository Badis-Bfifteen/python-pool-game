from ball import Ball
from constants import HEIGHT, WIDTH
from utils import Vec2


def check_ball_collisions(*balls):


    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            b1, b2 = balls[i], balls[j]

            b1.check_collision(b2)




def check_table_collisions(*balls):

    for ball in balls:
        if ball.rect.x + ball.rect.width > WIDTH or ball.rect.x < 0:
            ball.velocity.x *= -1
                

        if ball.rect.y + ball.rect.height > HEIGHT or ball.rect.y < 0:
            ball.velocity.y *= -1
