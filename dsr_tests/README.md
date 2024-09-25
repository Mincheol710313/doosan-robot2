<!--뱃지 활용-->
<img src="https://img.shields.io/badge/python-4B89DC?style=flat-square&logo=python&logoColor=White"/>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMincheol710313%2F&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=Mincheol+Github&edge_flat=false"/></a>

<!--Github Status 활용-->
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Mincheol710313)
<!--[Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=Mincheol710313)]-->

<!-- DSR Test Package Description -->
<h1> DSR ROS 2 Test Package </h1>
<h2> Requirements </h2>
<li> ROS 2 Humble realease </li>
<li> Use Python Unittest Framwork </li>
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
Build dsr_tests package
<pre><code>
  cd ros2_ws
  colcon build --packages-select dsr_tests
</code></pre>
<h3> Test </h3>
colcon test to dsr_tests
<pre><code>
  colcon test 
</code></pre>
if you want to know about colcon test command, use <code>--help</code> command option.

