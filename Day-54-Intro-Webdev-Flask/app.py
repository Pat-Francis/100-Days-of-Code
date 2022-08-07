from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# Use 'flask run' in terminal to run Flask web server
