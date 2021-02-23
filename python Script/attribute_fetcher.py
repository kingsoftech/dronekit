from dronekit import connect,VehicleMode, LocationGlobalRelative, APIException
import time
import math
import socket
import argparse
import exceptions
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
vehicle.wait_ready('autopilot_version')
print('autopilot version: %s' %vehicle.version)
print('supports set altitude from companion: %s'%vehicle.capabilities.set_attitude_target_local_ned)
print('location: %s' %vehicle.location.global_relative_frame)
print('velocities: %s'%vehicle.velocity)
print('altitude: %s'%vehicle.attitude)
print('last_heartbeat: %s' %vehicle.last_heartbeat)
print('is the vehicle armable: %s' %vehicle.is_armable)
print('groundspeed: %s',vehicle.groundspeed)
print('Mode: %s'%vehicle.mode.name)
print('Armed: %s'%vehicle.armed)
print('EKF ok: %s' %vehicle.ekf_ok)
vehicle.close()
