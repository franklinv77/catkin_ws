#!/usr/bin/env python3

import rospy
from test_msg.msg import Num
from math import sin

value = 0

def sine_wave():
    
    pub = rospy.Publisher('sample', Num, queue_size=10)
    rospy.init_node('sample_msg')
    rate = rospy.Rate(30)
    print("Running")
    while not rospy.is_shutdown():
        global value
        # show_image(frame)
        sin_val = sin(value)
        value += 0.002 

        #pub.publish(sin_val)
        rate.sleep()

if __name__ == "__main__":
    try:
        sine_wave()
    except rospy.ROSInterruptException:
        pass
