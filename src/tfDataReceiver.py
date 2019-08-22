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
tf = TransformStamped()
tf2 =TransformStamped()
def tfReceiver():
    global tf
    pub = rospy.Publisher('tf', TFMessage, queue_size=10)
    rospy.init_node('tfReceiver', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, 4004))
    i = 0
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data = json.loads(data)
        if(len(data["transforms"]) == 1):
            pub.publish(singleTf(data))
        if(len(data["transforms"]) == 2):
            pub.publish(doubleTf(data))

        #pub.publish(tf)
        rate.sleep()


def singleTf(data):
    print "-----------------------------------------------"
    #print data["transforms"][0]["header"]["stamp"]["secs"]
    tf.header.stamp.secs= data["transforms"][0]["header"]["stamp"]["secs"]
    tf.header.stamp.nsecs= data["transforms"][0]["header"]["stamp"]["nsecs"]
    tf.header.frame_id= str(data["transforms"][0]["header"]["frame_id"])
    tf.header.seq= data["transforms"][0]["header"]["seq"]
    tf.child_frame_id= str(data["transforms"][0]["child_frame_id"])
    tf.transform.translation.x=data["transforms"][0]["transform"]["translation"]["x"]
    tf.transform.translation.y=data["transforms"][0]["transform"]["translation"]["y"]
    tf.transform.translation.z=data["transforms"][0]["transform"]["translation"]["z"]
    tf.transform.rotation.x=data["transforms"][0]["transform"]["rotation"]["x"]
    tf.transform.rotation.y=data["transforms"][0]["transform"]["rotation"]["y"]
    tf.transform.rotation.z=data["transforms"][0]["transform"]["rotation"]["z"]
    tf.transform.rotation.w=data["transforms"][0]["transform"]["rotation"]["w"]    
    tfm = TFMessage([tf])
    return tfm

def doubleTf(data):
    print "-----------------------------------------------"
    global tf, tf2
    tf.header.stamp.secs= data["transforms"][0]["header"]["stamp"]["secs"]
    tf.header.stamp.nsecs= data["transforms"][0]["header"]["stamp"]["nsecs"]
    tf.header.frame_id= str(data["transforms"][0]["header"]["frame_id"])
    tf.header.seq= data["transforms"][0]["header"]["seq"]
    tf.child_frame_id= str(data["transforms"][0]["child_frame_id"])
    tf.transform.translation.x=data["transforms"][0]["transform"]["translation"]["x"]
    tf.transform.translation.y=data["transforms"][0]["transform"]["translation"]["y"]
    tf.transform.translation.z=data["transforms"][0]["transform"]["translation"]["z"]
    tf.transform.rotation.x=data["transforms"][0]["transform"]["rotation"]["x"]
    tf.transform.rotation.y=data["transforms"][0]["transform"]["rotation"]["y"]
    tf.transform.rotation.z=data["transforms"][0]["transform"]["rotation"]["z"]
    tf.transform.rotation.w=data["transforms"][0]["transform"]["rotation"]["w"]
    #--------------------------------------------------------------------------
    tf2.header.stamp.secs= data["transforms"][1]["header"]["stamp"]["secs"]
    tf2.header.stamp.nsecs= data["transforms"][1]["header"]["stamp"]["nsecs"]
    tf2.header.frame_id= str(data["transforms"][1]["header"]["frame_id"])
    tf2.header.seq= data["transforms"][1]["header"]["seq"]
    tf2.child_frame_id= str(data["transforms"][1]["child_frame_id"])
    tf2.transform.translation.x=data["transforms"][1]["transform"]["translation"]["x"]
    tf2.transform.translation.y=data["transforms"][1]["transform"]["translation"]["y"]
    tf2.transform.translation.z=data["transforms"][1]["transform"]["translation"]["z"]
    tf2.transform.rotation.x=data["transforms"][1]["transform"]["rotation"]["x"]
    tf2.transform.rotation.y=data["transforms"][1]["transform"]["rotation"]["y"]
    tf2.transform.rotation.z=data["transforms"][1]["transform"]["rotation"]["z"]        
    tf2.transform.rotation.w=data["transforms"][1]["transform"]["rotation"]["w"]
    tfm = TFMessage([tf, tf2])
    return tfm


if __name__ == '__main__':
    try:
        tfReceiver()
    except rospy.ROSInterruptException:
        pass

{u'transforms': [{u'header': {u'stamp': {u'secs': 1565392634, u'nsecs': 190188707}, u'frame_id': u'odom', u'seq': 0}, u'transform': {u'translation': {u'y': 6.30758449915e-07, u'x': 0.000666846521199, u'z': 0.0}, u'rotation': {u'y': 0.0, u'x': 0.0, u'z': 0.000945882032209, u'w': 0.999999552653}}, u'child_frame_id': u'base_footprint'}]}
#------------------------------------------------------------------
#{u'transforms': [{u'header': {u'stamp': {u'secs': 1565392518, u'nsecs': 591193230}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': 0.1175, u'x': 0.0, u'z': 0.015}, u'rotation': {u'y': 0.00617446971455, u'x': 0.0, u'z': 0.0, u'w': 0.99998093778}}, u'child_frame_id': u'left_wheel_link'}, {u'header': {u'stamp': {u'secs': 1565392518, u'nsecs': 591193230}, u'frame_id': u'base_link', u'seq': 0}, u'transform': {u'translation': {u'y': -0.1175, u'x': 0.0, u'z': 0.015}, u'rotation': {u'y': 0.0123487040309, u'x': 0.0, u'z': 0.0, u'w': 0.999923751847}}, u'child_frame_id': u'right_wheel_link'}]}
#------------------------------------------------------------------

