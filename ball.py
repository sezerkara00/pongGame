from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_multiplier = 0.3  # Hız çarpanı ekledik
        self.reset_ball()
    
    def move(self):
        new_x = self.xcor() + (self.x_move * self.speed_multiplier)
        new_y = self.ycor() + (self.y_move * self.speed_multiplier)
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        # Hız çarpanını artır (maksimum 2.0 olacak şekilde)
        self.speed_multiplier = min(self.speed_multiplier + 0.1, 2.0)
    
    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 0.2
        self.y_move = 0.2
        self.speed_multiplier = 0.3  # Hızı başlangıç değerine döndür
        self.bounce_x()
    
    def reset_position(self):
        self.reset_ball() 