#!/usr/bin/env python3

from __future__ import print_function

from random_stuff.srv import random, randomResponse
import rospy

def handle_random(data):
    #print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    #return randomResponse(req.a + req.b)

    print(str(data))

    #sum = data.value1 + data.value2
    #for val in data.values:
    #    sum += val

    #print(f"The sum of the values is: {sum}")

    return 0#int(sum)

def random_server():
    rospy.init_node('random_server')
    s = rospy.Service('random', random, handle_random)
    print("Ready randomly.")
    rospy.spin()

if __name__ == "__main__":
    random_server()
