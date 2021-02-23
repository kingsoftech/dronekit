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
#def arm_and_takeoff(TargetHeight):
#	while vehicle.is_armable!=True:
#		print('waiting for vehicle to be armable')
#		time.sleep(1)
#	print('vehicle is armable')
#	vehicle.mode=VehicleMode("GUIDED")
#	while not vehicle.mode:
#		print('waiting for vehicle to be in GUIDED mode')
#		time.sleep(1)
#	print('vehicle in guided mode')
#	vehicle.armed = True
#	while not vehicle.armed:
#		print('vehicle is not armed')
#		time.sleep(1)
#	print('EKF ok: %s' %vehicle.ekf_ok)
#	print('props is spinning')
#	vehicle.simple_takeoff(TargetHeight)
#	current_attitude= vehicle.location.global_relative_frame.alt
##	while True:
##		print("current altitude %d" %current_attitude)
##		if current_attitude>=.95*TargetHeight:
##			break
##		time.sleep(1)
#	print('target attitude reached')
#	return None
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
vehicle = connect_my_copter()
#arm_and_takeoff(10)
