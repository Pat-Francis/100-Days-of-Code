from random import randint
from flask import Flask
app = Flask(__name__)
answer = randint(1, 9)


@app.route('/')
def homepage():
    return '<h1>Guess a number between 1 and 9</h1><p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def load_guess(guess):
    if guess == answer:
        return "<font color='green'>You're right!</font> <P>" \
               "<img src='https://media.giphy.com/media/3oFzmkkwfOGlzZ0gxi/giphy.gif'>"
    elif guess > answer:
        return "<font color='red'>Guess is too high!</font><P>" \
               "<img src='https://media.giphy.com/media/UVsEApdS35zdJitRBd/giphy.gif'>"
    else:
        return "<font color='red'>Guess is too low!</font><P>" \
               "<img src='https://media.giphy.com/media/5YL1YP9eT62KPhGabk/giphy.gif'>"


if __name__ ==  '__main__':
    app.run()
