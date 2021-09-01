import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# TODO: Add exception handling for when there are no more words to learn
# Load words_to_learn.csv (if it exists), if not load french_words.csv into Pandas Dataframe and create Dictionary
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # Update canvas text and background image
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Update canvas text and background image
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def known_words():
    to_learn.remove(current_card)
    # Create new Dataframe from to_learn and export to CSV
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI
# Create Tkinter window
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip_card)

# Create canvas and configure
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Add and place card image in canvas
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 265, image=card_front_image)

# Add text to canvas
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Add the buttons
wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_words)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
