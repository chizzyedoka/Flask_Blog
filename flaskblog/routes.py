from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

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
