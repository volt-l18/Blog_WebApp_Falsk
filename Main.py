from flask import Flask , render_template , url_for

app = Flask(__name__)

posts = [
    {
        'author' : "khushal",
        'title' : "first post",
        'content' : "my first post",
        'date_of_posted' : "feb 18, 2004"
    },
    {
        'author' : "khushal",
        'title' : "second post",
        'content' : "my second post",
        'date_of_posted' : "feb 18, 2004"
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
