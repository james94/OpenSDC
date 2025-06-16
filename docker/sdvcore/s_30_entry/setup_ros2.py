import os
import sys
import subprocess
import shutil

class SetupROS2:
    def __init__(self, logger=None, ros_distro="humble"):
        self.ros_distro = ros_distro
        self.ros_setup_script = f"/opt/ros/{ros_distro}/setup.bash"
        self.logger = logger
        self.env_sourced = False
        self.python_path = sys.executable
        self.ros2cli_path = shutil.which("ros2") or f"/opt/ros/{ros_distro}/bin/ros2"


    def source_ros2_environment(self):
        if not os.path.exists(self.ros_setup_script):
            msg = f"ROS2 setup script not found at {self.ros_setup_script}."
            if self.logger:
                self.logger.error(msg)
            else:
                print(msg)
            raise FileNotFoundError(msg)

        command = f"bash -c 'source {self.ros_setup_script} && env'"
        if self.logger:
            self.logger.info(f"Sourcing ROS2 environment: {self.ros_setup_script}")
        proc = subprocess.Popen(command, 
            shell=True, stdout=subprocess.PIPE, 
            executable="/bin/bash")
        for line in proc.stdout:
            key, _, value = line.decode().partition("=")
            if key and value:
                os.environ[key.strip()] = value.strip()
        proc.communicate()
        self.env_sourced = True
        if self.logger:
            self.logger.info("ROS2 environment variables loaded into process.")

    def is_ros2_setup(self):
        return os.environ.get("ROS_DISTRO", "") == self.ros_distro

    def get_python(self):
        return sys.executable
    
    def get_user(self):
        return os.environ.get("USER", "")
    
    def is_venv_active(self):
        return (hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix")
                and sys.base_prefix != sys.prefix))

    def get_ros2cli_path(self):
        return self.ros2cli_path

    def status(self):
        return {
            "ros2_setup": self.is_ros2_setup(),
            "python": self.get_python(),
            "venv_active": self.is_venv_active(),
            "user": self.get_user(),
            "ros2cli_path": self.get_ros2cli_path(),
        }
