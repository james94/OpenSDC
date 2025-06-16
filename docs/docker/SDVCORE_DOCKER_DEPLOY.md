# SDVCore Docker Container Deployment Script

**File:** `scripts/deploy/docker/deploy.py`  

---

## **Overview**

This script is a command-line tool for deploying the SDVCore Docker container. It detects the host OS (Linux, WSL2, or Windows), configures X11 GUI forwarding when needed, manages workspace volume mounts, and ensures a clean deployment by removing any existing containers with the same name. The script is designed for both developer and CI/CD use, with clear logging and error handling.

---

## **Usage**

```bash
python scripts/deploy/docker/deploy.py [--image IMAGE] [--tag TAG] [--container_name NAME] [--gui/--no-gui]
```

**Arguments:**
- `--image`: Docker image name to deploy (default: `sdvcore`)
- `--tag`: Docker image tag (default: `latest`)
- `--container_name`: Name for the running container (default: `sdvcore_container`)
- `--gui` / `--no-gui`: Enable or disable X11 GUI support (default: enabled)

**Example:**
```bash
python scripts/deploy/docker/deploy.py --image sdvcore --tag latest --container_name my_sdvcore --gui
```

---

## **Key Features**

- **Cross-Platform Support:**  
  Detects and configures deployment for Linux, WSL2, and Windows hosts, including X11 GUI forwarding for GUI applications.

- **Workspace Mounting:**  
  Mounts the host workspace directory (`/home/ubuntu/src` by default) into the container for seamless code and data access.

- **Container Lifecycle Management:**  
  Cleans up any existing container with the same name before deploying a new one.

- **Interactive and GUI Modes:**  
  Launches containers in interactive mode (`-it`) and sets up X11 socket mounts and environment variables for GUI apps.

- **Robust Logging and Error Handling:**  
  Logs each deployment step and gracefully handles errors, making it suitable for both manual and automated workflows.

---

## **Class and Method Documentation**

### **class DockerContainerDeployer**
Manages the deployment of a Docker container with support for X11 GUI and workspace mounting.

#### **Attributes**
- `image` (str): Docker image to deploy.
- `tag` (str): Image tag.
- `container_name` (str): Name for the running container.
- `gui` (bool): Enable or disable X11 GUI support.
- `host_workspace` (str): Path to the host workspace directory.
- `container_workspace` (str): Path inside the container for the workspace.
- `os_type` (str): Detected host OS type.
- `x11_env` (dict): X11-related environment variables.
- `x11_volumes` (list): X11-related volume mounts.

#### **Methods**

- `run()`:  
  Orchestrates the deployment process through state transitions.

- `prepare()`:  
  Detects OS, checks Docker availability, configures X11 if needed, and validates the workspace directory.

- `deploy()`:  
  Removes any existing container with the same name, builds the Docker run command, and launches the container.

- `post_deploy()`:  
  Verifies container status and provides GUI usage instructions if enabled.

- `setup_x11()`:  
  Sets up X11 display environment and volume mounts based on host OS.

- `validate_workspace()`:  
  Ensures the workspace directory exists; falls back to the current directory if not.

- `cleanup_existing_container()`:  
  Removes any running or stopped container with the same name.

---

## **Design Rationale**

- **State Machine Pattern:**  
  The deployment process is modeled as a state machine for clarity, extensibility, and robust error handling.

- **Separation of Concerns:**  
  Each method is responsible for a single aspect of deployment, making the code easier to maintain and extend.

- **Cross-Platform Compatibility:**  
  Handles differences between Linux, WSL2, and Windows for GUI and filesystem access.

- **Developer and CI/CD Friendly:**  
  Designed for both interactive development and automated deployment in CI/CD pipelines.

---

## **Best Practices Followed**

- **PEP 8 code style and PEP 257 docstrings**[4][6]
- **Clear logging for all actions and errors**
- **All public interfaces (methods, CLI) are documented**[3][6]
- **Separation of configuration, logic, and error handling**
- **Extensible for future features (e.g., GPU, networking, custom entrypoints)**

---

## **Example Docstring for the Script**

```python
"""
SDVCore Docker Container Deployment Script

Automates deployment of the SDVCore Docker container with cross-platform X11 GUI support and workspace mounting.
Supports Linux, WSL2, and Windows hosts. Cleans up existing containers and provides robust logging.

Usage:
    python scripts/deploy/docker/deploy.py [--image IMAGE] [--tag TAG] [--container_name NAME] [--gui/--no-gui]
"""
```

---

## **References**

- [PEP 257: Python Docstring Conventions](https://peps.python.org/pep-0008/)
- [Python Documentation Best Practices](https://www.docuwriter.ai/posts/python-documentation-best-practices-guide-modern-teams)
- [Swimm: Documentation in Python](https://swimm.io/learn/code-documentation/documentation-in-python-methods-and-best-practices)
- [Docker Buildx Bake Documentation](https://docs.docker.com/reference/cli/docker/buildx/bake/)
- [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/index.html)
- [Real Python: Documenting Python Code](https://realpython.com/documenting-python-code/)
- [Reddit: What are your preferred conventions for documenting python code?](https://www.reddit.com/r/Python/comments/zfbm0q/what_are_your_preferred_conventions_for/)
- [Stackoverflow: Documenting and detailing a single script based on the comments inside](https://stackoverflow.com/questions/62876777/documenting-and-detailing-a-single-script-based-on-the-comments-inside)
- [The Hitchhiker's Guide to Python: Documentation](https://docs.python-guide.org/writing/documentation/)
- [Python How Tos: Documentation Best Practices](https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/best_practices.html)

---

**This script is a robust, maintainable solution for automated Docker container deployment in modern robotics and cloud-native projects.**

---

<!-- [1]: https://realpython.com/documenting-python-code/ -->
<!-- [3]: https://swimm.io/learn/code-documentation/documentation-in-python-methods-and-best-practices -->
<!-- [4]: https://peps.python.org/pep-0008/ -->
<!-- [6]: https://www.docuwriter.ai/posts/python-documentation-best-practices-guide-modern-teams -->
<!-- [9]: programming.documentation -->

<!-- [1] https://realpython.com/documenting-python-code/
[2] https://www.reddit.com/r/Python/comments/zfbm0q/what_are_your_preferred_conventions_for/ -->
<!-- [3] https://swimm.io/learn/code-documentation/documentation-in-python-methods-and-best-practices -->
<!-- [4] https://peps.python.org/pep-0008/ -->
<!-- [5] https://stackoverflow.com/questions/62876777/documenting-and-detailing-a-single-script-based-on-the-comments-inside -->
<!-- [6] https://www.docuwriter.ai/posts/python-documentation-best-practices-guide-modern-teams -->
<!-- [7] https://docs.python-guide.org/writing/documentation/
[8] https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/best_practices.html -->
<!-- [9] programming.documentation -->
