from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

# Higher order function: Function which can work with other function.
# Function in parameter in another function like variable.


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()