from launch import substitutions as sub

import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    robot_description_path = l.declare_arg("robot_description_path")

    robot_description_urdf = sub.Command(["xacro ", robot_description_path])

    with l.namespace("hardware"):
        l.node(
            "robot_state_publisher",
            parameters={
                "robot_description": cw.as_str_param(robot_description_urdf),
            },
        )

    return l
