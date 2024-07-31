from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyCH4m5kxMrUhSeddnBZz3XBnzMByoyDPUI",
  'authDomain': "database-fbf25.firebaseapp.com",
  'databaseURL': "https://database-fbf25-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "database-fbf25",
  'storageBucket': "database-fbf25.appspot.com",
  'messagingSenderId': "94806808302",
  'appId': "1:94806808302:web:6629ee95c6c69cdba205ff",
  'measurementId': "G-B4RVZF7D58"
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth

@app.route('/')
def begin():
	return render_template('start.html')

@app.route('/signin')
def signin():
  return render_template('signin.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/home', methods=["POST", "GET"])
def home():
  return render_template('home.html')

@app.route('/aboutus')
def about():
  return render_template('aboutus.html')

@app.route('/lion')
def lion():
  return render_template('lion.html')

@app.route('/ferret')
def ferret():
  return render_template('ferret.html')

@app.route('/raccoon')
def raccoon():
  return render_template('raccoon.html')

@app.route('/favorites')
def favorites():
  return render_template('favorites.html')

if __name__ == '__main__':
    app.run(debug=True)