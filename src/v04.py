from flask import Flask, flash, redirect, render_template, \
     request, url_for
import random


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class state_machine:
    def __init__(self,uid,domain_file):
        self.user_id=uid
        self.global_state=0
        self.expect_decision=False
        data = eval(' '.join([x.rstrip() for x in open(domain_file,"rt").readlines()]))
        self.state_queries=data['state_queries']
        self.options=data['options']
        self.visual_state=data['visual_state']

cm = state_machine('001','domains/pcf.01.json')
#cm = state_machine('001','domains/finn.01.json')

@app.route('/')
def interaction_rendering():

    user=cm.user_id
    name = request.args.get("name")

    ### Operations are based in the current state

    ## Does the current state have a visual component?


     ## Does the current state expects a decision to be made?
        
    if cm.expect_decision is True:
        feedback = request.args.get("decision")        

        if not feedback is None:
            flash("Got it," + feedback,"feedback")
            if feedback in cm.options[cm.global_state][1]:
                cm.global_state=cm.options[cm.global_state][1][feedback]
            else:
                cm.global_state+=1
        cm.expect_decision=False
        messages=None

    if True:

        if cm.global_state in cm.visual_state:
            flash("Showing visual","visual")

        if cm.global_state in cm.state_queries:

            messages=cm.state_queries[cm.global_state][0]

            if cm.global_state in cm.options:
                cm.expect_decision=True
                flash(cm.options[cm.global_state][0],"prompt")
                for x in cm.options[cm.global_state][1]:
                    flash(x,"options")
            else:
                cm.expect_decision=False
                if not name is None:
                    pass
                #cm.global_state+=1
                cm.global_state=cm.state_queries[cm.global_state][1]
        else:
            messages=["Ok. Reached dialog completion. Lets startover."]
            cm.global_state=0
            messages+=cm.state_queries[cm.global_state][0]
            if not name is None:
                pass
            #cm.global_state+=1
            cm.global_state=cm.state_queries[cm.global_state][1]

### Plug all till the last one to feedback queue and the rest to next_message
    if messages is not None:
        if len(messages)>1:
            for i in range(len(messages)-1):
                message=messages[i]
                flash(message,"feedback")
        message=messages[-1]
        flash(message,"next_message")
            
    return render_template('index.html')


