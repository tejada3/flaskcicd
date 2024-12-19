from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/jose")
def hello_jose():
    return "Hello Jose"


@app.route("/coop")
def hello_coop():  # put application's code here
    return "Hello Coop"


if __name__ == "__main__":
    app.run()
