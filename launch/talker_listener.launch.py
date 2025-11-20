from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_topic_demo',
            executable='talker',
            name='talker'
        ),
        Node(
            package='py_topic_demo',
            executable='listener',
            name='listener'
        ),
    ])
