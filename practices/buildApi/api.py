from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/home")
def home():
    return "<h1> Helloo Ellie :P </h1>"

@app.route("/<name>")
def user(name):
    return f"helloo new user named {name} :)"


@app.route("/admin")
def admin():
    # we put the name of the function inside of the url_for , for redirecting to that page
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run()
