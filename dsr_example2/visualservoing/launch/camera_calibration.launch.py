# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# 
#  camera_calibration.launch.py
#  Modified by: Chemin Ahn (chemx3937@gmail.com)
#  
#  Copyright (c) 2024 Doosan Robotics
#  Use of this source code is governed by the BSD, see LICENSE
# 

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

WORKSPACENAME = 'doosan_ws'

def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            #'gz_args': '-r sensors_demo.sdf'
            'gz_args': '-r /workspace/doosan_ws/src/doosan-robot2/dsr_example2/visualservoing/description/camera_calibration.sdf'


        }.items(),
    )


    # RQt
    rqt = Node(
        package='rqt_image_view',
        executable='rqt_image_view',
        arguments=[LaunchConfiguration('image_topic')],
        condition=IfCondition(LaunchConfiguration('rqt'))
    )

    # ######################################################################
    # # RViz
    # pkg_ros_gz_sim_demos = get_package_share_directory('ros_gz_sim_demos')

    # rviz = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     arguments=[
    #         '-d', os.path.join(pkg_ros_gz_sim_demos, 'rviz', 'rgbd_camera_bridge.rviz')
    #     ],
    #     condition=IfCondition(LaunchConfiguration('rviz'))
    # )
    # ######################################################################

    bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        arguments=['rgbd_camera/image', 'rgbd_camera/depth_image'],     #rgbd키메라만 사용
        output='screen'
    )

    return LaunchDescription([
        gz_sim,
        DeclareLaunchArgument('rqt', default_value='true',
                              description='Open RQt.'),

        # ###################################################
        # DeclareLaunchArgument('rviz', default_value='true',
        #                       description='Open RViz.'),
        # ###################################################


        DeclareLaunchArgument('image_topic', default_value='/camera',
                              description='Topic to start viewing in RQt.'),
        bridge,
        rqt,

        # ####
        # rviz
        # ####
    ])