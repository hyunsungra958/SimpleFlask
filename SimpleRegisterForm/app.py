from flask import Flask
from flask import request

app = Flask(__name__)

users = {
    "test": "test"
}

@app.route('/')
def home():
    return """
    <p>Login page is <a href="/login">here</a></p>
    <p>Register page is <a href="/register">here</a></p>
    """

@app.route('/register')
def register():
    return """
    <form method="POST" action="/api_register">
        <span>ID: </span><input type="name" name="id"><br>
        <span>Password: </span><input type="password" name="pwd"><br>
        <input type="submit" value="Register">
    </form>
    """

@app.route('/login')
def login():
    return """
    <form method="POST" action="/api_login">
        <span>ID: </span><input type="name" name="id"><br>
        <span>Password: </span><input type="password" name="pwd"><br>
        <input type="submit" value="Login">
    </form>
    """

@app.route('/api_register', methods=["POST"])
def api_register():
    username = request.form["id"]
    password = request.form["pwd"]
    if not username in users.keys():
        users[username] = password
        return "Register completed."
    else:
        return "User already exists."

@app.route('/api_login', methods=["POST"])
def api_login():
    username = request.form["id"]
    password = request.form["pwd"]
    if username in users.keys():
        if users[username] == password:
            return "Login completed."
        else:
            return "Password incorrect."
    return "Username not found."

if __name__ == "__main__":
    app.run(debug=True)