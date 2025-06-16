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
        self.container_workspace = "/home/ubuntu/src"
    
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
        # Detect OS
        self.detect_os()

        # Check Docker
        self.check_docker()

        # Setup X11 for GUI apps
        if self.gui:
            self.setup_x11()
        self.validate_workspace()

    def detect_os(self):
        sys_platform = platform.system().lower()
        if "windows" in sys_platform:
            self.os_type = "windows"
        elif "linux" in sys_platform:
            # Further check if WSLg is present
            if any(keyword in platform.uname().release.lower() for keyword in ["microsoft", "wsl"]):
                self.os_type = "wsl2"
            else:
                self.os_type = "linux"
        else:
            raise RuntimeError(f"Unsupported OS: {sys_platform}")

    def check_docker(self):
        try:
            subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("Docker not available or not running") from e

    def setup_x11(self):
        self.logger.info(f"Configuring X11 display for {self.os_type}...")
        if self.os_type == "windows" or self.os_type == "wsl2":
            # WSL2 + WSLg: X11 socket is at /tmp/.X11-unix, DISPLAY=:0, access is built-in
            self.x11_env = {"DISPLAY": ":0"}
            self.x11_volumes = ["/tmp/.X11-unix:/tmp/.X11-unix:rw"]
        elif self.os_type == "linux":
            # Ubuntu: Use host's X11 socket and DISPLAY
            display = os.environ.get("DISPLAY", ":0")
            self.x11_env = {"DISPLAY": display}
            self.x11_volumes = ["/tmp/.X11-unix:/tmp/.X11-unix:rw"]
            # Optionally, handle xhost permissions
            subprocess.run(["xhost", "+local:docker"], check=False)
        else:
            raise RuntimeError("X11 GUI not supported on this OS.")

    def validate_workspace(self):
        if not os.path.exists(self.host_workspace):
            self.logger.warning(f"Host workspace directory {self.host_workspace} not found!")
            self.host_workspace = os.getcwd()
            self.logger.info(f"Using current directory instead: {self.hsot_workspace}")
        
    def build_docker_command(self):
        cmd = [
            "docker", "run", "-it", "--rm",
            "--name", self.container_name,
            "-v", f"{self.host_workspace}:{self.container_workspace}",
        ]

        if self.gui:
            cmd += ["-e", f"DISPLAY={self.x11_env['DISPLAY']}"]
            for vol in self.x11_volumes:
                cmd += ["-v", vol]

        cmd += [f"{self.image}:{self.tag}"]
        return cmd

    def cleanup_existing_container(self):
        result = subprocess.run(
            ["docker", "ps", "-a", "-q", "-f", f"name={self.container_name}"],
            stdout=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip():
            self.logger.info("Removing existing container...")
            subprocess.run(
                ["docker", "rm", "-f", self.container_name], check=True
            )

    def deploy(self):
        self.logger.info("Deploying Docker container...")
        self.cleanup_existing_container()
        cmd = self.build_docker_command()
        self.logger.info("Running: " + " ".join(cmd))
        subprocess.run(cmd, check=True)
        self.logger.info(f"Container {self.container_name} deployed.")

    def post_deploy(self):
        self.logger.info("Post-deployment: Validating container status...")
        # Optionally check logs or attach
        subprocess.run(["docker", "ps", "-f", f"name={self.container_name}"])
        # Optionally, print instructions for GUI apps
        if self.gui:
            self.logger.info("If your container runs a GUI app, it should now display on your host's X server.")

def main():
    parser = argparse.ArgumentParser(description="SDVCore Docker Deployment Manager",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--image", default="sdvcore", help="Docker image name (e.g., sdvcore_base)")
    parser.add_argument("--tag", default="latest", help="Docker image tag")
    parser.add_argument("--container_name", default="sdvcore_container", help="Docker container name")
    parser.add_argument("--gui", dest="gui", action="store_true", help="Enable X11 GUI support")
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
