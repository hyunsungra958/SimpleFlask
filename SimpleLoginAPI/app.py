from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Login using id=admin and pwd=1234 at /login"

@app.route('/login', methods=["GET"])
def login():
    args = request.args
    username = args["id"]
    password = args["pwd"]
    if username == "admin" and password == "1234":
        return "Login Complete!"
    else:
        return "Login Failed."


if __name__ == '__main__':
    app.run(debug=True)