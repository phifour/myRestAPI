from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello, World!"


@app.route('/user/<username>')
def profile(username):
    return username
