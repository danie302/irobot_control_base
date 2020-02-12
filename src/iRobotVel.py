#!/usr/bin/env python
import rospy
import socket
from geometry_msgs.msg import Twist
import os

IP="ubuntu.local"

def callback(msg):
    vel = []
    vel.append(msg.linear.x)
    vel.append(msg.linear.y)
    vel.append(msg.linear.z)
    vel.append(msg.angular.x) 
    vel.append(msg.angular.y) 
    vel.append(msg.angular.z)
    vel = str(vel)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(vel, (IP, 4005))

def velSubs():
    rospy.init_node('iRobotVel', anonymous=True)

    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    velSubs()
