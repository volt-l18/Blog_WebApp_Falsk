from flask import Flask , render_template , url_for
from Forms import RegistrationFrom , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '457e9068bdca2a4d6cdf300d3e510c49'

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

@app.route("/register")
def register():
    form = RegistrationFrom()
    return render_template("register.html" , title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html" , title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)
