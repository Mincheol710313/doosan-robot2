<!-- DSR Test Package Description -->
<h1> DSR ROS 2 Example Package </h1>
<h2> Description </h2>
A simple example package for using a Doosan Robot with the DSR ROS 2 <code>common2</code> Python package.
<li> dance example : Example using various motion services(movej, movel, moveb, etc..) </li>
<li> single_robot_simple example : Example using movej motion serivces </li>
<h2> Requirements </h2>
<li> ROS 2 Humble realease </li>
<li> DSR ROS 2 Package Setting </li>
<h2> Build instructions </h2>
<h3> DSR ROS 2 common2 package install </h3>
Add bellow code to common2 CMakeLists.txt
<pre><code>install(DIRECTORY imp DESTINATION lib/${PROJECT_NAME}
FILES_MATCHING PATTERN "*.py"
PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ
)</code></pre>
<h3> Edit .bashrc </h3>
Add Python Path for DSR module
<pre><code>export PYTHONPATH=$PYTHONPATH:~/ros2_ws/install/common2/lib/common2/imp</code></pre>
<h3> Build </h3>
Build example package
<pre><code>cd ros2_ws
colcon build --packages-select example</code></pre>
<h3> Run Dance Example </h3>
<pre><code>ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
ros2 run example dance</code></pre>
<h4> Run Simple Example </h4>
<pre><code>ros2 launch dsr_bringup2 dsr_bringup2_rviz.launch.py mode:=virtual host:=127.0.0.1 port:=12345 model:=m1013
ros2 run example single_robot_simple
</code></pre>

