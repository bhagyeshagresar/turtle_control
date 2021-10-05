#!/usr/bin/env python
"""
setup node implements a draw service to draw all the waypoints.

service topic : draw, service type : std_srvs/Empty

"""

"""
    This function calls the 'reset', 'turtle1/teleport_absolute', 'turtle1/teleport_absolute', 'turtle1/teleport_relative' and the 'turtle1/set_pen' services
    to draw the waypoints
    
        Args:
        req

    Returns:
    EmptyResponse()
    """

import rospy
from turtlesim.srv import TeleportRelative, TeleportAbsolute, SetPen
from std_srvs.srv import Empty, EmptyResponse
import math
import yaml


def draw_waypoints(req):
    """
    This function calls the 'reset', 'turtle1/teleport_absolute', 'turtle1/teleport_absolute', 'turtle1/teleport_relative' and the 'turtle1/set_pen' services
    to draw the waypoints
    
        Args:
        req

        Returns:
        EmptyResponse()
    """
    
    restart_turtlesim = rospy.ServiceProxy('reset', Empty)
    restart_turtlesim()
    waypoints = rospy.get_param("/waypoint")
    for x in waypoints:
        teleport_turtle_abs= rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
        turtle_set_pen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
        turtle_set_pen(255, 255, 0, 5, True)
        teleport_turtle_abs(x[0], x[1], 30)
        turtle_set_pen(255, 255, 0, 5, False)
        teleport_turtle_rel = rospy.ServiceProxy('turtle1/teleport_relative',TeleportRelative)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(-1.0, 0)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(0, 90)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(-1.0, 0)
        teleport_turtle_rel(0.5, 0)
        turtle_set_pen(255, 255, 0, 5, True)
        teleport_turtle_abs(x[0], x[1], 30)

    
    return EmptyResponse()



    

def server_function():
    """
    initializes the 'server' node
    Declares the service 'draw'

    """   

    rospy.init_node('server')
    s = rospy.Service('draw', Empty, draw_waypoints)

if __name__ == "__main__":
    server_function()
    rospy.spin()