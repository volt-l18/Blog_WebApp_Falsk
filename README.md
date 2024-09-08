# FlaskBlog

## About the project:
This is a Bloging web site created completely in flask has its own db to mentain user data and privacy with our implemented one way 16-bit hashing you password with be safe and private
<br>
<hr>

## setup:
Make sure you have python installed after that we make a virtual enviorment and install the requirements
```
python -m venv env && python -r requirements.txt
```

To intialize the server you can run (with gunicorn):
```
gunicorn Run:app
```
note - if you having trouble with guincorn you can use teh other method to run the app or directly run the Run.py file with python

To intialize the server you can run (without gunicorn):
```
export FLASK_APP=Run.py && flask run
```
<br>
<hr>

## Database Management:

The database can be directly managed with the python interpreter:
first you have to push app context
```
from Run import app
app.app_context().push()
```

then you can access Database with:
```
from flaskblog import db
```

after this you can create a new blank Database with:
```
db.drop_all() # to drop the old db
db.create_all()
```

To run querrys on posts and users database:
```
from flaskblog.models import Post, User
Post.query.<required sql query>
User.query.<required sql query>
```
<br>
<hr>

## Our Contributors

<a href="https://github.com/volt-l18/Blog_WebApp_Falsk/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=volt-l18/Blog_WebApp_Falsk" />
</a>
<br>
<hr>
