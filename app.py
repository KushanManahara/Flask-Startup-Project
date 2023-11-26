from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("Login successfull!")
        return redirect(url_for("user"))

    else:  # get
        if "user" in session:
            flash("Already logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        return render_template("user.html", user=usr)

    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")
def nameFunc(name):
    return f"My name is {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route("/user")
def view():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
