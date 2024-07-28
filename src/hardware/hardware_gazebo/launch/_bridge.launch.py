import clingwrap as cw


def generate_launch_description():
    l = cw.LaunchBuilder()

    bridge_topics = [
        "/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock",
        "/hardware/sensors/livox_front/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked",
        "/hardware/sensors/camera_front/image_raw@sensor_msgs/msg/Image[ignition.msgs.Image",
        "/hardware/sensors/camera_front/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo",
    ]

    with l.namespace("simulation"):
        l.node(
            "ros_gz_bridge",
            "parameter_bridge",
            name="gz_bridge",
            arguments=bridge_topics,
        )

    return l
