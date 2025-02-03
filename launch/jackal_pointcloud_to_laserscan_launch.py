from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='namespace', default_value='',
            description='Namespace for sample topics'
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in',  'ouster/points'),
                        ('scan', 'scan'),
                        ('/tf_static', 'tf_static'),
                        ('/tf', 'tf')],
            parameters=[{
                'min_height': -0.5,
                'max_height': 0.5,
                'angle_min': -3.14,  # -M_PI/2
                'angle_max': 3.14,  # M_PI/2
                'angle_increment': 0.00017455,  # M_PI/180.0*0.01 where 0.01 is ouster resolution
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 36.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan',
            namespace=LaunchConfiguration('namespace'),
            #arguments=['--ros-args', '--log-level', 'DEBUG']
        )
    ])

