from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import socket
import time
import exception
import math
import argparse
def ConnectMyCopter():
    parser = argparse.ArgumentParser(description='commands')

    parser.add_argument('--connect')
    args= parser.parse_args()
    connection_string = args.connect
    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()
    vehicle = connect(connection_string, wait_ready=True)
    return vehicle
vehicle =ConnectMyCopter()
def armandtakeoff(TargetHeight):
    while vehicle.is_armable !=True:
        print('waiting for vehicle to become armable')

        time.sleep(1)
    print('vehicle is now armable')
    vehicle.mode = VehicleMode("GUIDED")
    while vehicle.mode != 'GUIDED':
        print("waiting for drone to enter GUIDED Flight mode")
        time.sleep(1)
    print("vehicle in Guided Mode, have fun")
    vehicle.armed = True
    while not vehicle.armed:
        print('waiting for vehicle to be armed')
        sleep(1)
    print("vehicle is armed")
armandtakeoff(10)
