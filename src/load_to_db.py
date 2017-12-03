import sys
import random
import pymongo
from pymongo import MongoClient


def load_user(posts):
    fp=open("domains/backend_data.json","rt")
    for x in fp:
        y=eval(x.rstrip().lower())
        print "loading", y
        result = posts.insert_one(y)


def show_all(posts):
    j_posts = posts.find({'user_id': 'juan123'})
    for post in j_posts:
        print "Found", post


def main():
    client = MongoClient()
    db = client.cfptbot
    posts = db.posts
    load_user(posts)
    show_all(posts)

if __name__== "__main__":
    main()
    

