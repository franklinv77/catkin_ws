#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from random_stuff.srv import random, randomRequest, randomResponse

def random_service(*args):
    rospy.wait_for_service('random')
    global random 
    try:
        random = rospy.ServiceProxy('random', random)
        resp1 = random(*args)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":

    a = rospy.Header()
    a.seq = 1
    a.stamp = rospy.Time(3, 2)
    a.frame_id = "tests" 
    random_service(a)