import clingwrap as cw


def spawn_controller(l: cw.LaunchBuilder, controller_name: str) -> cw.LaunchBuilder:
    l.node(
        "controller_manager",
        "spawner",
        arguments=[controller_name, "--controller-manager-timeout", "100"],
        ros_arguments=["--log-level", "INFO"],
    )

    return l


def generate_launch_description():
    l = cw.LaunchBuilder()

    with l.namespace("hardware"):
        l = spawn_controller(l, "joint_state_broadcaster")
        l = spawn_controller(l, "controller_ackermann")

    return l
