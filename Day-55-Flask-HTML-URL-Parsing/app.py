from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def make_bold(function):
    def wrap_text():
        return f"<b>{function()}</b>"
    return wrap_text


def make_italic(function):
    def wrap_text():
        return f"<i>{function()}</i>"
    return wrap_text


def make_underlined(function):
    def wrap_text():
        return f"<u>{function()}</u>"
    return wrap_text


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run()