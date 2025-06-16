# Autonomous Driving Stack

A modular, end-to-end software platform for the research, development, simulation, and deployment of self-driving car systems. This stack covers perception, planning, control, simulation, data management, and user interaction, integrating modern open-source technologies and industry best practices.

---

## Table of Contents  

- [Overview](#overview)  
- [Software Components](#software-components)  
- [Functionality and Scope](#functionality-and-scope)
- [Key Deliverables](#key-deliverables)
- [Architecture](#architecture)
- [Language Partitioning](#language-partitioning)  
- [C++ Modules (Safety-Critical)](#c-modules-safety-critical)
- [Python Modules (ML/Orchestration)](#python-modules-mlorchestration) 
- [C#/Unity3D Simulation](#cunity3d-simulation)  
- [Project Structure](#project-structure)  
- [How To Run](#how-to-run)

---

## Prerequisites  

- Unity 2022.3+ (simulation)  
- ROS2 Humble (C++/Python)  
- Docker 24.0+  

## Overview

This repository implements a production-grade autonomous driving stack with:  
- Real-time perception/prediction using PyTorch models  
- Safety-critical planning/control in C++  
- Unity3D simulation environment with scenario scripting  
- React/FastAPI passenger interface  
- ROS2-based middleware for modular integration  

---

## Software Components

- **Unity 3D Car Simulator**: Virtual environment for testing and validating perception, planning, and control algorithms.
- **Docker Images/Containers**: Encapsulate software modules for portability and reproducibility across environments.
- **Configuration YAML Parser**: Loads and manages system configurations for flexible deployment and tuning.
- **Workflow Event-Driven State Machine**: Orchestrates system states (idle, driving, emergency stop) and transitions based on events and sensor inputs.
- **MiNiFi C++/Python Data Pipelines**: Real-time data ingestion, preprocessing, and routing between modules.
- **PostgreSQL Database**: Stores historical driving data, logs, and metadata for training and analysis.
- **MQTT**: Lightweight messaging protocol for inter-module and cloud communication.
- **PyTorch Deep Learning**: Framework for perception (object/lane detection), sensor fusion, and decision-making models.
- **React TypeScript**: Frontend for passenger/user interfaces, dashboards, and real-time visualization.
- **FastAPI**: Backend API for serving data, handling user requests, and integrating with external services.
- **ROS2 (Robot Operating System 2)**: Middleware for inter-process communication, sensor integration, and modular software architecture.

| Component                | Technology Stack       | Criticality      |  
|--------------------------|------------------------|------------------|  
| Sensor Drivers           | C++17                  | Safety-critical  |  
| Localization             | C++ (EKF/Particle Filter) | Real-time      |  
| Perception               | PyTorch/Python + C++   | ML/CV pipeline   |  
| Path Planning            | C++/ROS2               | Safety-critical  |  
| Vehicle Control          | C++ PID controllers    | Real-time        |  
| Simulation               | Unity3D/C#             | Validation       |  
| Data Pipelines           | MiNiFi (C++/Python)    | High-throughput  |  
| User Interface           | React/FastAPI          | Passenger-facing |  


---

## Functionality and Scope

- **End-to-End Autonomy**: Full stack from sensor input to vehicle control output, including perception, planning, and control.
- **Simulation Environment**: Scenario-based validation and testing in Unity 3D.
- **Real-Time Data Pipelines**: Logging, monitoring, and data management for development and deployment.
- **User Interaction**: Intuitive interfaces for passengers and operators.
- **Modular, Containerized Deployment**: Scalable, maintainable, and reproducible workflows.

---

## Key Deliverables

- Functional self-driving stack (simulation and real-world capable)
- Passenger/user interface (React TypeScript)
- Real-time data pipelines and logging infrastructure
- Simulation scenarios and validation reports
- Comprehensive documentation and deployment scripts

---

## Architecture

The stack is organized into modular subsystems, each responsible for a core aspect of autonomous driving:

- **Sensors**: Camera, Radar, LiDAR, GPS, IMU
- **Localization**: Particle Filter, Extended Kalman Filter
- **Perception**: CNN-based object detection, tracking, traffic sign and light classification, advanced lane detection
- **Planning**: Waypoint loader/updater, route planning, behavior and trajectory planning, prediction
- **Control**: PID controller, drive-by-wire, waypoint follower
- **Simulation**: Unity 3D-based scenario generation and validation
- **Data Management**: MiNiFi pipelines, PostgreSQL, MQTT
- **User Interface**: React dashboard, FastAPI backend
- **Orchestration**: Event-driven state machine, ROS2 middleware

---

## Language Partitioning  
### C++ Modules (Safety-Critical)  
```cpp  
// Example: Real-time PID controller  
void ControlModule::update_steering() {  
  error = target_angle - current_angle;  
  integral += error * dt;  
  output = Kp*error + Ki*integral + Kd*(error-prev_error)/dt;  
}  
```
- Sensor drivers (LiDAR/Camera/Radar)  
- Localization (EKF/Particle Filter)  
- Motion planning/prediction  
- Vehicle control systems  

### Python Modules (ML/Orchestration)  
```python  
# PyTorch perception model  
class ObjectDetector(nn.Module):  
    def forward(self, sensor_data):  
        return self.yolonet(sensor_data)  
```
- Deep learning models (CNN detectors/classifiers)  
- Data preprocessing pipelines  
- Workflow state machines  
- FastAPI backend services  

### C#/Unity3D Simulation  
```csharp  
// Unity vehicle controller  
void FixedUpdate() {  
    wheelCollider.motorTorque = throttleInput * motorForce;  
    steeringAngle = maxSteerAngle * steerInput;  
}  
```
- Scenario generation toolkit  
- Sensor data synthesis  
- Visualization dashboard  

---

## Project Structure

```
autonomous-driving-stack/  
├── cpp/                       # Safety-critical components  
│   ├── control/               # PID/MPC controllers  
│   ├── perception/            # Sensor fusion algorithms  
│   └── planning/              # RRT*/Frenet planners  
├── python/                    # ML/data pipelines  
│   ├── models/                # PyTorch/YOLO networks  
│   └── orchestration/         # Airflow DAGs  
├── unity/                     # C# simulation  
│   ├── scenarios/             # OpenSCENARIO files  
│   └── assets/                # Vehicle models  
├── interface/                 # React/FastAPI  
└── tools/                     # CI/CD pipelines  
```

## How To Run

### Build SDVCore Docker Image

~~~bash
python scripts/build_image/build.py
~~~

### Deploy SDVCore Docker Container

~~~bash
python scripts/deploy/docker/deploy.py
~~~

## Resources

- Perplexity AI general reference: https://www.perplexity.ai/search/from-a-software-system-design-mMwCeIXkROGame_61.Juww
