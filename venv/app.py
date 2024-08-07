from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/calculator")
def calculation():
    return render_template("calculator.html")


if __name__ == "__main__":
    app.run(debug=True)
