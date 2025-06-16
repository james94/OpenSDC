import os
import sys
import logging
import argparse
# import subprocess
from setup_ros2 import SetupROS2

class SDVEntrypoint:
    def __init__(self):
        self.progname = "sdvcore-entrypoint"
        self.commands = ['bash', 'ros2', 'script', 'status', 'help']
        self.parser = self.create_argument_parser()
        self.args = self.parser.parse_args()
        self.logger = logging.getLogger("SDVEntrypoint")
        logging.basicConfig(level=logging.INFO)
        self.ros2_setup = SetupROS2(self.logger, ros_distro="humble")
        # self.ros2_setup.source_ros2_environment()
        self.initialize_environment()

    def in_docker(self):
        # Heuristic: check for /.dockerenv
        return os.path.exists("/.dockerenv")

    def create_argument_parser(self):
        parser = argparse.ArgumentParser(
            prog = self.progname,
            description = "SDVEntrypoint: Interactive Docker Entrypoint for SDVCore",
            epilog = "Examples:\n python entrypoint.py bash\n python entrypoint.py ros2 arg1 arg2\n python entrypoint.py script myscript.py\n python entrypoint.py status",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("command", nargs="?", default="bash", choices=self.commands, 
            help="Which command to run: bash, ros2, script, status, help")
        parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for the command")
        return parser

    def show_env_status(self):
        status = self.ros2_setup.status()
        print("=== SDVEntrypoint Environment Status ===")
        print(f"ROS2 setup: {'Yes' if status['ros2_setup'] else 'No'}")
        print(f"Python: {status['python']}")
        print(f"Virtual Env: {'Active' if status['venv_active'] else 'No'}")
        print(f"User: {status['user']}")
        print(f"ROS2 CLI Path: {status['ros2cli_path']}")
        print(f"In Docker: {'Yes' if self.in_docker() else 'No'}")
        print("========================================")

    def run_bash(self):
        self.logger.info("Launching interactive /bin/bash shell...")
        os.execvp("/bin/bash", ["/bin/bash"])
    
    def run_ros2(self):
        ros2cli = self.ros2_setup.get_ros2cli_path()
        if not os.path.exists(ros2cli):
            self.logger.error(f"ros2 CLI not found at {ros2cli}")
            sys.exit(1)
        cmd = [ros2cli] + self.args.args
        self.logger.info(f"Running ros2 CLI: {' '.join(cmd)}")
        os.execvp(ros2cli, cmd)

    def run_script(self):
        if not self.args.args:
            self.logger.error("No script specified for 'script' command.")
            sys.exit(1)
        script = self.args.args[0]
        if not os.path.exists(script):
            self.logger.error(f"Script not found: {script}")
            sys.exit(1)
        ext = os.path.splitext(script)[1]
        if ext == ".py":
            cmd = [self.ros2_setup.get_python(), script] + self.args.args[1:]
        elif ext in [".sh", ""]:
            cmd = ["/bin/bash", script] + self.args.args[1:]
        else:
            self.logger.error("Unsupported script type. Use .py or .sh")
            sys.exit(1)
        self.logger.info(f"Running script: {' '.join(cmd)}")
        os.execvp(cmd[0], cmd)
    
    def run_command(self, command):
        self.logger.info(f"Executing command: {' '.join(command)}")
        os.execvp(command[0], command)

    def execute_command(self):
        cmd = self.args.command
        if cmd == "bash":
            self.run_bash()
        elif cmd == "ros2":
            self.run_ros2()
        elif cmd == "script":
            self.run_script()
        elif cmd == "status":
            self.show_env_status()
            sys.exit(0)
        elif cmd == "help":
            self.parser.print_help()
            sys.exit(0)
        else:
            self.logger.error(f"Unknown command: {cmd}")
            self.parser.print_help()
            sys.exit(0)


    def initialize_environment(self):
        self.logger.info("Initializing container environment...")
        self.ros2_setup.source_ros2_environment()
        self.logger.info("ROS2 environment initialized")

    def run(self):
        try:
            self.logger.info("SDVEntrypoint starting up...")
            self.execute_command()
        except Exception as e:
            self.logger.error(f"Entrypoint failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    entrypoint = SDVEntrypoint()
    entrypoint.run()
