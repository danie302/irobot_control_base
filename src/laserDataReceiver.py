#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import socket
import json
import yaml
import os
IP=os.environ.get("IPbaseDRI")

def LaserReceiver():
    pub = rospy.Publisher('scan', LaserScan, queue_size=10)
    rospy.init_node('LaserReceiver', anonymous=True)
    rate = rospy.Rate(500000) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, 4001))
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(12824)
        data= yaml.load(data)
        data= json.dumps(data, indent= 4)
        data = json.loads(data)
        intensities = data["intensities"]
        intensities[:] = [float(x) for x in intensities]
        ranges = data["ranges"]
        ranges[:] = [float(x) for x in ranges]
        laser = LaserScan()
        laser.header.stamp=rospy.Time.now()
        laser.header.frame_id = data["header"]["frame_id"].encode("ascii")
        laser.header.seq = data["header"]["seq"]
        laser.angle_min = data["angle_min"]
        laser.angle_max = data["angle_max"]
        laser.angle_increment = data["angle_increment"]
        laser.time_increment = data["time_increment"]
        laser.range_min = data["range_min"]
        laser.range_max = data["range_max"]
        laser.scan_time = data["scan_time"]
        laser.ranges = ranges
        laser.intensities = intensities
        pub.publish(laser)
        rate.sleep()

if __name__ == '__main__':
    try:
        LaserReceiver()
    except rospy.ROSInterruptException:
        pass