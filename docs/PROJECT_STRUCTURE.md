# Project Folder Structure (Idea)

Here is a proposed folder structure for your end-to-end autonomous driving stack, explicitly partitioning critical performance and safety modules for C++, high-level orchestration and ML for Python, and simulation for C#. This structure reflects industry best practices for modularity, safety, and performance[6][7][2].

```
autonomous-driving-stack/
│
├── README.md
├── docker/                         # Dockerfiles and container orchestration scripts
├── config/                         # YAML configuration files for all modules
├── docs/                           # Documentation, architecture diagrams, API specs
├── scripts/                        # Utility scripts for setup, deployment, and testing
│
├── simulation/                     # Unity3D Car Simulator (C#)
│   ├── unity_project/              # Unity project files and C# scripts
│   └── scenarios/                  # Scenario definitions and test cases
│
├── sensors/                        # Sensor drivers and data interfaces
│   ├── camera_cpp/                 # C++ camera drivers and interfaces
│   ├── lidar_cpp/                  # C++ LiDAR drivers and interfaces
│   ├── radar_cpp/                  # C++ radar drivers and interfaces
│   └── gps_cpp/                    # C++ GPS drivers and interfaces
│
├── localization/                   # Localization algorithms
│   ├── particle_filter_cpp/        # C++ Particle Filter implementation
│   └── ekf_cpp/                    # C++ Extended Kalman Filter implementation
│
├── perception/                     # Perception stack
│   ├── cpp/                        # C++ real-time perception (critical path, e.g., sensor fusion)
│   └── python/                     # PyTorch-based deep learning (object detection, lane detection, etc.)
│       ├── object_detection/
│       ├── lane_detection/
│       ├── traffic_sign_classifier/
│       ├── traffic_light_classifier/
│       ├── behavioral_cloning/
│       └── tracking/
│
├── planning/                       # Path and behavior planning
│   ├── cpp/                        # C++ real-time path/trajectory planning and prediction
│       ├── waypoint_loader/
│       ├── waypoint_updater/
│       ├── route_planning/
│       ├── prediction/
│       ├── behavior_planning/
│       └── trajectory_planning/
│   └── python/                     # High-level planners, experimentation, or ML-based planning
│
├── control/                        # Vehicle control algorithms
│   ├── cpp/                        # C++ PID, drive-by-wire, waypoint follower (real-time, safety critical)
│       ├── pid/
│       ├── drive_by_wire/
│       └── waypoint_follower/
│   └── python/                     # Optional: prototyping, non-critical controllers
│
├── ros2/                           # ROS2 nodes, launch files, and packages (C++ and Python)
│   ├── launch/
│   ├── src_cpp/
│   └── src_python/
│
├── data_management/                # Data pipelines, DB schemas, MQTT, MiNiFi
│   ├── minifi_cpp/                 # C++ MiNiFi data pipeline components
│   ├── minifi_python/              # Python MiNiFi data pipeline components
│   ├── db/                         # PostgreSQL schema, migration scripts
│   ├── mqtt/                       # MQTT broker/client configs and code (C++ and Python)
│   └── ingestion/                  # Data ingestion and preprocessing scripts
│
├── user_interface/                 # Passenger/operator UIs
│   ├── frontend/                   # React TypeScript codebase
│   └── backend/                    # FastAPI backend, API endpoints (Python)
│
├── workflow/                       # Event-driven state machines, orchestration logic
│   ├── cpp/                        # C++ state machines for real-time modules
│   └── python/                     # Python state machines for orchestration, integration
│
├── tests/                          # End-to-end and integration test suites (Python, C++, C#)
│
└── tools/                          # Utilities, monitoring, logging, and development tools
```

---

## Language Partitioning Rationale

- **C++:** Used for all real-time, safety-critical modules (sensor drivers, localization, core perception, path planning, control, and state machines) to ensure high performance, low latency, and compliance with automotive safety standards[6][7].
- **Python:** Used for deep learning (PyTorch), high-level orchestration, rapid prototyping, data pipelines, and backend APIs, leveraging Python’s productivity and ML ecosystem[2].
- **C#:** Used exclusively for the Unity3D simulator and scenario scripting.
- **ROS2:** Supports both C++ and Python nodes for flexible integration and modularity.
- **React TypeScript:** For user-facing dashboards and visualization.

This structure supports modularity, scalability, and efficient collaboration across teams specializing in different languages and domains, while aligning with industry and academic best practices for autonomous vehicle software development[6][7][2].

## Citations:

- [1] https://www.reddit.com/r/SelfDrivingCars/comments/iie3qs/preparing_for_a_c_software_engineer_for_self/
- [2] https://github.com/kuzen/Awesome-Self-Driving
- [3] https://carla.readthedocs.io/en/latest/start_introduction/
- [4] https://github.com/mikeroyal/Autonomous-Systems-Guide
- [5] https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/choosing-an-autonomous-program-from-smartdashboard.html
- [6] http://www.propellence.com/blog/c-driving-autonomous--cars
- [7] https://www.griddynamics.com/blog/c-automotive

## Resources

- Perplexity AI specific reference: https://www.perplexity.ai/search/from-a-software-system-design-mMwCeIXkROGame_61.Juww#5

- Perplexity AI general reference: https://www.perplexity.ai/search/from-a-software-system-design-mMwCeIXkROGame_61.Juww
