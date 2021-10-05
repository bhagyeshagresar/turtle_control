#!/usr/bin/env python
"""
Converts messages of type turtle_control/TurtleVelocity to geometry_msgs/Twist

Publisher:
    topic :'turtle1/cmd_vel'
Subscriber: 
    topic :'turtle_cmd'

"""

import rospy
from turtlesim.msg import Pose
from std_msgs.msg import String
from turtle_control.msg import TurtleVelocity
from geometry_msgs.msg import Twist


def callback(data):
"""
callback function publishes 3D velocities of type Twist

"""
    rospy.loginfo("Received 2D velocities")
    velocities_3D = Twist()
    velocities_3D.linear.x = data.linear
    velocities_3D.angular.z = data.angular
    pub.publish(velocities_3D)




def translate():
"""
Initialize the translate node.
In this the node subscribes to the turtle_cmd topic

"""
    rospy.init_node('translate', anonymous = True)
    sub = rospy.Subscriber('turtle_cmd', TurtleVelocity, callback)
    
    
    rospy.spin()
    


if __name__ == "__main__":
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)
    translate()
