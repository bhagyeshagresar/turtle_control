import rospy
from turtlesim.srv import TeleportRelative, TeleportAbsolute, SetPen
from std_srvs.srv import Empty, EmptyResponse
import math
import yaml


def draw_waypoints():
    restart_turtlesim = rospy.ServiceProxy('restart', std_srvs.srv.Empty)
    restart_turtlesim()
    waypoints = rospy.get_param("/waypoints")
    for x in waypoints:
        teleport_turtle_abs= rospy.ServiceProxy('turtle1/teleport_absolute', turtlesim.srv.TeleportAbsolute)
        turtle_set_pen = rospy.ServiceProxy('turtle1/set_key', turtlesim.srv.SetPen)
        turtle_set_pen(255, 255, 0, 5, on)
        teleport_turtle(x)
        turtle_set_pen(255, 255, 0, 5, off)
        teleport_turtle_rel = rospy.ServiceProxy('turtle1/teleport_relative', turtlesim.srv.TeleportRelative)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(-1.0, 0)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(0, 90)
        teleport_turtle_rel(0.5, 0)
        teleport_turtle_rel(-1.0, 0)
        teleport_turtle_rel(0.5, 0)
    
    return EmptyResponse()



    

def server_function():
    rospy.init_node('server')
    s = rospy.Service('draw', Empty, draw_waypoints)

if __name__ == "__main__":
    server_function()