# Imports and screen setup
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Welcome to Pong Game")
# Turn OFF paddle positioning animation 
screen.tracer(0)


# Init objects:
r_paddle = Paddle((350, 200))
l_paddle = Paddle((-350, -200))
ball = Ball()



# paddles movement
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()



screen.exitonclick()