from flask import Flask
from be.view import auth

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.register_blueprint(auth.bp_auth)
    app.run()
