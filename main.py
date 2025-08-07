import turtle
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 states is correct", prompt="Guess another state?").title()

    if guess == "Exit":
        break
    if guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(state_data.x.item(), state_data.y.item())  # best practice is  to use item() at the end but this is my way of solving the error
        t.write(guess)  # you can also get this by using state_data.state.item() , but this is my style

remaining_states = []

for state in all_states:
    if state not in guessed_states:
        remaining_states.append(state)
db_states = pandas.DataFrame(remaining_states)
db_states.to_csv("remaining_states.csv")
