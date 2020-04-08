from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Python Flask app stored in Github"
    return "Hello Python"
