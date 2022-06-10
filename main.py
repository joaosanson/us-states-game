import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim = turtle.Turtle()
tim.hideturtle()

all_states = data.state.to_list()
turtle.shape(image)
game_is_on = True
already_guessed = []
score = 0
while len(already_guessed) < 50:
    answer = screen.textinput(title=f"{len(already_guessed)}/50 States Correct",
                              prompt="What's another state's name").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in already_guessed]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states and answer not in already_guessed:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        answer_state = data[data.state == answer]
        answer_x = int(answer_state.x)
        answer_y = int(answer_state.y)
        tim.goto(answer_x, answer_y)
        tim.write(answer, align="center")
        already_guessed.append(answer)
