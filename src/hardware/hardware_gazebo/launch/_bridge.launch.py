import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    bridge_topics = [
        "/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock",
    ]

    with l.namespace("simulation"):
        l.node(
            "ros_gz_bridge",
            "parameter_bridge",
            name="gz_bridge",
            arguments=bridge_topics,
        )

    return l