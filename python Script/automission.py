from dronekit import connect,VehicleMode, LocationGlobalRelative, APIException,Command
import time
import math
import socket
import exceptions
import argparse
from pymavlink import mavutil
def connect_my_copter():
	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()
	connection_string = args.connect
	if not connection_string:
		import dronekit_sitl
		sitl = dronekit_sitl.start_default()
		sitl_args = ['-I0', '--model', 'quad', '--home=44.5013,-88.0622,0,180']
		sitl.launch(sitl_args, await_ready=True, restart=True)
		connection_string = sitl.connection_string()
	vehicle = connect(connection_string,wait_ready=True)
	return vehicle 
def armandtakeoff(TargetHeight):
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
	vehicle.simple_takeoff(TargetHeight)

	while True:
		print("current altitude: %d"%vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=.95*TargetHeight:
			break
		time.sleep(1)
	print("TargetHeight reached")

	vehicle.close()
 	return None
vehicle = connect_my_copter()
wphome = vehicle.location.global_relative_frame
cmd1 = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, wphome.lat, wphome.lon, wphome.alt)
cmd2 = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, 44.50137, -88.062645, 14)
cmd3 = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, 44.501746, -88.062242, 10)
cmd4 = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0, 44.50137, -88.062645, 10)
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
cmds.clear()
cmds.add(cmd1)
cmds.add(cmd2)
cmds.add(cmd3)
cmds.add(cmd4)
vehicle.commands.upload()

armandtakeoff(10)
print("after arm and take off")
vehicle.mode= VehicleMode("AUTO")
while vehicle.mode != "AUTO":
	time.sleep(.2)
while vehicle.location.global_relative_frame.alt>2:
	print("Drone is executing mission, but we can stil run code")
	time.sleep(1)

armandtakeoff(10)
vehicle.close()
