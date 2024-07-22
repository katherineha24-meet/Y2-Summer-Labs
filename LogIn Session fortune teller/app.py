

from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY']="PASSWORD"

fortunes=["you'll step on food", "you'll have a good day", "A cat will follow you everywhere starting now", "a bird poops on you everytime you step outside", "you'll meet a leprachuan", "I cant think of anymore. leave me be", "good night sleep", "stomach ache every 2 hours", "your life is now great.", "you get stuck with 10 gnomes who dont speak a sinlge word of english and only communicate in gibberish who are lactose intolerent and only drink milk."]

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    else:     
        login_session["name"] = request.form['name']
        login_session["month"] = request.form['month']
        return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', name=login_session["name"], month = login_session['month'])
    else:     
        return redirect(url_for('fortune',m = login_session['month'],f=True))

@app.route('/home/<f>')
def fortune(f):
    if(len(login_session['month'])>10):
        return render_template("home.html", ff = fortunes[len(login_session['month'])], flag = True, name=login_session["name"], month = login_session['month'])
    return render_template("home.html", ff = fortunes[len(login_session['month'])], flag = True, name=login_session["name"], month = login_session['month'])


if __name__ == '__main__':
    app.run(debug = True)