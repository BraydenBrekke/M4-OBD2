import obd
import time 

connection = obd.Async() # same constructor as 'obd.OBD()'
print(connection.port_name())

connection.watch(obd.commands.RPM) # keep track of the RPM
connection.watch(obd.commands.SPEED) # keep track of the RPM
connection.watch(obd.commands.OIL_TEMP) # keep track of the RPM
connection.watch(obd.commands.THROTTLE_POS) # keep track of the RPM
#connection.watch(obd.commands.MONITOR_BOOST_PRESSURE_B1) # keep track of the RPM

connection.start() # start the async update loop

print(connection.query(obd.commands.RPM).value)
payload = {
        "RPM" : connection.query(obd.commands.RPM).value,
        "SPEED" : connection.query(obd.commands.SPEED).value,
        "OIL_TEMP" : connection.query(obd.commands.OIL_TEMP).value,
        "THROTTLE_POS" : connection.query(obd.commands.THROTTLE_POS).value,
        "BOOST" : connection.query(obd.commands.MONITOR_BOOST_PRESSURE_B1).value,
}
print(payload)
connection.stop()

