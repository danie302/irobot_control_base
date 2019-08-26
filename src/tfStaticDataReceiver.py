#!/usr/bin/env python
# ----------------------------------------------------------------------------
import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped
import socket
import json
import yaml
import os
IP=os.environ.get("IPbaseDRI")
def tfReceiver():
    pub = rospy.Publisher('tf_static', TFMessage, queue_size=10)
    rospy.init_node('tfStaticReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, 4005))
    i = 0
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        array = []
        for x in range(0, 8):
            tf = TransformStamped()
            #tf.header.stamp.secs= data["transforms"][x]["header"]["stamp"]["secs"]
            #tf.header.stamp.nsecs= data["transforms"][x]["header"]["stamp"]["nsecs"]
            tf.header.stamp=rospy.Time.now()
            tf.header.frame_id= str(data["transforms"][x]["header"]["frame_id"])
            tf.header.seq= data["transforms"][x]["header"]["seq"]
            tf.child_frame_id= str(data["transforms"][x]["child_frame_id"])
            tf.transform.translation.x=data["transforms"][x]["transform"]["translation"]["x"]
            tf.transform.translation.y=data["transforms"][x]["transform"]["translation"]["y"]
            tf.transform.translation.z=data["transforms"][x]["transform"]["translation"]["z"]
            tf.transform.rotation.x=data["transforms"][x]["transform"]["rotation"]["x"]
            tf.transform.rotation.y=data["transforms"][x]["transform"]["rotation"]["y"]
            tf.transform.rotation.z=data["transforms"][x]["transform"]["rotation"]["z"]
            tf.transform.rotation.w=data["transforms"][x]["transform"]["rotation"]["w"]
            array.append(tf)
        tfm = TFMessage([array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7]])
        print "--------------------------------------"
        print tfm
        pub.publish(tfm)
        rate.sleep()


if __name__ == '__main__':
    try:
        tfReceiver()
    except rospy.ROSInterruptException:
        pass

{u'transforms': [{u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334611189}, u'frame_id': u'base_footprint', u'seq': 0}, u'transform': {u'translation': {u'y': 0.0, u'x': 0.0, u'z': 0.017}, u'rotation': {u'y': 0.0, u'x': 0.0, u'z': 0.0, u'w': 1.0}}, u'child_frame_id': u'base_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334678324}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': 0.14, u'x': 0.07, u'z': 0.01}, u'rotation': {u'y': 0.707106781185, u'x': 0.0, u'z': 0.0, u'w': 0.707106781188}}, u'child_frame_id': u'left_cliff_sensor_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334703012}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': 0.04, u'x': 0.15, u'z': 0.01}, u'rotation': {u'y': 0.707106781185, u'x': 0.0, u'z': 0.0, u'w': 0.707106781188}}, u'child_frame_id': u'leftfront_cliff_sensor_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334714574}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': -0.14, u'x': 0.07, u'z': 0.01}, u'rotation': {u'y': 0.707106781185, u'x': 0.0, u'z': 0.0, u'w': 0.707106781188}}, u'child_frame_id': u'right_cliff_sensor_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334722907}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': -0.04, u'x': 0.15, u'z': 0.01}, u'rotation': {u'y': 0.707106781185, u'x': 0.0, u'z': 0.0, u'w': 0.707106781188}}, u'child_frame_id': u'rightfront_cliff_sensor_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334735043}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': -0.12, u'x': 0.09, u'z': 0.042}, u'rotation': {u'y': 0.0, u'x': 0.0, u'z': -0.479425538604, u'w': 0.87758256189}}, u'child_frame_id': u'wall_sensor_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334742803}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': 0.0, u'x': 0.13, u'z': 0.0}, u'rotation': {u'y': 0.0, u'x': 0.0, u'z': 0.0, u'w': 1.0}}, u'child_frame_id': u'front_wheel_link'}, {u'header': {u'stamp': {u'secs': 1565392682, u'nsecs': 334749887}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': 0.0, u'x': 0.0, u'z': 0.04}, u'rotation': {u'y': 0.0, u'x': 0.0, u'z': 0.0, u'w': 1.0}}, u'child_frame_id': u'gyro_link'}]}

