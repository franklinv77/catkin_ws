#!/usr/bin/env python

from matplotlib.pyplot import show
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

bridge = CvBridge()


def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)

def callback(data):
    image = bridge.imgmsg_to_cv2(data)
    show_image(image)

def listen():
    rospy.init_node('image_dislayer')
    rospy.Subscriber("webcam_video", Image, callback)
    rospy.spin()

if __name__ == "__main__":
    listen()