# OpenSDC

Open Source Self-Driving Car

## Outline

- Clone OpenSDC Repo
- Self-Driving Car Simulator
    - Unity 3D SDC Simulator Overview
    - Launch Unity 3D SDC Simulator from Source
    - Udacity Unity 3D Pre-Built SDC Simulators
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

### Unity 3D SDC Simulator Overview

The simulator is based on Udacity's archived Unity Self-Driving Car simulator. We will update it to work with our Unity 3D 2022.3.50f1 HDRP project.

After migrating Udacity's **self-driving-car-sim** assets over to our Unity 3D HDRP project and making some necessary, we were able to load scenes from Udacity's **Self Driving Car** asset. You will notice pink because the assets need to be updated to be compatible with HDRP.

![](./docs/images/udacity_lake_track_training_before_hdrp_fix_in_unity_2022_3_50f1.png)

**Figure 1:** Unity3D Lake Track Training Scene (ported over to HDRP before HDRP Fixes as we see pink)

![](./docs/images/udacity_jungle_track_training_before_hdrp_fix_in_unity_2022_3_50f1.png)

**Figure 2:** Unity3D Jungle Track Training Scene (ported over to HDRP before HDRP Fixes as we see pink)

After instructing my **Unity 3D 2022.3.50f1 HDRP project** through **HDRP Wizard** to **Convert All Built-in Materials to HDRP**, we were able to successfully automate most of our **SDC Simulator materials** to HDRP materials that **use HDRP built-in shaders**. We can see most of the pink objects from our scenes earlier are now illustrated in their expected color.

![](./docs/images/udacity_jungle_track_training_after_hdrp_fix_in_unity_2022_3_50f1.png)

**Figure 3:** Unity3D Jungle Track Training Scene (ported over to HDRP with automated HDRP Fixes via HDRP Wizard)

![](./docs/images/udacity_lake_track_training_after_auto_hdrp_fix_in_unity_2022_3_50f1.png)

**Figure 4:** Unity3D Lake Track Training Scene (ported over to HDRP with automated HDRP Fixes via HDRP Wizard)

- **TODO (JG Oct 22, 2024)**: We can see most of the materials have been successfully updated to HDRP materials. However with the trees, some are still pink as shown in **Figure 4**. So, we will have to do some manual updating for these materials to HDRP to be compatible.

### Launch Unity 3D SDC Simulator from Source

1\. To launch **sdc-simulator** project, make sure you downloaded and installed **Unity 3D 2022.3.50f1** from **[UnityHub](https://unity.com/download)** or your preferred method.

2\. Open **Unity Hub** after you've downloaded it.

3\. Click **Installs** tab, click **Install Editor**, and click **Install** for **Unity 3D 2022.3.50f1**.

4\. Click **Projects** tab, click **Add**, click **Add project from disk**, provide the location of our **sdc-simulator** of OpenSDC project and click **Add Project**:

~~~bash
# After clicking "Add project from disk", you can add "sdc-simulator" folder
apps/unity/sdc-simulator
~~~

- **NOTE**: After opening our **sdc-simulator** in **Unity Hub**, you can launch the **"Unity3D Lake Track Training Scene"** located on path `OpenSDC/apps/unity/sdc-simulator/Assets/Udacity_SDC_Assets/1_SelfDrivingCar/Scenes/LakeTrackTraining.unity`

- **NOTE**: After opening our **sdc-simulator** in **Unity Hub**, you can launch the **"Unity3D Jungle Track Training Scene"** located on path `OpenSDC/apps/unity/sdc-simulator/Assets/Udacity_SDC_Assets/1_SelfDrivingCar/Scenes/JungleTrackTraining.unity`

If you are interested in learning more about the Unity 3D Udacity SDC Assets that go into making the **Self-Driving Car Simulator**, you can learn more in [Unity 3D Udacity SDC Assets: README.md](./apps/unity/sdc-simulator/Assets/Udacity_SDC_Assets/README.md) where I have started documenting features of each of these assets.

### Udacity Unity 3D Pre-Built SDC Simulators

- For more information on Udacity's self-driving-car-sim, you can checkout our [Udacity Self-Driving Car Simulators Notes](docs/UDACITY_CARSIM.md) to see how to launch precompiled Unity Simulator builds

Heres a link to Udacity's **self-driving-car-sim public archive** for their source code for reference: https://github.com/udacity/self-driving-car-sim/tree/master

## Self-Driving Car Docker Image

For more information on building a docker image for deep learning self-driving car development environment, refer steps in [UDACITY_SDC_DOCKER.md](./docs/UDACITY_SDC_DOCKER.md)
