import datetime
import pyrebase
from flask import Flask, render_template, request


# Database Configration
config = {
    "apiKey": "AIzaSyD8XfrhLtN6DknYxfAJKkIkJJwII1CqG2Q",
    "authDomain": "stubby-78a46.firebaseapp.com",
    "databaseURL": "https://stubby-78a46-default-rtdb.firebaseio.com/",
    "projectId": "stubby-78a46",
    "storageBucket": "stubby-78a46.appspot.com",
    "messagingSenderId": "819719849099",
    "appId": "1:819719849099:web:08dcb10568a7bd0f49408e",
    "measurementId": "G-K1JXVJXPMY"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("names").push({"name": "Srijan"})
# db.child("names").push({"roll": "2110991384"})


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            # this is to push the data to the database
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            db.child("users").push(
                {"password": password,
                 "email": email,
                 "name": name
                 })
            # this is to get the data the data from the database
            todo = db.child("users").get()
            to = todo.val().values()

            return render_template('index.html', t=to)

        elif request.form['submit'] == 'delete':
            db.child("users").remove()
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=2002)
