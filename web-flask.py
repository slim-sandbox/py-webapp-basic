# Simple web application using Flask framework
from flask import Flask
import os

HELLO_NAME = os.getenv('APP_HELLO_NAME', "World")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, {HELLO_NAME}!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
