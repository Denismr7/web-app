from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    hi = "Hello, user! "

    return render_template("index.html", hi=hi)


@app.route("/about-me", methods=["GET", "POST"])
def aboutme():
    if request.method == "GET":
        return render_template("/aboutme.html")
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("email")
        contact_message = request.form.get("message")

        print(contact_name)
        print(contact_email)
        print(contact_message)
        return render_template("success.html")


@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")


@app.route("/hairsalon")
def hairsalon():
    return render_template("/hairsalon.html")


if __name__ == '__main__':
    app.run(debug=True)
