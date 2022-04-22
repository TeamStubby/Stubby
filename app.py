import datetime
from email import message
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
    return render_template('index.html')


@app.route('/select/')
def select():
    return render_template('select.html')


@app.route('/template/')
def template():
    return render_template('template.html')

@app.route('/design/')
def design():
    return render_template('design.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # this is to push the data to the database
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        # password = request.form['password']
        db.child("users").push(
            {"password": "Ganpati Bappa",
             "email": email,
             "name": name,
             "message": message,
             "subject": subject
             })
        # this is to get the data the data from the database
        todo = db.child(r"users/-N0IF-qmRlFtCbVsjxWi").get()
        to = todo.val()['name']
        print(to)
        return render_template('index.html', t=to)

    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=2002)
