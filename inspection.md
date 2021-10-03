# CRAZY TURTLE
Demonstration package for ME495.
This README is intentionally vague.
Figuring out how this package works and filling in the details is part of the
exercise. Replace the the blanks marked with `${ITEM}` with your answer.
Unless otherwise specified, list the command and all arguments that you passed to it.

## Setup Instructions
1. Compile the workspace by executing `catkin_make`
2. Initialize the ROS environment (i.e., set the necessary ROS environment variables) by executing `source /opt/ros/noetic/setup.bash`
3. Make sure no other ROS nodes are running prior to starting. 
3. Run the launchfile `/ws/src/crazy_turtle/go_crazy_turtle.launch` by executing `roslaunch crazy_turtle go_crazy_turtle.launch`
4. When running you can see a visual depiction of the ROS graph using the `rqt_graph` command.
   The ROS graph, including all topics and node labels, looks like:
   ![${The ROS Graph}](${path_to_image_here_include_image_in_your_repository})

## Runtime Information
The `launchfile` from above should be running at all times when executing these commands.
If the nodes launched from the `launchfile` are not running, you will get incorrect results.

5. Use the ROS command `rosnode list` to list all the nodes that are running.
   The output of the command looks like
   ```
   /mover
   /rosout
   /roving_turtle

   ```
6. Use the ROS command `rostopic list` to list the topics
   The output of the command looks like
   ```
   /rosout
   /rosout_agg
   /turtle1/cmd_vel
   /turtle1/color_sensor
   /turtle1/pose
   ```

7. Use the ROS command `rostopic hz /turtle1/cmd_vel` to verify that the frequency of
   the `/turtle1/cmd_vel` topic is `120.004 Hz`

8. Use the ROS command `rosservice list` to list the services.
   The output of the command looks like
   ```
   /clear
   /kill
   /mover/get_loggers
   /mover/set_logger_level
   /reset
   /rosout/get_loggers
   /rosout/set_logger_level
   /rostopic_22535_1632685185530/get_loggers
   /rostopic_22535_1632685185530/set_logger_level
   /roving_turtle/get_loggers
   /roving_turtle/set_logger_level
   /spawn
   /switch
   /turtle1/set_pen
   /turtle1/teleport_absolute
   /turtle1/teleport_relative

   ```
9. Use the ROS command `rosservice info /switch` to view information about the `/switch` service.
   The type of the `/switch` service is `crazy_turtle/Switch` and it is offered by
   the `/mover` node.

10. Use the ROS command `rosparam list` to list the parameters that are loaded
    into the parameter server.
    The output of the command looks like
    ```
    /mover/velocity
    /rosdistro
    /roslaunch/uris/host_bhagyesh_inspiron_5570__46101
    /rosversion
    /roving_turtle/background_b
    /roving_turtle/background_g
    /roving_turtle/background_r
    /run_id

    ```

## Package and Dependencies
11. Use the ROS command `${command and args}` to list the types of services defined by `crazy_turtle`
    The output of the command looks like
    ```
    ${list service types here}
    ```
12. Use the ROS command `rospack depends1 crazy_turtle` to list the immediate (direct) dependencies of `crazy_turtle`
   The output of the command looks like
   ```
   rospy
   message_runtime
   turtlesim

   ```
## Live Interaction
13. Use the ROS command `rosservice call /switch "mixer: {x: 2.0, y: 1.0, theta: 0.8, linear_velocity: 0.5, angular_velocity: 1.5}"` to call the `/switch` service.
    The command returns `x: 3.0 y: 0.5` and the turtle `The turtle spawns to a new position at x = 3.0 and y = 0.5 and moves randomly`.
    (Hint: use `rossrv info` on the type of the `/switch` service to see the parameters.
     To test the behavior, look at the code or try calling with `x = 1`, `y = 1`, once with `linear_velocity = 0` and `angular_velocity = 0` and once with these at different nonzero values.)
14. What is the value of the `/mover/velocity` parameter? `4.5`
15. What happens to the turtle's motion if you change `/mover/velocity` to 10 while the turtlesim and mover node are running? same
16. Use the ROS command `rosnode kill /mover` to kill the `/mover` node.
17. Use the ROS command `${command and args}` to start the `/mover` node. Be sure to
    remap `cmd_vel` to `/turtle1/cmd_vel`.
18. What happened to the turtle's velocity after relaunching `mover`? `${faster | slower | same}`
