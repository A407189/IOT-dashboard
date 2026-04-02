from flask import Flask, render_template, request, redirect, url_for, jsonify
import random

app = Flask(__name__)

# LOGIN DETAILS
USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == USERNAME and pwd == PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid Username or Password"

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/data")
def data():
    temperature = random.randint(25, 40)
    voltage = random.randint(210, 240)
    return jsonify({"temp": temperature, "volt": voltage})


if __name__ == "__main__":
    app.run(debug=True)