from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Login with admin and 1234 at /login"

@app.route('/login')
def login():
    return """
    <form method="POST" action="/loginapi">
        <input type="name" name="id">
        <input type="password" name="pwd">
        <input type="submit" value="Login">
    </form>
    """

@app.route('/loginapi', methods=["POST"])
def loginapi():
    username = request.form["id"]
    password = request.form["pwd"]
    if username == "admin" and password == "1234":
        return "Success!"
    else:
        return "Failed!"

if __name__ == "__main__":
    app.run(debug=True)