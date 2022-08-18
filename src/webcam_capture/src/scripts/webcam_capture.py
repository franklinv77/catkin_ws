#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

vid = cv2.VideoCapture(0)
bridge = CvBridge()

def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)

def capture():
    
    pub = rospy.Publisher('webcam_video', Image, queue_size=10)
    rospy.init_node('image_capturer')
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():

        ret, frame = vid.read()        
        # show_image(frame)
        
        image_msg = bridge.cv2_to_imgmsg(frame)
        pub.publish(image_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        capture()
    except rospy.ROSInterruptException:
        pass