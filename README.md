
# ROS2 Jazzy Project: Trash Detection Robot

![image](https://github.com/user-attachments/assets/11842f1f-3047-40e7-85f5-580d4c83c5cc)


## Overview

This ROS2 (Jazzy) project simulates a trash detection robot with three main packages:

    perception – Processes mock camera input to detect trash.

    brain – Decides robot movement based on detections and monitors battery.

    actuator – Executes movement commands from the brain.

The system uses topics for communication and services for battery status checks.
## Packages & Nodes
### 1. perception Package

#### Node: perception_node

    Subscribes to: /camera_topic (receives mock strings: "trash image" or "no trash image")

    Publishes to: /trash_detection (sends detection results)

    Services:

        /component_status (reports battery level when requested by the brain)

#### Functionality:

    If input is "trash image", publishes detected=True.

    If input is "no trash image", publishes detected=False.

    Responds to battery status requests with a value between 0.0 (empty) and 1.0 (full).

### 2. brain Package

#### Node: brain_node

    Subscribes to: /trash_detection (receives detections from perception)

    Publishes to: /actuator_commands (sends movement instructions)

    Services:

        Calls /component_status every 5 seconds to check battery.

#### Functionality:

    If trash is detected, sends a command to move the robot.

    If no trash is detected, does nothing.

    Logs battery status periodically.

### 3. actuator Package

#### Node: actuator_node

    Subscribes to: /actuator_commands (receives movement commands from the brain)

#### Functionality:

    Moves the robot when instructed (simulated for now).



## Installation & Setup
### Prerequisites

   **1:** ROS2 Jazzy

   **2:** Python 3.x

### Build & Run

    Clone & Build:

     mkdir -p ~/trashbot_ws/src
    cd ~/trashbot_ws/src
    git clone [[YOUR_REPO_URL](https://github.com/KhaledGhandour/trash-collection-robot.git)]
    cd ~/trashbot_ws
    colcon build
    source install/setup.bash







## Future Improvements:

  **✅** Replace mock camera input with real OpenCV processing
  **✅** Add obstacle avoidance
  ✅ Implement battery recharge behavior
  ✅ Integrate with real hardware (Raspberry Pi/Arduino)











## Contact 📧

**Developer:**  Khaled Ghandour

**Email:** khaled.essam.200230@gmail.com

**Project Link:** (https://github.com/KhaledGhandour/trash-collection-robot.git)




