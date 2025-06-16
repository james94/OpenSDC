import subprocess
import sys
import os
import shutil
import logging
from enum import Enum, auto

class BuildState(Enum):
    INIT = auto()
    PREPARE = auto()
    BUILD = auto()
    POST_BUILD = auto()
    CLEANUP = auto()
    DONE = auto()
    ERROR = auto()

class DockerBuildxBakeManager:
    def __init__(self, tag="latest", docker_bake_path=None):
        self.state = BuildState.INIT
        self.tag = tag
        self.docker_bake_path = docker_bake_path or os.path.join(os.path.dirname(__file__), "../../docker/sdvcore/docker-bake.hcl")
        self.bake_dir = os.path.abspath(os.path.dirname(self.docker_bake_path))
        self.entries_path = os.path.join(self.bake_dir, "s_30_entry")

        self.logger = logging.getLogger("DockerBuildxBakeManager")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

    def run(self):
        try:
            self.transition(BuildState.PREPARE)
            self.prepare()
            self.transition(BuildState.BUILD)
            self.build()
            self.transition(BuildState.CLEANUP)
            self.cleanup()
            self.transition(BuildState.DONE)
        except Exception as e:
            self.logger.error(f"Error encountered: {e}")
            self.transition(BuildState.ERROR)
            self.cleanup()
            sys.exit(1)

    def transition(self, new_state):
        self.logger.info(f"Transitioning to state: {new_state.name}")
        self.state = new_state
    
    def prepare(self):
        self.logger.info("Checking prerequisites...")
        # Check Docker
        try:
            subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE)
            subprocess.run(["docker", "buildx", "version"], check=True, stdout=subprocess.PIPE)
        except Exception as e:
            raise RuntimeError("Docker or Buildx not available: " + str(e))
        # Check docker-bake.hcl exists
        if not os.path.isfile(self.docker_bake_path):
            raise FileNotFoundError(f"Bake file not found: {self.docker_bake_path}")

        self.logger.info("All prerequisites satisfied.")

    def build(self):
        self.logger.info(f"Changing working directory to {self.bake_dir}")
        os.chdir(self.bake_dir)

        self.logger.info("Starting Docker Buildx Bake process...")
        cmd = [
            "docker", "buildx", "bake",
            # "--no-cache",
            "--pull",
            f"--allow=fs.read={self.entries_path}",
            "--allow=network.host",
            "-f", self.docker_bake_path
            # "--progress", "plain"
        ]

        self.logger.info("Running: " + " ".join(cmd))
        subprocess.run(cmd, check=True)
        self.logger.info("Buildx Bake process completed.")

    def cleanup(self):
        self.logger.info("Performing Docker Cleanup.")
        try:
            # Clean buildx cache
            subprocess.run(["docker", "buildx", "prune", "-f"], check=True)

            # Remove dangling images
            subprocess.run(["docker", "image", "prune", "-f"], check=True)

            # Remove dangling build cache
            subprocess.run(["docker", "builder", "prune", "-f"], check=True)
        except Exception as e:
            self.logger.warning(f"Cleanup encountered an error: {e}")

def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "latest"
    
    # Optionally, allow passing a custom bake path as a second argument
    docker_bake_path = sys.argv[2] if len(sys.argv) > 2 else None

    builder = DockerBuildxBakeManager(tag=tag, docker_bake_path=docker_bake_path)
    builder.run()

if __name__ == "__main__":
    main()
