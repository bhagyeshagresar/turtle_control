#!/usr/bin/env python
"""
Publishes velocity messages to move the turtle in the direction of the waypoints.

Publisher:
topic - turtle_cmd  message type - turtle_control/TurtleVelocity

Subscriber:
topic - /turtle1/pose message type - turtlesim/Pose

Server:
topic - /restart message type - turtle_control/Start




"""

import rospy
from turtlesim.msg import Pose
from turtlesim.srv import TeleportRelative, TeleportAbsolute, SetPen
from std_msgs.msg import String
from turtle_control.msg import TurtleVelocity
from geometry_msgs.msg import Twist
from turtle_control.srv import Start
from std_srvs.srv import Empty, EmptyResponse
import math
from math import atan2,sqrt
import json


def call_back(data):   
    """
    Collects the waypoints, calculates the orientation of the turtle with respect to the waypoints and publishes velocity messages on turtle_cmd

    Args:
        data

    Returns:
        None

    """
    with open("counter.json",'r') as json_file:
        counter_dict = json.load(json_file)
    print("json dict", counter_dict)
    counter = int(counter_dict["counter"])
    if counter < len(waypoints):

        
    
        turtle_pos = data

        angle_list = []

        vel_pub = rospy.Publisher('turtle_cmd', TurtleVelocity, queue_size = 20)

        turtle_velocities= TurtleVelocity()
        turtle_velocities.linear = 1.5
        turtle_velocities.angular = 1.5
        
        current_pose = [data.x, data.y]
        print("current_pose", current_pose)
        goal = waypoints[counter]
        dist1 = math.dist(goal, current_pose)
        diff_1_x = goal[0] - current_pose[0]
        diff_1_y = goal[1] - current_pose[1]
        first_angle = atan2(diff_1_y, diff_1_x) 

        print("data.theta",data.theta)
        print("first_angle", first_angle)

        angle_new = data.theta
        angle_diff = abs(first_angle - angle_new)
         
        print("angle_diff", angle_diff)
        if (angle_diff > 0.5): 
            turtle_velocities.linear = 0        
            vel_pub.publish(turtle_velocities)
            print("inside angle diff rotation")
            
                
        else:
            print("inside angle diff stop")
            turtle_velocities.angular = 0
            print("dist1", dist1)
            if (dist1 > 0.05):
                print("inside distance moves")
                vel_pub.publish(turtle_velocities) 
                print("counter inside dist move", counter)
                print("goal inside dist move", goal)
                
            else:
                print("inside distance stops")
                
                turtle_velocities.linear = 0
                
                vel_pub.publish(turtle_velocities)
                
                counter += 1
                if counter < len(waypoints):
                    goal = waypoints[counter]
                elif counter == len(waypoints):
                    counter = 0
                    goal = waypoints[0]
                with open("counter.json", 'w') as json_file:
                    json.dump({"counter":counter}, json_file)
                
                rospy.loginfo("waypoint reached --------------")
           
    return 0
            
    
        
    
def restart_fn(req):

    """
    collects the waypoints, resets the turtle, draws the waypoints

    Args:
    req

    Returns:
    
    distance - the distance covered by the turtle by moving from the starting position to the final waypoint

    """
    init_x = req.x
    init_y = req.y
    
    init = [init_x, init_y]
    
    
   
    reset_service = rospy.ServiceProxy('reset', Empty)
    reset_service()
        
    draw_service = rospy.ServiceProxy('draw', Empty)
    draw_service()


    turtle_set_pen_1 = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    turtle_set_pen_1(255, 255, 0, 5, True)
    
    teleport_turtle_abs_1= rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
    teleport_turtle_abs_1(1, 1, 30)

    
    angle_new = 0
    angle_threshold = 0.5
    
    rospy.Subscriber('/turtle1/pose', Pose, call_back)
   
    print("counter- final", counter)
    distance = 0
    distance1 = math.dist(waypoints[0], init)
    distance2 = math.dist(waypoints[1], waypoints[0])
    distance3 = math.dist(waypoints[2], waypoints[1])
    distance4 = math.dist(waypoints[3], waypoints[2])


    distance = distance1+distance2+distance3+distance4
    print("distance covered: ")
    print(distance)

        
    return distance



def follower():
    """
    This function initalizes the follower node. 
    
    The node will provide restart service to reset and draw the waypoints by calling the draw service


    """
    rospy.init_node('follower', anonymous = True)
    
    
    rospy.Service('restart', Start, restart_fn)


if __name__ == "__main__":
    PI = 3.14
    i = 0
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    init_x = 0
    dish_tresh = 0.05
    init_y = 0
    waypoints = rospy.get_param("/waypoint")
    with open("counter.json", 'w') as json_file:
        json.dump({"counter":0}, json_file)
    
    follower()
    rospy.spin()
    

