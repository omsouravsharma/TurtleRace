import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Who wil win')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
is_race_on = False
y_position = -100
all_turtle = []

for t_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position)
    new_turtle.color(colors[t_index])
    all_turtle.append(new_turtle )
    y_position +=30


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! Winnning Turtle is: {winning_color}")
            else:
                print(f"You Lost! Winnning Turtle is: {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()

