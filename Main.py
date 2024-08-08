from flask import Flask , render_template , url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
