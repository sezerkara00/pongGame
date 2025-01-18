from turtle import Screen
from paddle import Paddle
from ball import Ball
from line import CenterLine
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Oyuncuları oluştur
r_paddle = Paddle((350, 0))  # Sağ oyuncu
l_paddle = Paddle((-350, 0))  # Sol oyuncu

# Tuş kontrolleri
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Top oluştur
top = Ball()

# Orta çizgiyi oluştur
center_line = CenterLine()

# Skor tahtasını oluştur
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    top.move()
    
    # Üst ve alt duvara çarpma kontrolü
    if top.ycor() > 280 or top.ycor() < -280:
        top.bounce_y()
    
    # Raketlere çarpma kontrolü
    if (top.distance(r_paddle) < 50 and top.xcor() > 320 and top.x_move > 0) or \
       (top.distance(l_paddle) < 50 and top.xcor() < -320 and top.x_move < 0):
        top.bounce_x()
    
    # Top kaçırıldı mı kontrolü
    if top.xcor() > 380:  # Sağ oyuncu kaçırdı
        top.reset_position()
        if scoreboard.l_point():  # Sol oyuncu puan aldı ve 10'a ulaştı mı?
            scoreboard.game_over("SOL OYUNCU")
            game_is_on = False
    
    if top.xcor() < -380:  # Sol oyuncu kaçırdı
        top.reset_position()
        if scoreboard.r_point():  # Sağ oyuncu puan aldı ve 10'a ulaştı mı?
            scoreboard.game_over("SAĞ OYUNCU")
            game_is_on = False

screen.exitonclick()  # Oyun bittiğinde tıklayana kadar ekranı tut
