from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_move, y_move):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = x_move
        self.y_move = y_move

    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)



    def bounce(self):
        self.y_move *= - 1.1
    

    def bounce_x(self):
        self.x_move *= - 1.1