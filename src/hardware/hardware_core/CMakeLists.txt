cmake_minimum_required(VERSION 3.8)
project(hardware_core)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch urdf meshes DESTINATION share/${PROJECT_NAME}/)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env_hooks/gazebo_setup.dsv.in")

# Package
ament_package()
