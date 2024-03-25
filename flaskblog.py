from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!<h1>"

@app.route("/about")
def about_page():
    return "<h1>I'm a software Engineer</h1>"


if __name__ == "__main__":
    app.run(debug=True)