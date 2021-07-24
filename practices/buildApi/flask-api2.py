from flask import Flask

my_app = Flask(__name__)


@my_app.route("/")
def homePage():
    return "<h1>This is Ellie's home page</h1>"

@my_app.route("/ellie-page")
def elliePage():
    return "<h1>Welcome!This is ellie's page!!</h1>"

@my_app.route("/<number>")
def calculate(number):
    result = int(number) * 100
    return f"you need to pay {result}"



if __name__ == "__main__":
    my_app.run()
