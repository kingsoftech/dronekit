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
def get_distance_meters(targetLocation,currentLocation):
	dlat= targetLocation.lat - currentLocation.lat
	dlon= targetLocation.lon - currentLocation.lon
	
	return math.sqrt(dlon*dlon)+(dlat*dlat)*1.113195e5
vehicle = connect_my_copter()
armandtakeoff(10)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3
wphome = vehicle.location.global_relative_frame
print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(wphome.lon, wphome.lat, 15)
vehicle.simple_goto(point1)

# sleep so we can see the change in map
time.sleep(30)

print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
point2 = LocationGlobalRelative(44.50137, -88.062645, 14)
vehicle.simple_goto(point2, groundspeed=10)

point2 = LocationGlobalRelative(44.501746, -88.062242, 10)
vehicle.simple_goto(point2, groundspeed=10)

# sleep so we can see the change in map
time.sleep(30)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()
