import os

from launch import LaunchDescription
from launch.actions import RegisterEventHandler, DeclareLaunchArgument, TimerAction
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch.conditions import IfCondition

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import OpaqueFunction
from launch_ros.parameter_descriptions import ParameterValue


def print_launch_configuration_value(context, *args, **kwargs):
    gz_value = LaunchConfiguration('gz').perform(context)
    print(f'LaunchConfiguration gz: {gz_value}')
    return gz_value

def generate_launch_description():
    ARGUMENTS = [
        DeclareLaunchArgument('name', default_value='dsr01', description='NAME_SPACE'),
        DeclareLaunchArgument('host', default_value='127.0.0.1', description='ROBOT_IP'),
        DeclareLaunchArgument('port', default_value='12345', description='ROBOT_PORT'),
        DeclareLaunchArgument('mode', default_value='virtual', description='OPERATION MODE'),
        DeclareLaunchArgument('model', default_value='m1013', description='ROBOT_MODEL'),
        DeclareLaunchArgument('color', default_value='white', description='ROBOT_COLOR'),
        DeclareLaunchArgument('gripper', default_value='none', description='ROBOT_GRIPPER'),
        DeclareLaunchArgument('gui', default_value='false', description='Start RViz2'),
        DeclareLaunchArgument('gz', default_value='false', description='USE GAZEBO SIM'),
    ]
    xacro_path = os.path.join(get_package_share_directory('dsr_description2'), 'xacro')

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("dsr_description2"),
                    "xacro",
                    LaunchConfiguration('model'),
                ]
            ),
            ".urdf.xacro",
            " color:=", LaunchConfiguration('color'),
            " gripper:=", LaunchConfiguration('gripper'),
        ]
    )

    robot_description = {
        'robot_description': ParameterValue(robot_description_content, value_type=str)
    }

    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("dsr_controller2"),
            "config",
            "dsr_controller2.yaml",
        ]
    )
    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("dsr_description2"), "rviz", "default.rviz"]
    )

    connection_node = Node(
        package="dsr_bringup2",
        executable="connection",
        namespace=LaunchConfiguration('name'),
        parameters=[
            {"name": LaunchConfiguration('name')},
            {"rate": 100},
            {"standby": 5000},
            {"command": True},
            {"host": LaunchConfiguration('host')},
            {"port": LaunchConfiguration('port')},
            {"mode": LaunchConfiguration('mode')},
            {"model": LaunchConfiguration('model')},
            {"gripper": LaunchConfiguration('gripper')},
            {"mobile": "none"},
        ],
        output="screen",
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        namespace=LaunchConfiguration('name'),
        parameters=[robot_description, robot_controllers],
        output="both",
    )

    robot_state_pub_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=LaunchConfiguration('name'),
        output='both',
        parameters=[{
            'robot_description': ParameterValue(robot_description_content, value_type=str)
        }]
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        namespace=LaunchConfiguration('name'),
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        namespace=LaunchConfiguration('name'),
        executable="spawner",
        arguments=["joint_state_broadcaster", "-c", "controller_manager"],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        namespace=LaunchConfiguration('name'),
        executable="spawner",
        arguments=["dsr_controller2", "-c", "controller_manager"],
    )

    delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=robot_controller_spawner,
            on_exit=[rviz_node],
        )
    )

    nodes = [
        connection_node,
        control_node,
        robot_state_pub_node,
        robot_controller_spawner,
        joint_state_broadcaster_spawner,
        delay_rviz_after_joint_state_broadcaster_spawner,
    ]

    return LaunchDescription(ARGUMENTS + nodes)
