# Design Thoughts

## Subsystems
- hardware
- sensing
- control
- perception
- localisation
- navigation
- system
- simulation


## Topics
- /hardware/sensors/camera?/front/img
- /hardware/sensors/camera?/back/img
- /hardware/sensors/livox/front/points
- /hardware/sensors/livox/front/scan
- /hardware/sensors/livox/back/points
- /hardware/sensors/livox/back/scan
- /hardware/request/steering_angle
- /hardware/request/wheel_speed
- /hardware/description
- /hardware/joint_states
- /system/engaged
- /perception/*
- /localisation/*
- /control/*
- /simulation/*
    - e.g. /simulation/ground_truth/pose

## Services
- 

## Actions
- 

## Other
- How does simulation work with hardware?
- Code should use "placeholder" topic names, which are mapped to fully qualified names in a launch file
    - fully qualified names should be used in the launch file
    - individual launch files are responsible for remapping input and output names correctly to respect subsystem naming scheme
