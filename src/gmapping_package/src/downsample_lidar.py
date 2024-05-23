#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import tf2_ros
import tf_conversions
import geometry_msgs.msg
from geometry_msgs.msg import TransformStamped
#def callback(msg):
#    # Downsample the scan, take 2 readings for every 3 readings
#    downsampled_ranges = [reading for i, reading in enumerate(msg.ranges) if i % 4!= 2]
#    downsampled_intensities = [intensity for i, intensity in enumerate(msg.intensities) if i % 3 != 2]
#
#    # Create a new LaserScan message
#    downsampled_scan = LaserScan()
#    downsampled_scan.header = msg.header
#    downsampled_scan.header.stamp = rospy.Time.now()
#    downsampled_scan.header.frame_id = 'laser_frame'
#    downsampled_scan.angle_min = msg.angle_min
#    downsampled_scan.angle_max = msg.angle_max
#    downsampled_scan.angle_increment = msg.angle_increment * 1.3
#    downsampled_scan.time_increment = msg.time_increment 
#    downsampled_scan.scan_time = msg.scan_time
#    downsampled_scan.range_min = msg.range_min
#    downsampled_scan.range_max = msg.range_max
#    downsampled_scan.ranges = downsampled_ranges
#    downsampled_scan.intensities = downsampled_intensities
#
#    # Publish the downsampled scan
#    pub.publish(downsampled_scan)
def callback(msg):
    # Downsample the scan, for example, take every 10th reading
    downsampled_ranges = msg.ranges[::2]
    downsampled_intensities = msg.intensities[::2]

    # Create a new LaserScan message
    downsampled_scan = LaserScan()
    downsampled_scan.header = msg.header
    downsampled_scan.header.stamp = rospy.Time.now()
    downsampled_scan.header.frame_id = 'laser_frame'
    downsampled_scan.angle_min = msg.angle_min
    downsampled_scan.angle_max = msg.angle_max
    downsampled_scan.angle_increment = msg.angle_increment * 2
    downsampled_scan.time_increment = msg.time_increment 
    downsampled_scan.scan_time = msg.scan_time
    downsampled_scan.range_min = msg.range_min
    downsampled_scan.range_max = msg.range_max
    downsampled_scan.ranges = downsampled_ranges
    downsampled_scan.intensities = downsampled_intensities

    # Publish the downsampled scan
    pub.publish(downsampled_scan)
def publish_transform():
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    # Your transform configuration here
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)
rospy.init_node('downsample_scan')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/downsampled_scan', LaserScan, queue_size=1)


rospy.spin()