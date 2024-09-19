import rclpy
import os

# for single robot
ROBOT_ID   ="dsr01"
ROBOT_MODEL="m1013"

import DR_init
DR_init.__dsr__id   = ROBOT_ID
DR_init.__dsr_model = ROBOT_MODEL

from DSR_ROBOT2 import *

if __name__ == "__main__":
        rclpy.init()

        node = rclpy.create_node('dsr_simple_test_py')

        DR_init.__dsr_node = node
        
        set_velx(30, 20)
        set_accx(60, 40)

        JReady = [0, 0, 90, 0, 90, 0]
        
        movej(JReady, vel=20, acc=20)

        rclpy.shutdown()