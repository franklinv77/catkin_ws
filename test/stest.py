#!/usr/bin/python

from time import sleep
import serial
from formant.sdk.agent.v1 import Client as FormantClient

ser = serial.Serial('/dev/ttyACM2')
fclient = FormantClient()

# defines all the track states
LEFT_TRACK_ON = str.encode('2\n')
RIGHT_TRACK_ON = str.encode('3\n')
BOTH_TRACKS_ON = str.encode('1\n')

STOP = str.encode('0\n')
FORWARD = BOTH_TRACKS_ON
TURN_RIGHT = LEFT_TRACK_ON
TURN_LEFT = RIGHT_TRACK_ON

def tank_stop():
    ser.write(STOP)

def tank_right():
    ser.write(TURN_RIGHT)

def tank_left():
    ser.write(TURN_LEFT)

def tank_forward():
    ser.write(FORWARD)

def execute_tank_command(command):
    execute_tank_command.commands[command]()

execute_tank_command.commands = [
    tank_stop,
    tank_forward, 
    tank_left,
    tank_right
]

def handle_teleop(datapoint):
    print("New Payload")
    print(datapoint)
    linear = 0
    angular = 0
    if datapoint.stream == "Joystick":
        angular = datapoint.twist.angular.z
        linear = datapoint.twist.linear.x 
    
    print(f"Linear: {linear}")
    print(f"Angular: {angular}")

    if linear == 1:
        tank_forward()
    
    elif(angular == -1):
        tank_left()
    
    elif(angular == 1):
        tank_right()
    
    else:
        tank_stop()

fclient.register_teleop_callback(handle_teleop)

def main():
    while True:
        sleep(100)
    # direction = input("Please enter command [0-3]: ")
    # execute_tank_command(int(direction))

if __name__ == "__main__":
    main()