#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import socket
import json
import yaml

def LaserReceiver():
    pub = rospy.Publisher('scanPi', LaserScan, queue_size=10)
    rospy.init_node('LaserReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind(("192.168.1.65", 4001))
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        laser = LaserScan()
        laser.header.stamp.secs = data["header"]["stamp"]["secs"]
        laser.header.stamp.nsecs = data["header"]["stamp"]["nsecs"]
        laser.header.frame_id = data["header"]["frame_id"]
        laser.header.seq = data["header"]["seq"]
        laser.angle_min = data["angle_min"]
        laser.angle_max = data["angle_max"]
        laser.angle_increment = data["angle_increment"]
        laser.time_increment = data["time_increment"]
        laser.range_min = data["range_min"]
        laser.range_max = data["range_max"]
        laser.scan_time = data["scan_time"]
        laser.ranges = data["ranges"]
        laser.intensities = data["intensities"]
        pub.publish(laser)
        rate.sleep()

if __name__ == '__main__':
    try:
        LaserReceiver()
    except rospy.ROSInterruptException:
        pass