from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-me")
def aboutme():
    return render_template("/aboutme.html")


@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")


@app.route("/hairsalon")
def hairsalon():
    return render_template("/hairsalon.html")


if __name__ == '__main__':
    app.run()
