#!/usr/bin/env python3
import rospy
import sys
import rosbag
from sensor_msgs.msg import LaserScan

def callback(msg):
    # Serialize the message to a string
    serialized_message = rospy.msg.serialize_message(msg)

    # Calculate the size of the serialized message in bytes
    size_in_bytes = sys.getsizeof(serialized_message)

    # Print the size of the message
    rospy.loginfo('Size of the message: %s bytes', size_in_bytes)

def listener():
    rospy.init_node('message_size_listener', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()