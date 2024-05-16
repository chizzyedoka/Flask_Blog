from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Chisom Edoka',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 25, 2024'
    },
     {
        'author': 'Samuel Edoka',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 26, 2024'
    },
]

@app.route("/")
def greet():
    return "hello world"

@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)