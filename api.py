from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/throttle")
def throttle():
    return jsonify({ 
        'value':1
        })
