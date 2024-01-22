# / # / # PROJECT OF DAY 20 # / # / #

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# x_cor = 0
# y_cor = 0
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []
game_is_on = True

for position in starting_positions:
    body = Turtle("square")
    body.color("white")
    body.penup()
    # x_cor -= 20
    # body.goto(x=x_cor, y=y_cor)
    body.goto(position)
    snake_body.append(body)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[num - 1].xcor()
        new_y = snake_body[num - 1].ycor()
        snake_body[num].goto(new_x, new_y)

    snake_body[0].forward(20)

screen.exitonclick()
