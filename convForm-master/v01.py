from flask import Flask, flash, redirect, render_template, \
     request, url_for
import random

app = Flask(__name__)
app.secret_key = 'some_secret'



@app.route('/')
def index():
    x=random.random()
    if x>=0.5:
        message="THis is message one"
    else:
        message="This is message two"
    flash(message)
    return render_template('index.html')
    #return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

