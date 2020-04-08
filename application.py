from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is from Python Flask Home Page"

@app.route('/about')
def about():
    return "<h2> Hello World from About page </h2>"

@app.route('/profile/<username>')
def profile(username):
    return "<h2> Welcome %s</h2>" % username
