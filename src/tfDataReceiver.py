#!/usr/bin/env python
# ----------------------------------------------------------------------------
import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped
import socket
import json
import yaml
import os 

IP="daniel.local"
tf = TransformStamped()
tf2 =TransformStamped()
def tfReceiver():
    global tf
    pub = rospy.Publisher('tf', TFMessage, queue_size=10)
    rospy.init_node('tfReceiver', anonymous=True)
    rate = rospy.Rate(1000000) # 10hz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((IP, 4004))
    i = 0
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(15024)
        data= yaml.load(data)
        data= json.dumps(data, indent= 4)
        data = json.loads(data)
        if(len(data["transforms"]) == 1):
            pub.publish(singleTf(data))
        if(len(data["transforms"]) == 2):
            pub.publish(doubleTf(data))

        rate.sleep()


def singleTf(data):
    tf.header.stamp=rospy.Time.now()
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
    global tf, tf2
    tf.header.stamp=rospy.Time.now()
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
    tf2.header.stamp=rospy.Time.now()
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
