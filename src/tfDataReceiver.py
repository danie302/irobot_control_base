import rospy
from nav_msgs.msg import Odometry
import socket
import json
import yaml
import os
IP=os.environ.get("IPbaseDRI")

def OdomReceiver():
    pub = rospy.Publisher('odom', Odometry, queue_size=10)
    rospy.init_node('OdomReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind(("10.154.116.42", 4003))
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        odom = Odometry()
        odom.twist.twist.linear.y = data["twist"]["twist"]["linear"]["y"]
        odom.twist.twist.linear.x = data["twist"]["twist"]["linear"]["x"]
        odom.twist.twist.linear.z = data["twist"]["twist"]["linear"]["z"]
        odom.twist.twist.angular.y = data["twist"]["twist"]["angular"]["y"]
        odom.twist.twist.angular.x = data["twist"]["twist"]["angular"]["x"]
        odom.twist.twist.angular.z = data["twist"]["twist"]["angular"]["z"]
        odom.twist.covariance = data["twist"]["covariance"]
        odom.header.stamp.secs = data["header"]["stamp"]["secs"]
        odom.header.stamp.nsecs = data["header"]["stamp"]["nsecs"]
        odom.header.frame_id = data["header"]["frame_id"]
        odom.header.seq = data["header"]["seq"]
        odom.pose.pose.position.x = data["pose"]["pose"]["position"]["x"]
        odom.pose.pose.position.y = data["pose"]["pose"]["position"]["y"]
        odom.pose.pose.position.z = data["pose"]["pose"]["position"]["z"]
        odom.pose.pose.orientation.x = data["pose"]["pose"]["orientation"]["x"]
        odom.pose.pose.orientation.y = data["pose"]["pose"]["orientation"]["y"]
        odom.pose.pose.orientation.z = data["pose"]["pose"]["orientation"]["z"]
        odom.pose.pose.orientation.w = data["pose"]["pose"]["orientation"]["w"]
        odom.pose.covariance = data["pose"]["covariance"]
        odom.child_frame_id = data["child_frame_id"]
        pub.publish(odom)
        rate.sleep()

if __name__ == '__main__':
    try:
        OdomReceiver()
    except rospy.ROSInterruptException:
        pass