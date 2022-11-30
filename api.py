from flask import Flask, jsonify
import obd

connection = obd.OBD("/dev/ttyUSB0") # auto connect


app = Flask(__name__)
print(connection.query(obd.commands.RPM).value)

@app.route("/")
def car_data():
    payload = { 
        "RPM": float("{:.2f}".format(connection.query(obd.commands.RPM).value.magnitude),
        "SPEED": float("{:.2f}".format(connection.query(obd.commands.SPEED).value.to("mph").magnitude),
        "TEMP": float("{:.2f}".format(connection.query(obd.commands.OIL_TEMP).value.to("fahrenheit").magnitude),
        "THROTTLE": float("{:.2f}".format(connection.query(obd.commands.THROTTLE_POS).value.magnitude),
        "BOOST": float("{:.2f}".format(connection.query(obd.commands.INTAKE_PRESSURE).value.to("psi").magnitude)
    }
    return jsonify(payload)
