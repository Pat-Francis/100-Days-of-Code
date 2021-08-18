import turtle
import pandas
from statename import StateName

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV into Pandas
data = pandas.read_csv("50_states.csv")

# Grab the state column from the dataframe and load into a list
state_list = data["state"].to_list()

# Create empty list to store correct guesses
guessed_states = []

while len(guessed_states) < 50:
    # Ask the user for input and convert to Title Case e.g. ohio -> Ohio
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another State name?").title()

    if answer_state == "Exit":
        # Remove all guessed states from state_list
        for state in guessed_states:
            state_list.remove(state)

        # Load remaining state_list into Pandas Dataframe and export to CSV
        data_frame = pandas.DataFrame(state_list)
        data_frame.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # Get the row of data for the state in the users answer and pass to the StateName class
        state_data = data[data.state == answer_state]
        StateName(answer_state, int(state_data.x), int(state_data.y))


