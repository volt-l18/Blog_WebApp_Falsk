from flask import Flask , render_template , url_for, flash, redirect
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
