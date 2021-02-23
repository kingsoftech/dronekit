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
while vehicle.is_armable!=True:
	print('waiting for vehicle to be armable')
	time.sleep(1)
print('vehicle is armable')
vehicle.mode=VehicleMode("GUIDED")
while not vehicle.mode:
	print('waiting for vehicle to be in GUIDED mode')
	time.sleep(1)
print('vehicle in guided mode')
vehicle.armed = True
while not vehicle.armed:
	print('vehicle is not armed')
	time.sleep(1)
print('EKF ok: %s' %vehicle.ekf_ok)
print('props is spinning')
vehicle.close()
