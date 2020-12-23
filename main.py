# Structure breakdown

# Components(classes) needed:

# - Imports and screen setup
# - Player class
# - Computer class (similar to player but randomly moved or make follow the ball)
# - Ball and ball collision
# - Score
# - Middle line
# - While loop that makes game be True/on until a cetain score is reached

# Course breakdown

# - Screen setup (same)
# - Create and move paddle(same but I represented it as player)
# - Create another paddle(same, I represented it as computer class)
# - Create ball and make it move(same)
# - Detect collision with wall and bounce(not mentioned in mine)
# - Detect collision with paddle(same)
# - Detect when paddle misses(not addressed)
# - Keep score(same)

# Imports and screen setup
from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Welcome to Pong Game")
# Turn off paddle animation positioning
screen.tracer(0)


# Init objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# Turn on paddle animation positioning
screen.tracer(1)


# paddle movement
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



screen.exitonclick()