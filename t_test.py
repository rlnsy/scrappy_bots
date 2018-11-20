# Some simple I wrote to understand
# threads in flask

from flask import Flask
import time

import threading
import atexit


max_items = 1000000
l = []

myThread = threading.Thread()

def create_app():

    app = Flask(__name__)

    def interrupt():
        global myThread
        myThread.cancel()

    def add_to_list():
        global l
        while(True):
            print ("adding")
            if (len(l) < max_items):
                l.append(len(l))
                time.sleep(10)

    def sub_init():
        global myThread
        myThread = threading.Timer(5, add_to_list, ())
        myThread.start()

    sub_init()
    atexit.register(interrupt)
    return app

app = create_app()

@app.route("/")
def hello():
    if (len(l) > 0):
        return str(l[len(l) - 1])
    return "no list"