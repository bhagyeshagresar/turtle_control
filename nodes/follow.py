#!/usr/bin/env python


import rospy
from turtlesim.msg import Pose
from turtlesim.srv import TeleportRelative, TeleportAbsolute, SetPen
from std_msgs.msg import String
from turtle_control.msg import TurtleVelocity
from geometry_msgs.msg import Twist
from turtle_control.srv import Start
from std_srvs.srv import Empty, EmptyResponse
from math import atan2,sqrt

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
        reset_service = rospy.ServiceProxy('reset', Empty)
        reset_service()
        
        draw_service = rospy.ServiceProxy('draw', Empty)
        draw_service()
        
        initial_pos = Pose() # x, y, theta
        
        dist1 = sqrt((waypoints[0][0] - first_pos.linear.x)**2 - (waypoints[0][1] - first_pos.linear.y)**2)
        dist2 = sqrt((waypoints[1][0] - waypoints[0][0])**2 - (waypoints[1][1] - waypoints[0][1])**2)
        dist3 = sqrt((waypoints[2][0] - waypoints[1][0])**2 - (waypoints[2][1] - waypoints[1][1])**2)
        dist4 = sqrt((waypoints[3][0] - waypoints[2][0])**2 - (waypoints[3][1] - waypoints[2][1])**2)

        waypoint_1 = Pose()
        waypoint_2 = Pose()
        waypoint_3 = Pose()
        waypoint_4 = Pose()

        waypoint_1.x = waypoints[0][0]
        waypoint_1.y = waypoints[0][1]
        
        waypoint_2.x = waypoints[1][0]
        waypoint_2.y = waypoints[1][1]
        
        waypoint_3.x = waypoints[2][0]
        waypoint_3.y = waypoints[2][1]
        
        waypoint_4.x = waypoints[3][0]
        waypoint_4.y = waypoints[3][1]


        vel_pub = rospy.Publisher('turtle/cmd', TurtleVelocity, queue_size = 10)

        turtle_velocities= TurtleVelocity()
        turtle_velocities.linear = 5.0
        turtle_velocities.angular = 5.0

        diff_1_x = waypoint_1.x - initial_pos.x
        diff_1_y = waypoint_1.y - initial_pos.y
        
        diff_2_x = waypoint_2.x - waypoint_1.x
        diff_2_y = waypoint_2.y - waypoint_1.y

        diff_3_x = waypoint_3.x - waypoint_2.x
        diff_3_y = waypoint_3.y - waypoint_2.y

        diff_4_x = waypoint_4.x - waypoint_2.x
        diff_4_y = waypoint_4.y - waypoint_3.y

        initial_angle = ((initial_pos.theta)*2*PI)/360 #converting the initial angle of turtle from degrees to radians

        #first angle represents the angle made by the initial position of the turtle with respect to the first waypoint 

        first_angle = atan2(diff_1_y, diff_1_x)    
        second_angle = atan2(diff_2_y, diff_2_x)
        third_angle = atan2(diff_3_y, diff_3_x)
        fourth_angle = atan2(diff_4_y, diff_4_x)

        current_distance = 0
        t0 = rospy.Time.now().to_sec()


        while (current_distance < (dist1+dist2+dist3+dist4)):
            
            while(current_distance < dist1):
                if (initial_angle == first_angle):
                    vel_pub.publish(turtle_velocities.linear)
                    t1 = rospy.Time.now().to_sec()
                    current_distance = turtle_velocities.linear * (t1 - t0)
                else:
                    vel_pub.publish(turtle_velocities.angular)
        

            while(current_distance < dist2):
                if (first_angle == second_angle):
                    vel_pub.publish(turtle_velocities.linear)
                    t2 = rospy.Time.now().to_sec()
                    current_distance = turtle_velocities.linear * (t2 - t1)
                else:
                    vel_pub.publish(turtle_velocities.angular)
            

            while(current_distance < dist3):
                if (second_angle == third_angle):
                    vel_pub.publish(turtle_velocities.linear)
                    t3 = rospy.Time.now().to_sec()
                    current_distance = turtle_velocities.linear * (t3 - t2)
                else:
                    vel_pub.publish(turtle_velocities.angular)


            while(current_distance < dist4):
                if (third_angle == fourth_angle):
                    vel_pub.publish(turtle_velocities.linear)
                    t4 = rospy.Time.now().to_sec()
                    current_distance = turtle_velocities.linear * (t4 - t3)
                else:
                    vel_pub.publish(turtle_velocities.angular)


        









def follower():
    #rospy.get_param("/waypoint")
    rospy.init_node('follower', anonymous = True)
    #rospy.Subscriber('/turtle1/pose', Pose, callback)
    
    
    rospy.Service('restart', Start, restart_fn)





if __name__ == "__main__":
    follower()
    rospy.spin()