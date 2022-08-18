#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
from math import sin
import time

value = 0

def sine_wave():
    
    pub = rospy.Publisher('sine_wave', Float64, queue_size=10)
    rospy.init_node('sine_wave_creator')
    rate = rospy.Rate(15)

    while not rospy.is_shutdown():
        global value
        # show_image(frame)
        sin_val = sin(value)
        value += 0.002 
#	time.sleep(1)
        pub.publish(sin_val)
        rate.sleep()

if __name__ == "__main__":
    try:
        sine_wave()
    except rospy.ROSInterruptException:
        pass
