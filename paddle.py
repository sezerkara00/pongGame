from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # 20x100 pixel (5x20 ve 1x20)
        self.penup()
        self.goto(position)  # x=350 sağ oyuncu, x=-350 sol oyuncu için

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:  # Ekran sınırlarını kontrol et
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:  # Ekran sınırlarını kontrol et
            self.goto(self.xcor(), new_y) 