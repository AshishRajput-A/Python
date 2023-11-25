from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello,World</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello,ashish</h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello,world2</h1>"

@app.route("/test")
def test():
    a=6+5
    return "<h1>this is my function to run app {}</h1>".format(a)

@app.route("/test2/test2")
def test2 ():
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)

@app.route("/print")
def print ():
    return " i like to play cricket"



if __name__=="__main__":
    app.run(host="0.0.0.0")
