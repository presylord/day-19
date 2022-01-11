from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]
turtles = []

screen.setup(width=500, height=400)

for index in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[index])
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() == 230.0:
            is_race_on = False
            color = turtle.color()
            if user_bet == color[0]:
                print(f"You win! The {color[0]} turtle is the winner.")
            else:
                print(f"You lose! The {color[0]} turtle is the winner.")


