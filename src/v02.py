from flask import Flask, flash, redirect, render_template, \
     request, url_for
import random

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class state_machine:
    def __init__(self):
        self.global_state={'001':0,'002':1}
        self.state_queries={0:["Hi, Im Marcus.","what can I do for you?"], 1:["Ok, What's your UserID please?"], 2:["Your balance is 200 dollars"], 3:["Good, glad to be of help"]}
        self.options={2:["Here are the details: Your balance is 200. More details?",["More details","No thanks"]]}
        self.expect_decision=False

cm = state_machine()
user='001'

@app.route('/')
def state_machine():
    name = request.args.get("name")        
    if cm.expect_decision is True:
        feedback = request.args.get("decision")        
        if not feedback is None:
            flash("Got it," + feedback,"feedback")
        

    if cm.global_state[user] in cm.state_queries:
        messages=cm.state_queries[cm.global_state[user]]
        if cm.global_state[user] in cm.options:
            cm.expect_decision=True
            flash(cm.options[cm.global_state[user]][0],"prompt")
            for x in cm.options[cm.global_state[user]][1]:
                flash(x,"options")
        else:
            cm.expect_decision=False
        if not name is None:
            pass
        cm.global_state[user]+=1
    else:
        messages=["Ok. Reached dialog completion. Lets startover."]
        cm.global_state[user]=0
        messages+=cm.state_queries[cm.global_state[user]]
        if not name is None:
            pass
        cm.global_state[user]+=1

### Plug all till the last one to feedback queue and the rest to next_message
    if len(messages)>1:
        for i in range(len(messages)-1):
            message=messages[i]
            flash(message,"feedback")
    message=messages[-1]
    flash(message,"next_message")
            
    return render_template('index.html')


