cmake_minimum_required(VERSION 3.0.2)
project(kinyarwanda_tts)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

install(PROGRAMS
  scripts/tts_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

