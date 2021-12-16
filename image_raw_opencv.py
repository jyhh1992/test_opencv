#! /usr/bin/env python3

import rospy
import cv2

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


global bridge
bridge = CvBridge()

def callback(data):
    
    cv_image =  bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('callback',cv_image)
    cv2.waitKey(1)
    pass
def main():
    rospy.init_node('img_opencv')
    rospy.Subscriber('/usb_cam/image_raw',Image,callback)
    rospy.spin()
    

if __name__ =='__main__':

    main()
    pass