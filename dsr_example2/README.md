<!-- DSR Test Package Description -->
# DSR ROS 2 Example Package

## Description

A simple example package for using a Doosan Robot with the DSR ROS 2 `common2` Python package.

- **dance example**: Example using various motion services (`movej`, `movel`, `moveb`, etc.)
- **single_robot_simple example**: Example using `movej` motion services

## Requirements

- ROS 2 Humble release
- DSR ROS 2 Package Setting

## Build instructions

### DSR ROS 2 common2 package install

Add the following code to `common2/CMakeLists.txt`:

```cmake
install(DIRECTORY imp DESTINATION lib/${PROJECT_NAME}
FILES_MATCHING PATTERN "*.py"
PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ
)
```

### Edit .bashrc
Add Python Path for DSR module:
```bash
export PYTHONPATH=$PYTHONPATH:~/ros2_ws/install/common2/lib/common2/imp
```

## Build
Build example package:
```shell
cd ros2_ws
colcon build --packages-select example
```
