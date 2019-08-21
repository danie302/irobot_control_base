#!/usr/bin/env python
# ----------------------------------------------------------------------------
import rospy
from tf2_msgs.msg import TFMessage
import socket
import json
import yaml
import os
IP=os.environ.get("IPbaseDRI")

def tfReceiver():
    pub = rospy.Publisher('tf', TFMessage, queue_size=10)
    rospy.init_node('tfReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, 4004))
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        tf = TFMessage()
        print data 
        pub.publish(tf)
        rate.sleep()

if __name__ == '__main__':
    try:
        tfReceiver()
    except rospy.ROSInterruptException:
        pass