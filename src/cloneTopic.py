#!/usr/bin/env python
import rospy
from geometry_msgs.msg import TwistWithCovarianceStamped 
from nav_msgs.msg import Odometry

def callback(msg):
    pub = rospy.Publisher('twist0', TwistWithCovarianceStamped, queue_size=10)
    twist = TwistWithCovarianceStamped()
    twist.header = msg.header
    twist.header.frame_id = "base_link"
    twist.twist = msg.twist
    pub.publish(twist)

def twistPub():
    rospy.init_node('twistPub', anonymous=True)

    rospy.Subscriber("odom0", Odometry, callback)

    rospy.spin()
    

if __name__ == '__main__':
    print "empezo"
    twistPub()