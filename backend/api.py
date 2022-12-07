from flask import Flask, jsonify
import obd
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

connection = obd.OBD() # auto connect
f = open("/home/pi/OBD2/m4.log", "a")

@app.route("/")

def car_data():
    payload = { 
        "RPM": float("{:.2f}".format(connection.query(obd.commands.RPM).value.magnitude)),
        "SPEED": float("{:.2f}".format(connection.query(obd.commands.SPEED).value.to("mph").magnitude)),
        "TEMP": float("{:.2f}".format(connection.query(obd.commands.OIL_TEMP).value.to("celsius").magnitude)),
        "THROTTLE":  abs(float("{:.0f}".format(13-connection.query(obd.commands.THROTTLE_POS).value.magnitude))),
        "BOOST": float("{:.2f}".format(connection.query(obd.commands.INTAKE_PRESSURE).value.to("psi").magnitude))
    }
    
    f.write(serialize_log(payload) + "\n")

    return jsonify(payload)

def serialize_log(payload):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    RPM = payload["RPM"]
    SPEED = payload["SPEED"]
    TEMP = payload["TEMP"]
    THROTTLE = payload["THROTTLE"]
    BOOST = payload["BOOST"]

    return f'{current_time} [RPM:{RPM},SPEED:{SPEED},TEMP:{TEMP},THROTTLE:{THROTTLE},BOOST:{BOOST}]'
