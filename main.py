from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter color: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

def get_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    return turtle

for turtle_index in range(0, 6):
    t = get_turtle(colors[turtle_index])
    t.goto(x=-210,y= y_pos[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            is_race_on = False
            if win_color == user_bet:
                print("you win!")
            else:
                print(f"you lose. winner {win_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
