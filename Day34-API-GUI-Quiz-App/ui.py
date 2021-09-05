import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create and configure the Tkinter window
        self.window = tkinter.Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create the scoreboard
        self.scoreboard = tkinter.Label(bg=THEME_COLOR, fg="white", text=f"Score: 0")
        self.scoreboard.grid(row=0, column=1)

        # Create the question canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Add text to the canvas
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="question goes here",
            width=280,
            font=("Arial", 20, "italic"),
            fill="black"
        )

        # Create the 'True' Button
        true_button_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_button_image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.true_click
        )
        self.true_button.grid(row=2, column=0)

        # Create the 'False' Button
        false_button_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_button_image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.false_click
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz completed!\nYour score was {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            print(is_right)
            self.canvas.config(bg="green")
        else:
            print(is_right)
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
