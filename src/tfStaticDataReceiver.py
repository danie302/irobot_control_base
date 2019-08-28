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
        data= yaml.load(data)
        data= json.dumps(data, indent= 4)
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


