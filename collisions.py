from constants import HEIGHT, WIDTH


def check_ball_collisions(balls):


    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            b1, b2 = balls[i], balls[j]

            b1.check_collision(b2)




def check_table_collisions(balls):

    for ball in balls:
        next_x = ball.rect.x + ball.velocity.x
        next_y = ball.rect.y + ball.velocity.y

        if next_x + ball.rect.width > WIDTH - 45:
            ball.velocity.x *= -1
            ball.set_position(WIDTH - 45 - ball.rect.width, ball.rect.y)

        if next_x < 45:
            ball.velocity.x *= -1
            ball.set_position(45, ball.rect.y)
                

        if next_y + ball.rect.height > HEIGHT - 45:
            ball.velocity.y *= -1
            ball.set_position(ball.rect.x, HEIGHT - 45 - ball.rect.height)

        if next_y < 45:
            ball.velocity.y *= -1
            ball.set_position(ball.rect.x, 45)

