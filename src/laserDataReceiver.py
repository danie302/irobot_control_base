#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import socket
import json
import yaml

def LaserReceiver():
    pub = rospy.Publisher('scan', LaserScan, queue_size=10)
    rospy.init_node('LaserReceiver', anonymous=True)
    rate = rospy.Rate(1000) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    IP = '192.168.0.3'
    PORT= 4001
    BUFFER_SIZE = 15024
    sock.bind((IP, PORT))
    sock.listen(1)
    while not rospy.is_shutdown():
        conn, addr = s.accept()
        print 'Connection address:', addr
        data= conn.recv(BUFFER_SIZE)
        conn.send(data)
        conn.close()
        data = json.loads(data)
        print "-----------------------------------------------------------------------"
        print data["header"]["seq"]
        print "-----------------------------------------------------------------------"
        intensities = data["intensities"]
        intensities[:] = [float(x) for x in intensities]
        ranges = data["ranges"]
        ranges[:] = [float(x) for x in ranges]
        laser = LaserScan()
        laser.header.stamp.secs = data["header"]["stamp"]["secs"]
        laser.header.stamp.nsecs = data["header"]["stamp"]["nsecs"]
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