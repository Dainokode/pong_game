# Imports and screen setup
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Welcome to Pong Game")
# Turn OFF paddle positioning animation 
screen.tracer(0)


# Init objects:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()



# paddles movement
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    # detect wall collision
    if ball.ycor() == 295 or ball.ycor() == -295:
        ball.bounce()



screen.exitonclick()