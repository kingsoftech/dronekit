from dronekit import connect,VehicleMode, LocationGlobalRelative, APIException
import time
import math
import socket
import exceptions
import argparse
def connect_my_copter():
	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()
	connection_string = args.connect
	if not connection_string:
		import dronekit_sitl
		sitl = dronekit_sitl.start_default()
		connection_string = sitl.connection_string()
	vehicle = connect(connection_string,wait_ready=True)
	return vehicle 
vehicle = connect_my_copter()
gps_type = vehicle.parameters['GPS_TYPE']
print("GPS_TYPE param value is %s" %str(gps_type))
if gps_type is not 4:
	gps_type = 4
print("GPS_TYPE param value is %s" %str(gps_type))
