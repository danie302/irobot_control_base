#!/usr/bin/env python
import rospy
import socket
from geometry_msgs.msg import Twist
import os

IP=os.environ.get("IPraspiDRI")

def callback(msg):
    vel[0] = msg.linear.x
    vel[1] = msg.linear.y 
    vel[2] = msg.linear.z 
    vel[3] = msg.angular.x 
    vel[4] = msg.angular.y 
    vel[5] = msg.angular.z
    vel = str(vel)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(vel, (IP, 4005))

def velSubs():
    rospy.init_node('iRobotVel', anonymous=True)

    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    velSubs()
