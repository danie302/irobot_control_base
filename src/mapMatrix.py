#!/usr/bin/env python
import rospy
import os
from nav_msgs.msg import OccupancyGrid

def callback(msg):
    width = msg.info.width
    height = msg.info.height
    resolution = msg.info.resolution
    map = msg.data 
    dir = os.path.dirname(os.path.abspath(__file__)) + '/map.txt'
    with open(dir,"w") as f:
        f.write(str(map))


def listener():
    rospy.init_node('mapMatrix', anonymous=True)

    rospy.Subscriber("map", OccupancyGrid, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
