#!/usr/bin/env python


import rospy
from turtlesim.msg import Pose
from turtlesim.srv import TeleportRelative, TeleportAbsolute, SetPen
from std_msgs.msg import String
from turtle_control.msg import TurtleVelocity
from geometry_msgs.msg import Twist
from turtle_control.srv import Start
from std_srvs.srv import Empty, EmptyResponse
import math

#def callback_1(data):
#    return(Twist(Vector3(linear.x, linear.y, angular.z)),Vector3(linear.x, linear.y, angular.z)))




def callback(data):
    turtle_pos = Pose()
    return(turtle_pos(data.x), turtle_pos(data.y), turtle_pos(data.theta))
    


def restart_fn(req):
    
    
    waypoints = rospy.get_param("/waypoint")
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    #turtle_pos = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    
    current_pos = Pose()
    if (current_pos.x > 11 or current_pos.y > 11 or current_pos.x < 0 or current_pos.y < 0):
        rospy.loginfo("None")
    else:
        draw_service = rospy.ServiceProxy('draw', Empty)
        draw_service()
        reset_service = rospy.ServiceProxy('reset', Empty)
        reset_service()
        first_pos = Pose()
        
        dist1 = sqrt((waypoints[0][0] - first_pos.linear.x)**2 - (waypoints[0][1] - first_pos.linear.y)**2)
        dist2 = sqrt((waypoints[1][0] - waypoints[0][0])**2 - (waypoints[1][1] - first_pos.linear.y)**2)
        dist3 = sqrt((waypoints[1][0] - waypoints[0][0])**2 - (waypoints[1][1] - first_pos.linear.y)**2)
        dist4 = sqrt((waypoints[1][0] - waypoints[0][0])**2 - (waypoints[1][1] - first_pos.linear.y)**2)
        
        pub = rospy.Publisher('turtle/cmd', TurtleVelocity, queue_size = 10)











def follower():
    #rospy.get_param("/waypoint")
    rospy.init_node('follower', anonymous = True)
    #rospy.Subscriber('/turtle1/pose', Pose, callback)
    
    
    rospy.Service('restart', Start, restart_fn)





if __name__ == "__main__":
    follower()
    rospy.spin()