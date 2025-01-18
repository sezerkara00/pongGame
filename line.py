from turtle import Turtle

class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()
    
    def draw_line(self):
        self.pensize(5)
        for _ in range(30):  # Kesikli çizgi için
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20) 