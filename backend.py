from flask import Flask, jsonify
import odb

#connection = obd.OBD("/dev/ttyUSB1") # auto-connects to USB or RF port

#cmd = obd.commands.SPEED # select an OBD command (sensor)

#response = connection.query(cmd) # send the command, and parse the response



app = Flask(__name__)

@app.route("/RPM")
def RPM():
    return jsonify({ 
        'value': getRPM()
    })
@app.route("/boost")
def boost():
    return jsonify({ 
        'value': getBoost()
    })
@app.route("/speed")
def speed():
    return jsonify({ 
        'value': getSpeed()
        })
@app.route("/gear")
def gear():
    return jsonify({ 
        'value': getGear()
        })
@app.route("/mode")
def mode():
    return jsonify({ 
        'value': getMode()
        })
    

def getRPM():
    return 1
def getBoost():
    return 1
def getSpeed():
    return 1
def getGear():
    return 1
def getMode():
    return 1