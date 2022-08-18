#!/usr/bin/env python3

from importlib import reload
import os
import rospy
from std_msgs.msg import Float64
from math import cos
import time
import logging
from utils import get_logger

logger = get_logger(__name__) 

value = 0

def sine_wave():
    
    pub = rospy.Publisher('cosine_wave', Float64, queue_size=10)
    rospy.init_node('cosine_wave_creator')
    # reload(logging) 
    rate = rospy.Rate(15)

    logger.debug("Running") 
    logger.warning("Warned")

    while not rospy.is_shutdown():
        global value
        # show_image(frame)
        sin_val = cos(value)
        value += 0.002 
#	time.sleep(1)
        pub.publish(sin_val)
        rate.sleep()

if __name__ == "__main__":
    try:
        sine_wave()
    except rospy.ROSInterruptException:
        pass
