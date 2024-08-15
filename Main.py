from datetime import datetime
from flask import Flask , render_template , url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from Forms import RegistrationFrom , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '457e9068bdca2a4d6cdf300d3e510c49'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String[20], unique = True , nullable = False)
    email = db.Column(db.String[120], unique = True , nullable = False)
    image_file = db.Column(db.String[20], nullable = False, default = 'default.jpeg')
    password = db.Column(db.String[60], nullable = True)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String[100], nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author' : "Khushal",
        'title' : "First post",
        'content' : "My first post",
        'date_posted' : "Feb 18, 2004"
    },
    {
        'author' : "Khushal",
        'title' : "Second post",
        'content' : "My second post",
        'date_posted' : "Feb 18, 2004"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html' , title = "About")

@app.route("/register" , methods = ['GET', 'POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!' , 'success')
        return redirect(url_for('home'))
    return render_template("register.html" , title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'abc@abc.com' and form.password.data == 'password':
            flash('you have been logged in !' , 'success')
            return redirect(url_for('home'))
        else:
            flash("Log in unsuccessfull! Please try again" , "danger")
    return render_template("login.html" , title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)
