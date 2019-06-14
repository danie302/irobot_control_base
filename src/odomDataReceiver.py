#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import socket
import json
import yaml

def OdomReceiver():
    pub = rospy.Publisher('scanPiOdom', LaserScan, queue_size=10)
    rospy.init_node('OdomReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind(("192.168.1.65", 4003))
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        print data
        #laser = LaserScan()
        #pub.publish(laser)
        rate.sleep()

if __name__ == '__main__':
    try:
        OdomReceiver()
    except rospy.ROSInterruptException:
        pass