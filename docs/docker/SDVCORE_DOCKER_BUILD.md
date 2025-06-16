## SDVCore Docker Image Build Automation Script  
**File:** `scripts/build_image/build.py`

---

### **Overview**

This script automates the process of building the SDVCore Docker image using Docker Buildx Bake and an HCL configuration. It is designed for robust, reproducible, and maintainable builds, supporting both developer and CI/CD workflows on WSL2/Windows 11 and Linux hosts.

---

### **Key Features**

- **State Machine Architecture:**  
  The build process is organized into clear states: INIT, PREPARE, BUILD, CLEANUP, DONE, ERROR. This structure enables robust error handling and clear logging throughout the build lifecycle.

- **Prerequisite Checks:**  
  The script verifies that both Docker and Docker Buildx are installed and available before proceeding, reducing the risk of build failures due to missing dependencies.

- **Context-Aware Directory Management:**  
  Automatically changes the working directory to the location of the `docker-bake.hcl` file, ensuring all relative paths in the bake file and Dockerfiles resolve correctly.

- **Flexible Configuration:**  
  Supports custom image tags and alternate bake file paths via command-line arguments.

- **Buildx Bake Integration:**  
  Leverages Docker Buildx Bake for multi-stage, cache-efficient builds, with support for advanced build features (e.g., network host, custom filesystem permissions).

- **Automated Cleanup:**  
  After building, the script prunes unused buildx cache and dangling images to conserve disk space and keep the development environment clean.

- **Comprehensive Logging:**  
  All major steps and errors are logged with timestamps for easy troubleshooting and auditing.

---

### **Usage**

```bash
python scripts/build_image/build.py [TAG] [DOCKER_BAKE_PATH]
```
- `TAG` (optional): The image tag to use (default: `latest`)
- `DOCKER_BAKE_PATH` (optional): Path to the `docker-bake.hcl` file (default: `../../docker/sdvcore/docker-bake.hcl`)

**Example:**
```bash
python scripts/build_image/build.py v1.1.0
```

---

### **Class and Method Documentation**

#### **class DockerBuildxBakeManager**
Automates the Docker Buildx Bake process for SDVCore images.

**Attributes:**
- `tag` (str): Docker image tag.
- `docker_bake_path` (str): Path to the bake HCL file.
- `bake_dir` (str): Directory containing the bake file.
- `entries_path` (str): Path to the entrypoint directory for context permissions.
- `logger` (logging.Logger): Logger for build events.
- `state` (BuildState): Current state of the build process.

**Methods:**

- `run()`:  
  Orchestrates the full build process, transitioning through all states.

- `transition(new_state)`:  
  Logs and updates the current state.

- `prepare()`:  
  Checks Docker and Buildx availability, verifies the bake file exists.

- `build()`:  
  Changes to the bake directory and invokes the Buildx Bake process with appropriate flags.

- `cleanup()`:  
  Prunes buildx cache, dangling images, and build cache to maintain a clean environment.

---

### **Best Practices Reflected**

- **Docstrings and Comments:**  
  The code is structured for clarity, with method-level docstrings recommended for further maintainability[1][3][6].

- **Separation of Concerns:**  
  Each method handles a single responsibility, making the script easy to extend or debug.

- **External Configuration:**  
  The script expects the Docker build configuration (HCL) and Dockerfiles to be maintained outside the script, supporting modular project structure.

---

### **Example Docstring for the Script (Recommended)**

```python
"""
SDVCore Docker Buildx Bake Automation Script

This script automates the building of SDVCore Docker images using Docker Buildx Bake and an HCL configuration.
It is designed for robust, reproducible builds and supports both developer and CI/CD workflows.

Usage:
    python scripts/build_image/build.py [TAG] [DOCKER_BAKE_PATH]

Author: [Your Name]
Date: 2025-06-15
"""
```

---

### **Extending the Script**

- **Add more build states** (e.g., POST_BUILD for notifications or artifact handling).
- **Integrate with CI/CD** by wrapping this script in pipeline steps.
- **Add more logging or exception handling** for custom error reporting.

---

### **References**

- [PEP 257: Python Docstring Conventions](https://peps.python.org/pep-0008/)
- [Python Documentation Best Practices](https://www.docuwriter.ai/posts/python-documentation-best-practices-guide-modern-teams)
- [Real Python: Documenting Python Code](https://realpython.com/documenting-python-code/)
- [Swimm: Documentation in Python](https://swimm.io/learn/code-documentation/documentation-in-python-methods-and-best-practices)
- [Docker Buildx Bake Documentation](https://docs.docker.com/reference/cli/docker/buildx/bake/)

- [Reddit: What are your preferred conventions for documenting python code?](https://www.reddit.com/r/Python/comments/zfbm0q/what_are_your_preferred_conventions_for/)
- [Stackoverflow: Documenting and detailing a single script based on the comments inside](https://stackoverflow.com/questions/62876777/documenting-and-detailing-a-single-script-based-on-the-comments-inside)
- [The Hitchhiker's Guide to Python: Documentation](https://docs.python-guide.org/writing/documentation/)
- [Python How Tos: Documentation Best Practices](https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/best_practices/best_practices.html)

---

**This script is a robust foundation for automated, maintainable Docker image builds in a modern robotics or cloud-native software project.**

---
