from typing import List
from ball import Ball
from constants import HEIGHT, HOLE_RADIUS, WIDTH, TABLE_OFFSET
from utils import Vec2


def check_ball_collisions(balls):


    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            b1, b2 = balls[i], balls[j]

            b1.check_collision(b2)




def check_table_collisions(balls):

    for ball in balls:
        next_x = ball.rect.x + ball.velocity.x
        next_y = ball.rect.y + ball.velocity.y

        if next_x + ball.rect.width > WIDTH - TABLE_OFFSET:
            ball.velocity.x *= -1
            ball.set_position(WIDTH - TABLE_OFFSET - ball.rect.width, ball.rect.y)

        if next_x < TABLE_OFFSET:
            ball.velocity.x *= -1
            ball.set_position(TABLE_OFFSET, ball.rect.y)
                

        if next_y + ball.rect.height > HEIGHT - TABLE_OFFSET:
            ball.velocity.y *= -1
            ball.set_position(ball.rect.x, HEIGHT - TABLE_OFFSET - ball.rect.height)

        if next_y < TABLE_OFFSET:
            ball.velocity.y *= -1
            ball.set_position(ball.rect.x, TABLE_OFFSET)

holes = [
    Vec2(TABLE_OFFSET + 10, TABLE_OFFSET + 10),
    Vec2(TABLE_OFFSET + 10, HEIGHT - TABLE_OFFSET - 10),
    Vec2(WIDTH - TABLE_OFFSET - 10, TABLE_OFFSET + 10),
    Vec2(WIDTH - TABLE_OFFSET - 10, HEIGHT - TABLE_OFFSET - 10),
    Vec2(WIDTH // 2, TABLE_OFFSET - 10),
    Vec2(WIDTH // 2, HEIGHT - TABLE_OFFSET + 10),
]

def check_holes_collision(balls: List[Ball]):
    for ball in balls:
        b_pos = ball.get_center_position()

        for hole in holes:
            if (b_pos - hole).sqrmagnitude() < HOLE_RADIUS ** 2:
                ball.pot()

