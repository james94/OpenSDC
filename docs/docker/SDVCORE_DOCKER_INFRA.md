## SDVCore Docker Buildx Bake Infrastructure  
**Software Documentation**

---

### **Overview**

This documentation describes the Docker Buildx Bake infrastructure for the SDVCore project, designed for reproducible, layered builds of a ROS 2 Humble-based robotics application. The system is optimized for cross-platform development (including WSL2 on Windows 11), CI/CD automation, and modular maintenance.

---

### **Folder Structure**

```
docker/sdvcore/
├── docker-bake.hcl
├── s_10_apt/
│   ├── apt_package_list.txt
│   └── Dockerfile
├── s_20_ros_humble/
│   ├── ros_humble_package_list.txt
│   └── Dockerfile
└── s_30_entry/
    ├── Dockerfile
    ├── entrypoint.py
    └── setup_ros2.py
```

---

### **Component Breakdown**

#### **1. docker-bake.hcl**

- **Purpose:**  
  Orchestrates multi-stage builds using Docker Buildx Bake, defining build targets, dependencies, and output.
- **Key Targets:**
  - `s_apt`: Base Ubuntu image with core system packages and CMake.
  - `s_ros_humble`: Adds ROS 2 Humble and related packages.
  - `sdvcore`: Application entrypoint with Python orchestration.

- **Key Features:**
  - Uses tags for versioning (`${TAG}`).
  - Each target outputs a local Docker image (`type=docker`).
  - Supports host networking and `linux/amd64` platform.

#### **2. s_10_apt/Dockerfile**

- **Purpose:**  
  Builds the foundational system layer.
- **Features:**
  - Starts from Ubuntu 22.04.
  - Installs packages from `apt_package_list.txt` using a robust, comment-friendly Perl filter.
  - Installs CMake 3.24.1 directly from Kitware.
  - Sets up a Python 3 virtual environment with Conan for C++ dependency management.
  - Ensures non-interactive, reproducible builds.

#### **3. s_20_ros_humble/Dockerfile**

- **Purpose:**  
  Adds ROS 2 Humble and its dependencies.
- **Features:**
  - Inherits from `s_apt`.
  - Installs ROS 2 Humble packages from `ros_humble_package_list.txt`.
  - Sets up ROS 2 apt repositories and keys.
  - Configures locales and environment variables for ROS 2.

#### **4. s_30_entry/Dockerfile**

- **Purpose:**  
  Configures the application entrypoint and runtime environment.
- **Features:**
  - Inherits from `s_ros_humble`.
  - Copies in `entrypoint.py` and `setup_ros2.py` for Python-based orchestration.
  - Sets the container entrypoint to the Python script.
  - Sets ROS 2 environment variables (e.g., `ROS_DOMAIN_ID`).

#### **5. s_30_entry/entrypoint.py**

- **Purpose:**  
  Provides a flexible, interactive CLI for the container.
- **Features:**
  - Supports commands: `bash`, `ros2`, `script`, `status`, `help`.
  - Initializes and validates the ROS 2 environment.
  - Allows running interactive shells, ROS 2 CLI commands, or custom scripts.
  - Displays environment status for debugging.

#### **6. s_30_entry/setup_ros2.py**

- **Purpose:**  
  Encapsulates ROS 2 environment setup and validation.
- **Features:**
  - Sources the ROS 2 environment and updates process environment variables.
  - Provides methods to check if ROS 2 is sourced, get Python path, user, and venv status.
  - Used by `entrypoint.py` for robust environment management.

---

### **Build & Deployment Workflow**

1. **Build the Images**
   - Use Docker Buildx Bake from the `docker/sdvcore` directory:
     ```bash
     docker buildx bake --pull
     ```
   - Images are tagged and loaded into the local Docker daemon.

2. **Deploy the Container**
   - Run the final image (`sdvcore:latest` by default):
     ```bash
     docker run -it --rm sdvcore:latest
     ```
   - The container will launch `entrypoint.py`, providing an interactive CLI.

---

### **Design Rationale**

- **Layered Architecture:**  
  Each Dockerfile builds on the previous, isolating system, middleware, and application layers for efficient caching and modular updates.
- **Externalized Package Lists:**  
  Makes dependency management auditable and easy to update.
- **Python Entrypoint:**  
  Offers flexibility for robotics workflows—developers can start a shell, run ROS 2 commands, or execute scripts directly.
- **CI/CD Ready:**  
  All installations are non-interactive; the build is deterministic and easily integrated into automated pipelines.
- **Cross-Platform:**  
  Designed and tested for WSL2 on Windows 11 and Linux native hosts.

---

### **Extending the System**

- **Add System or ROS 2 Packages:**  
  Update the respective package list files and rebuild.
- **Customize Entrypoint:**  
  Extend `entrypoint.py` to support more commands or initialization logic.
- **Add More Build Targets:**  
  Edit `docker-bake.hcl` to define new image layers or application variants.

---

### **Best Practices**

- **Keep package lists up to date and reviewed.**
- **Use multi-stage builds for minimal, secure images.**
- **Leverage buildx bake for reproducible, parallel builds.**
- **Document all custom scripts and entrypoints for maintainability.**

---

### **References**

- [Docker Buildx Bake documentation](https://docs.docker.com/build/bake/)
- [ROS 2 Humble documentation](https://docs.ros.org/en/humble/index.html)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)

---

**This infrastructure provides a maintainable, scalable, and developer-friendly foundation for robotics and ROS 2 containerized workflows.**