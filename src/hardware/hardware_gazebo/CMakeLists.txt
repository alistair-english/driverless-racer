cmake_minimum_required(VERSION 3.8)
project(hardware_gazebo)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch models worlds urdf config DESTINATION share/${PROJECT_NAME}/)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env_hooks/gazebo_setup.dsv.in")

# Package
ament_package()
