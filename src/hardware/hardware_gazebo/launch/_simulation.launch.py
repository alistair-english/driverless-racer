from launch import substitutions as sub

import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    robot_description_path = l.declare_arg("robot_description_path")

    gz_robot_description_urdf = sub.Command(["xacro ", robot_description_path])

    world = cw.find_file("hardware_gazebo", "worlds", "sonoma_raceway.sdf")

    l.include_launch_py("ros_gz_sim", "gz_sim.launch.py", {"gz_args": [" -r ", world]})

    # `ros2 run ros_gz_sim create --help` to see all arguments
    l.node("ros_gz_sim", "create", arguments=["-string", gz_robot_description_urdf, "-x", "277.0", "-y", "-136.0", "-z", "3.3", "-Y", "-0.62"])

    return l
