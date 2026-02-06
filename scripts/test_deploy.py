import os
import sys
import subprocess
import argparse
import platform
import logging
from enum import Enum, auto

class DeployState(Enum):
    INIT = auto()
    PREPARE = auto()
    DEPLOY = auto()
    POST_DEPLOY = auto()
    DONE = auto()
    ERROR = auto()

class DockerContainerDeployer:
    def __init__(self, image, tag="latest", container_name="sdvcore_container", gui=True):
        self.image = image
        self.tag = tag
        self.container_name = container_name
        self.gui = gui
        self.state = DeployState.INIT
        self.logger = logging.getLogger("DockerContainerDeployer")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
        self.os_type = None
        self.x11_env = {}
        self.x11_volumes = []
        self.host_workspace = "/home/ubuntu/src"
        self.container_workspace = "/workspace"

    def run(self):
        try:
            self.transition(DeployState.PREPARE)
            self.prepare()
            self.transition(DeployState.DEPLOY)
            self.deploy()
            self.transition(DeployState.POST_DEPLOY)
            self.post_deploy()
            self.transition(DeployState.DONE)
        except Exception as e:
            self.logger.error(f"Deployment failed: {e}")
            self.transition(DeployState.ERROR)
            sys.exit(1)

    def transition(self, new_state):
        self.logger.info(f"Transitioning to state: {new_state.name}")
        self.state = new_state

    def prepare(self):
        self.logger.info("Preparing environment...")
        self.detect_os()
        self.check_docker()
        if self.gui:
            self.setup_x11()
        self.validate_workspace()

    def detect_os(self):
        sys_platform = platform.system().lower()
        if "windows" in sys_platform:
            self.os_type = "windows"
        elif "linux" in sys_platform:
            if any(keyword in platform.uname().release.lower() 
                   for keyword in ["microsoft", "wsl"]):
                self.os_type = "wsl2"
            else:
                self.os_type = "linux"
        else:
            raise RuntimeError(f"Unsupported OS: {sys_platform}")

    def check_docker(self):
        try:
            subprocess.run(["docker", "--version"], check=True, 
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("Docker not available or not running") from e

    def setup_x11(self):
        self.logger.info("Configuring X11 display...")
        if self.os_type in ["windows", "wsl2"]:
            self.x11_env = {"DISPLAY": "host.docker.internal:0"}
        elif self.os_type == "linux":
            self.x11_env = {"DISPLAY": os.getenv("DISPLAY", ":0")}
            self.x11_volumes = ["/tmp/.X11-unix:/tmp/.X11-unix"]
            subprocess.run(["xhost", "+local:docker"], check=False)
        else:
            raise RuntimeError("X11 GUI not supported on this platform")

    def validate_workspace(self):
        if not os.path.exists(self.host_workspace):
            self.logger.warning(f"Host workspace directory {self.host_workspace} not found!")
            self.host_workspace = os.getcwd()
            self.logger.info(f"Using current directory instead: {self.host_workspace}")

    def build_docker_command(self):
        cmd = [
            "docker", "run", "-it", "--rm",
            "--name", self.container_name,
            "-v", f"{self.host_workspace}:{self.container_workspace}"
        ]

        if self.gui:
            cmd += ["-e", f"DISPLAY={self.x11_env['DISPLAY']}"]
            cmd += ["-v", "/tmp/.X11-unix:/tmp/.X11-unix"] if self.x11_volumes else []

        cmd += [f"{self.image}:{self.tag}"]
        return cmd

    def deploy(self):
        self.logger.info("Starting container deployment...")
        self.cleanup_existing_container()
        
        cmd = self.build_docker_command()
        self.logger.info(f"Executing: {' '.join(cmd)}")
        
        # Replace current process with docker command
        os.execvp(cmd[0], cmd)

    def cleanup_existing_container(self):
        result = subprocess.run(
            ["docker", "ps", "-a", "-q", "-f", f"name={self.container_name}"],
            stdout=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip():
            self.logger.info("Removing existing container...")
            subprocess.run(
                ["docker", "rm", "-f", self.container_name],
                check=True
            )

    def post_deploy(self):
        self.logger.info("Validating container deployment...")
        subprocess.run(
            ["docker", "ps", "-f", f"name={self.container_name}"],
            check=True
        )

def main():
    parser = argparse.ArgumentParser(
        description="SDVCore Docker Deployment Manager",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--image", 
        default="sdvcore_base_s_30_sdventry", 
        help="Docker image name"
    )
    parser.add_argument(
        "--tag", 
        default="latest", 
        help="Docker image tag"
    )
    parser.add_argument(
        "--container-name", 
        default="sdvcore_container",
        help="Container instance name"
    )
    parser.add_argument(
        "--no-gui",
        dest="gui",
        action="store_false",
        help="Disable X11 GUI support"
    )
    parser.set_defaults(gui=True)

    args = parser.parse_args()

    deployer = DockerContainerDeployer(
        image=args.image,
        tag=args.tag,
        container_name=args.container_name,
        gui=args.gui
    )
    
    deployer.run()

if __name__ == "__main__":
    main()
