# OpenSDC

Open Source Self-Driving Car

## Outline

- Clone OpenSDC Repo
- Self-Driving Car Simulator
- Self-Driving Car Docker Image

## Clone OpenSDC Repo

~~~bash
# Ensure Git LFS is installed on your system
sudo apt -y install git-lfs

# Initialize Git LFS for your system
git lfs install

# Clone repo (and git should auto detect LFS-tracked files)
git clone git@github.com:james94/OpenSDC.git

# Ensure all LFS files are downloaded successfully (needed for .png, .fbx, .mp3, .tga, etc)
git lfs pull

# To check which files are tracked by Git LFS
# git lfs ls-files
~~~

## Self-Driving Car Simulator

### Unity 3D Self-Driving Car Simulator

The simulator is based on Udacity's archived Unity Self-Driving Car simulator. We will update it to work with our Unity 3D version.

Heres a link to self-driving-car-sim public archive for reference: https://github.com/udacity/self-driving-car-sim/tree/master

#### Resources

- Unity Simple File Browser: https://github.com/yasirkula/UnitySimpleFileBrowser

### Unity 3D Pre-Built Self-Driving Car Simulator

- For more information on Udacity's self-driving-car-sim, you can checkout our [Udacity Self-Driving Car Simulators Notes](docs/UDACITY_CARSIM.md) to see how to launch precompiled Unity Simulator builds

## Self-Driving Car Docker Image

For more information on building a docker image for deep learning self-driving car development environment, refer steps in [UDACITY_SDC_DOCKER.md](./docs/UDACITY_SDC_DOCKER.md)
