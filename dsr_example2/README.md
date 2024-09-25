<!-- DSR Test Package Description -->
<h1> DSR ROS 2 Example Package </h1>
<h2> Requirements </h2>
<li> ROS 2 Humble realease </li>
<li> DSR ROS 2 Package Setting </li>
<h2> Build instructions </h2>
<h3> DSR ROS 2 common2 package install </h3>
Add bellow code to common2 CMakeLists.txt
<pre><code>
  install(DIRECTORY imp DESTINATION lib/${PROJECT_NAME}
  FILES_MATCHING PATTERN "*.py"
  PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ GROUP_READ WORLD_READ
  )
</code></pre>
<h3> Edit .bashrc </h3>
Add Python Path for DSR module
<pre><code>
  export PYTHONPATH=$PYTHONPATH:~/ros2_ws/install/common2/lib/common2/imp
</code></pre>
<h3> Build </h3>
Build example package
<pre><code>
  cd ros2_ws
  colcon build --packages-select example
</code></pre>
<h3> Run Dance Example </h3>
<h4> Run Simple Example </h4>
<pre><code>
  colcon test 
</code></pre>
if you want to know about colcon test command, use <code>--help</code> command option.