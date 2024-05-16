from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddf638ac4d79c754ba2e59154b2a2fcb'

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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)