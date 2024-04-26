#!/bin/bash

# source ROS
source /opt/ros/${ROS_DISTRO}/setup.bash

# if container mounted folders are available, chown them to make sure we have
# the correct permissions
if [ -d ~/.ignition ]
then
  sudo chown -R $UID:$UID ~/.ignition
fi

if [ -d /ws/build ]
then
  sudo chown -R $UID:$UID /ws/build
fi

if [ -d /ws/install ]
then
  sudo chown -R $UID:$UID /ws/install
fi

if [ -d /ws/log ]
then
  sudo chown -R $UID:$UID /ws/log
fi

# execute the command passed into this entrypoint
exec "$@"
