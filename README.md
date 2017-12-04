
# Conversational Financial Plan Tracker (CFPT-Bot)
 
### Juan M. Huerta  (c)  2017

## Description:


This is a self contained system for interactive finance tracking in conversational mode. Contains basic NLU, chat, visual and backend components.




##  Dialog Manager - FSM

Allows for mixed initiative. Directed dialog options when necessary.

## Interaction Rendering

Mixed of chat-like interaction with discrete button choices and graphs.

## Natural Language Understanding Unit

Tight small domain parsing.


## Prediction Engine

Forecast engine to help track goals.

## Natural Language Generation

For backend summaries


## Backend

Persists user information, provides access to transactional events. Persists goals.

Persistnce is carried out using a MongoDb database.



## Domain Specification Object

In memory, keeps track of information provided and available states and substates.

## Running

cd src
export FLASK_APP=v05.py
flask run


go to the browser: localhost:5000


## Dependencies:





### Flask : microframework

### convForm : styles for interactive html pages 

### MongoDB and pymongo for backend persistence


