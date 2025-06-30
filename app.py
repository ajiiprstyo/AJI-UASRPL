import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good broo, how about you?'

@app.route('/about')
def about():
    return 'This is an about page.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
