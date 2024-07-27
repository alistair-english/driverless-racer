import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    desc_path = l.declare_arg(
        "desc_path", default_value=cw.find_file("hardware_core", "urdf", "racecar.urdf.xacro")
    )

    l.include_launch_py("hardware_core", "_robot_description.launch.py", {"robot_description_path": desc_path})

    with l.namespace("hardware"):
        l.node("joint_state_publisher_gui")

    return l
