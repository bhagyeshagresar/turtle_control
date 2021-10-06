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

        # angle_new = args[1]
        # angle_threshold = args[2]
        # global goal
        # goal = args[1]
        # print("counter", counter)
        # print("angle thresh", angle_threshold)
        # print(data["Pose"])
        # print(args[0])
        # print("---")
        # print(args[1])
        # print(data)
        # goal = args[0]
    
        turtle_pos = data

        angle_list = []

        vel_pub = rospy.Publisher('turtle_cmd', TurtleVelocity, queue_size = 20)

        turtle_velocities= TurtleVelocity()
        turtle_velocities.linear = 0.5
        turtle_velocities.angular = 0.5
        # rospy.loginfo(turtle_velocities)

        # linear_speed = 0.5
        # angular_speed = 0.5
        #initial_angle = turtle_pos.theta #converting the initial angle of turtle from degrees to radians

        #first angle represents the angle made by the initial position of the turtle with respect to the first waypoint 

        # angle_list.append(data.theta)
        # for indx,value in enumerate(waypoints):
        # print(indx)
        # print("---")
        # print(value)

        # rospy.loginfo(first_angle)
        # rospy.loginfo(initial_angle)
        
        # For reaching first waypoint:
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
        # else:
        #     angle_diff = first_angle - angle_list[] 
        print("angle_diff", angle_diff)
        if (angle_diff > 0.5): 
            turtle_velocities.linear = 0        #linear velocity = 0 and angular velocity = 0.5
            vel_pub.publish(turtle_velocities)
            print("inside angle diff rotation")
            # rospy.Subscriber('/turtle1/pose', Pose, callback, (counter, angle_new, angle_threshold))  #Rotate until it finds the first waypoint
                
        else:
            print("inside angle diff stop")
            turtle_velocities.angular = 0
            print("dist1", dist1)
            if (dist1 > 0.05):
                print("inside distance moves")
                vel_pub.publish(turtle_velocities) 
                print("counter inside dist move", counter)
                print("goal inside dist move", goal)
                # if counter > 0:
                    
                #rospy.Subscriber('/turtle1/pose', Pose, callback, (counter, goal)) #Move towards the waypoint
            else:
                print("inside distance stops")
                # rospy.loginfo()
                # angle_threshold = 0.5
                turtle_velocities.linear = 0
                # angle_new = first_angle
                vel_pub.publish(turtle_velocities)
                
                counter += 1
                if counter < len(waypoints):
                    goal = waypoints[counter]
                elif counter == len(waypoints):
                    counter = 0
                    goal = waypoints[0]
                with open("counter.json", 'w') as json_file:
                    json.dump({"counter":counter}, json_file)
                # if counter == len(waypoints)-1:
                #     return 0
                # counter = 0
                # counter += 1
                rospy.loginfo("waypoint reached --------------")
            # file.write(counter)
            # rospy.Publisher(counter)
            # callback.publish(counter)
            # rospy.Subscriber('/turtle1/pose', Pose, callback, (counter, goal))
            # turtle_velocities.linear = 0.5
            # turtle_velocities.angular = 0.5
            # goal = waypoints[1]
            # print("goal")
            # dist2 = math.dist(goal, current_pose)
            # diff_2_x = goal[0] - current_pose[0]
            # diff_2_y = goal[1] - current_pose[1]
            # second_angle = atan2(diff_2_y, diff_2_x) 

            # # if counter == 0:
            # angle_diff = second_angle - data.theta
            # print("angle_diff",angle_diff)
            # # else:
            # #     angle_diff = first_angle - angle_list[] 

            # if (angle_diff > 5): 
            #     turtle_velocities.linear = 0        #linear velocity = 0 and angular velocity = 0.5
            #     vel_pub.publish(turtle_velocities)  #Rotate until it finds the first waypoint
                    
            # else:
            #     turtle_velocities.angular = 0
            #     if (dist2 > 0.05):
            #         vel_pub.publish(turtle_velocities)
            #     else:
            #         counter += 1
            #         turtle_velocities.linear = 0
            #         vel_pub.publish(turtle_velocities)
            #         print(" second wavepoint reached --------------")

        # rospy.loginfo(turtle_velocities.angular)
    return 0
            
    # #For reaching second waypoint:
    # #current_pose = [data.x, data.y]
    # goal = waypoints[1]
    # dist2 = math.dist(goal, current_pose)
    # diff_2_x = waypoints[1][0] - current_pose[0]
    # diff_2_y = waypoints[1][1] - current_pose[1]
    # second_angle = atan2(diff_2_y, diff_2_x) 
    

    # if (second_angle - first_angle > 0.5):
    #     turtle_velocities.angular = 0.5
    #     turtle_velocities.linear = 0        #linear velocity = 0 and angular velocity = 0.5
    #     vel_pub.publish(turtle_velocities)  #Rotate until it finds the first waypoint
             
    # else:
    #     turtle_velocities.angular = 0
    #     if (dist2 > 0.05):
    #         vel_pub.publish(turtle_velocities)  #Move towards the waypoint
    #     else:
    #         turtle_velocities.linear = 0
    #         turtle_velocities.angular = 0
    #         vel_pub.publish(turtle_velocities)



    # #For reaching third waypoint:

    # #current_pose = [data.x, data.y]
    # goal = waypoints[2]
    # dist3 = math.dist(goal, current_pose)
    # diff_3_x = waypoints[2][0] - current_pose[0]
    # diff_3_y = waypoints[2][1] - current_pose[1]
    # third_angle = atan2(diff_3_y, diff_3_x) 
    

    # if (third_angle - second_angle > 0.5): #a < x < b 
    #     turtle_velocities.angular = 0.5
    #     turtle_velocities.linear = 0        
    #     vel_pub.publish(turtle_velocities)  #Rotate until it finds the first waypoint
             
    # else:
    #     turtle_velocities.angular = 0
    #     if (dist3 > 0.05):
    #         vel_pub.publish(turtle_velocities)  #Move towards the waypoint
    #     else:
    #         turtle_velocities.linear = 0
    #         vel_pub.publish(turtle_velocities)


    # #For reaching fourth waypoint:

    # #current_pose = [data.x, data.y]
    # goal = waypoints[3]
    # dist4 = math.dist(goal, current_pose)
    # diff_4_x = waypoints[3][0] - current_pose[0]
    # diff_4_y = waypoints[3][1] - current_pose[1]
    # fourth_angle = atan2(diff_4_y, diff_4_x) 
    

    # if (fourth_angle - third_angle > 0.5): #a < x < b 
    #     turtle_velocities.angular = 0.5
    #     turtle_velocities.linear = 0        
    #     vel_pub.publish(turtle_velocities)  #Rotate until it finds the first waypoint
             
    # else:
    #     turtle_velocities.angular = 0
    #     if (dist4 > 0.05):
    #         vel_pub.publish(turtle_velocities)  #Move towards the waypoint
    #     else:
    #         turtle_velocities.linear = 0
    #         vel_pub.publish(turtle_velocities)




            
        # Get to the first waypoint
        # Line up the turlte to the waypoint
        # GOOD
        # If not at point
        # if (dist > dist_thresh):
        # Move toward waypoint
        # vel_pub.publish(vel)
        
    
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
    #rospy.Subscriber('/turtle1/pose', Pose, callback)
    #turtle_pos = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    
   
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
    # counter = 0
    # goal = waypoints[0]
    # rospy.Subscriber('/turtle1/pose', Pose, callback, (counter, angle_new, angle_threshold))
    rospy.Subscriber('/turtle1/pose', Pose, call_back)
    # counter = callback(Pose, counter)
    print("counter- final", counter)
    distance = 0
    # distance1 = math.dist(waypoints[0], init)
    # distance2 = math.dist(waypoints[1], waypoints[0])
    # distance3 = math.dist(waypoints[2], waypoints[1])
    # distance4 = math.dist(waypoints[3], waypoints[2])


    # distance = distance1+distance2+distance3+distance4

        
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
    # angle_list = []
    # print("counter", counter)
    # angle_list.append("NA")
    follower()
    rospy.spin()
    # waypoints = rospy.get_param("/waypoint")
    # for i,j in enumerate(waypoints):
    #     print(i)
    #     print("---")
    #     print(j)

