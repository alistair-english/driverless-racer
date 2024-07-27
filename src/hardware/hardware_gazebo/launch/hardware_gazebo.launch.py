import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    desc_path = cw.find_file("hardware_gazebo", "urdf", "racecar.urdf.xacro")

    l.include_launch_py("hardware_core", "_robot_description.launch.py", {"robot_description_path": desc_path})

    l.include_launch_py("hardware_gazebo", "_simulation.launch.py", {"robot_description_path": desc_path})
    l.include_launch_py("hardware_gazebo", "_bridge.launch.py")
    l.include_launch_py("hardware_gazebo", "_controllers.launch.py")

    return l