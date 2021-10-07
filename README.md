# ME495 - Homework-1

# Name: Bhagyesh Agresar

# turtle_control Package
The package makes the turtle in the `turtlesim` package follow different waypoints and move in a loop through these waypoints. The package contains the `setup`, `translate` and
 the `follow` node. The `setup` node draws the waypoints in the 2D space. `translate` node is used to convert messages between `geometry_msgs/Twist` and `turtle_control/TurtleVelocity`.
 The `follow` node causes the turtle to follow the waypoints drawn using the `setup` node
 
 
 # Instructions to Setup the turtle_control Package
 
 Clone the package inside the `src` directory of the `catkin workspace`
 
 Build the package using `catkin_make`
 
 Source your environment using `source devel/setup.bash`
 
 Run the `turtlesim` node using `rosrun turtlesim turtlesim_node` and make sure `roscore` is running
 
 Run the launchfile `run_waypoints.launch` using `roslaunch turtle_control run_waypoints.launch`
 
 Run the service `/restart` and specify the starting position of the turtle using `rosservice call /restart "x: 5.0 y: 0.0"`
 
 
 # Video Demonstartion of the Turtle Following the waypoints
 
 ![Turtle](https://user-images.githubusercontent.com/82998852/136298585-06a78e1c-9f4d-48cf-ac94-6eb0fcd69bbc.gif)
