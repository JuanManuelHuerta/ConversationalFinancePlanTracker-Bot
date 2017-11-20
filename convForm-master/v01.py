from flask import Flask, flash, redirect, render_template, \
     request, url_for
import random

app = Flask(__name__)
app.secret_key = 'some_secret'


global_state={'001':0,'002':1}
user='001'
state_queries={0:"Hi, Im Marcus., what can I do for you?", 1:"Ok, What's your UserID please?", 2:"Your balance is 200 dollars", 3:"Good, glad to be of help"}
options={2:["Your balance is 200",["More details","ok"]]}

@app.route('/')
def index():
    name = request.args.get("name")
        
    if global_state[user] in state_queries:
        message=state_queries[global_state[user]]
        if global_state[user] in options:
            flash(options[global_state[user]][0],"prompt")
            for x in options[global_state[user]][1]:
                flash(x,"options")
        if not name is None:
            message+= " "+name
        global_state[user]+=1
    else:
        message="Ok. Reached dialog completion. Lets startove."
        global_state[user]=0
        message+=state_queries[global_state[user]]
        if not name is None:
            message+= " "+name
        global_state[user]+=1
        
    flash(message,"next_message")
    return render_template('index.html')


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

