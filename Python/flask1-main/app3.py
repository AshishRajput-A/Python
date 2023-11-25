from flask import Flask

app = Flask(__name__)

@app.route("/a1")
def hello():
    return "Welcome to TATA Corporation"


@app.route("/a2")
def detail():
    
    return "COMPANY NAME .: TATA CORPORATION"+"LOCATION .: INDIA"+"CONTACT-DETAIL.:982-476-0883" 

if __name__== '__main__':
    app.run(host="0.0.0.0")