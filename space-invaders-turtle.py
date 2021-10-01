from turtle import Screen, Turtle
import time
import random


width = 800
height = 800

screen = Screen()
screen.bgcolor("black")
screen.setup(width=width, height=height)
screen.tracer(0)

screen.listen()

projectile = Turtle()
projectile.penup()
projectile.color('red')
projectile.shape('square')
projectile.shapesize(0.2, 0.5)
projectile.hideturtle()
projectile.setheading(90)

enemy_projectile = Turtle()
enemy_projectile.penup()
enemy_projectile.color('green')
enemy_projectile.shape('square')
enemy_projectile.shapesize(0.2, 0.5)
enemy_projectile.hideturtle()
enemy_projectile.setheading(270)

player_shooting = False
invader_shooting = False


class Player(Turtle):

    def __init__(self, st_x, st_y):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.setpos(x=st_x, y=st_y)

    def move_right(self):
        self.setx(self.xcor() + 10)

    def move_left(self):
        self.setx(self.xcor() - 10)


# destroyable paddles
def summon_invaders():
    for row in range(60, 380, 100):
        for column in range(-300, 360, 100):
            invader = Turtle()
            invader.penup()
            invader.setheading(270)
            invader.shape("turtle")
            invader.color("yellow")
            invader.shapesize(stretch_wid=3, stretch_len=2)
            invader.setpos(x=column, y=row)
            invaders_list.append(invader)


def player_shoot():
    global player_shooting
    if not player_shooting:
        player_shooting = True
        x = player.xcor()
        y = player.ycor()
        projectile.setposition(x, y+30)
        projectile.showturtle()
    if projectile.ycor() >= 390:
        projectile.clear()
        player_shooting = False


def invader_shoot(x, y):
    global invader_shooting
    if not invader_shooting:
        invader_shooting = True
        enemy_projectile.setposition(x, y-30)
        enemy_projectile.showturtle()
    if enemy_projectile.ycor() <= -390:
        enemy_projectile.clear()
        invader_shooting = False


player = Player(0, -350)

screen.onkeypress(key="Right", fun=player.move_right)
screen.onkeypress(key="Left", fun=player.move_left)
screen.onkeypress(key="Up", fun=player_shoot)

invaders_list = []


summon_invaders()

game_on = True
z = 0.1
move = 5
new_line = -20
while game_on:
    time.sleep(z)
    screen.update()
    if player_shooting:
        projectile.forward(20)
    if invader_shooting:
        enemy_projectile.forward(20)

    for invader in invaders_list:
        attack = random.randint(0, 1)
        if attack == 1:
            invader_shoot(invader.xcor(), invader.ycor())
        invader.setx(invader.xcor() + move)
        if invader.xcor() >= 355:
            move = -5
        if invader.xcor() <= -355:
            move = 5
        if projectile.distance(invader) < 30:
            invader.hideturtle()
            invader.clear()
            projectile.hideturtle()
            invaders_list.remove(invader)
            player_shooting = False
        if invader.xcor() >= 400 or invader.xcor() <= -400:
            invader.setpos(random.randint(-350, 350), new_line)
            new_line -= 20

    if enemy_projectile.distance(player) < 30:
        game_on = False


screen.exitonclick()
