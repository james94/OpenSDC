# Udacity Self-Driving Car Assets

Initially, these Udacity Self-Driving Car (SDC) assets came from their Unity 3D 2020_3 project, but we migrated them over to Unity 3D 2022.3.50f1.

## Outline

- Unity Threading
- SocketIO
- Unity SimpleFileBrowser
- Editor (JetBrains Rider IDE)
- Unity Standard Assets
- Unity Editor Image Effects Integration

## Unity Threading

Key components of **Unity Main Thread Dispatcher**:

- **Queue of Actions**
    - Static queue stores actions that will be executed on the main thread.

- **Update Method**
    - Runs every frame and executes all queued actions.

- **Enqueue Methods**
    - There are two enqueue methods (for **IEnumerators** and **actions**) that add actions to the queue for execution on the main thread.

- **Singleton Pattern**
    - Ensures only one instance of the **UnityMainThreadDispatcher** exists.

- **Usage in Self-Driving Car Simulation**
    - 1\. Process sensor data on background threads
    - 2\. Update UI elements with simulation results
    - 3\. Apply physics calculations from background threads

## SocketIO

- **Real-Time Bidirectional Communication**
- **Event-Based Architecture**
- **JSON Serialization**
- **Reconnection Handling**
- **Room & Namespace Support**
- **Cross-Platform Compatibility**
- **Asynchronous Operations**
- **Custom Event Handling**
- **Usage in Self-Driving Car Simulation**
    - Send real-time sensor data from our simulated car to an external AI system for processing
    - Receive control commands from an external system to guide the car's behavior
    - Synchronize multiple instances of the simulation for multi-car scenarios
    - Stream environmental data (traffic, weather conditions) from a server to your Unity simulation

The SocketIO Unity3D asset plugin that Udacity used in their SDC simulator is deprecated and here is the link to SocketIO github:

- unity-socket.io-DEPRECATED
: https://github.com/fpanettieri/unity-socket.io-DEPRECATED

Since we are using Unity 2022.3.50f1 with HDRP for our SDC simulator, we will want to look at a more current SocketIO implementation, which can be found at this repo link:

- SocketIOUnity: https://github.com/itisnajim/SocketIOUnity

NOTE: We can look at switching the **DEPRECATED SocketIO** with the more recent **SocketIOUnity** plugin.

NOTE: We maybe able to switch the **DEPRECATED SocketIO** with **GRPC** and/or real-time PubSub tool (FastDDS, ZeroMQ, etc)

### Transition from SocketIO to GRPC

- grpc-dotnet-unity: https://github.com/doctorseus/grpc-dotnet-unity

- mr-grpc-unity: https://github.com/OpenAvikom/mr-grpc-unity

- ml-agents-grpc
: https://github.com/Unity-Technologies/ml-agents-grpc

### Transition from SocketIO to Real-Time PubSub

- dds-unity: https://github.com/pleonex/dds-unity

- RTI Connext DDS, Use Cases, Unity: https://github.com/rticommunity/rticonnextdds-usecases-unity

    - Gaming Visualizations with RTI Connext and Unity® Integration: https://www.rti.com/developers/case-code/unity-gaming

- unity-zeromq-client
: https://github.com/gench23/unity-zeromq-client

    - netmq: https://github.com/zeromq/netmq

- Unity-ZeroMQ-Example: https://github.com/valkjsaaa/Unity-ZeroMQ-Example

## Unity SimpleFileBrowser

Here are some key features of UnitySimpleFileBrowser:

- **Cross-Platform File Browsing**
- **File and Folder Selection**
- **Save File Functionality**
- **Custom File Filters**
- **Asynchronous Operation**
- **Quick Links**
- **Search Functionality**
- **Customizable UI**

## Editor (JetBrains Rider IDE)

Rider Unity Integration is designed to integrate JetBrains Rider IDE with Unity. Here are the three main classes:

- 1\. Rider Class
- 2\. User32Dll Class
- 3\. RiderAssetPostprocessor Class

## Unity Standard Assets

### Cameras

- **FreeLookCam**: Useful for creating a dynamic camera that can orbit around a target, which could be used to observe the self-driving car from different angles.

- **MultipurposeCameraRig**: Provides a versatile camera setup that can be adapted for various viewing needs in your simulation.

### Characters

- **ThirdPersonCharacter**: While not directly applicable to a car, this could be useful for pedestrian simulations in our environment.

### Cross Platform Input

- This system can be helpful in the case you plan to make your simulation accessible across different platforms, allowing for consistent input handling.

### Effects

- **ParticleSystems**: Can be used to simulate environmental effects like dust, smoke, or rain, which are crucial for realistic self-driving scenarios.
- **WaterEffects**: Useful for simulating wet road conditions or water hazards.

### Environment

- **TerrainAssets**: These can be used to quickly create varied terrains for your driving scenarios
- **Water**: For simulating water bodies that the self-driving car might encounter

### Utility

- **AutoMobileShaderSwitch**: Helps optimize shaders for mobile platforms if you plan to run simulations on mobile devices
- **FOVKick**: Could be used to simulate camera effects during acceleration or collision events
- **TimedObjectDestructor**: Useful for managing temporary objects in your simulation, like traffic or weather effects

### Vehicles

- **Car**: A basic car controller with physics based movement
- **CarAudio**: Provides realistic car sound effects
- **CarUserControl**: Allows for user input to control the car, which could be adapted for AI control
- **Mudguard**: Adds visual effects for wheel interction with the ground.
- **WheelEffects**: Simulates visual effects of wheels on different surfaces.

### Transition Standard Assets to Unity 2022.3.50f1

For Unity "**Standard Assets**", I referenced a few github repos as well as Udacity's Unity "Standard Assets":

- Udacity's **self-driving-car-sim** Standard Assets: https://github.com/udacity/self-driving-car-sim/tree/master/Assets/Standard%20Assets

- Unity-Standard-Assets-2022_LTS-usage: https://github.com/deathwatchgaming/Unity-Standard-Assets-2022_LTS-usage

- Unity-StandardAssets-2020: https://github.com/ImLp/Unity-StandardAssets-2020

- https://github.com/supinzhen/Unity-Standard-Assets-2018.4

**NOTE**: through my research, I have found these Unity "**Standard Assets**" are deprecated and I think have been replaced with features that now come with Unity when you create a new project. However, I am keeping them for now since Udacity uses them in their **self-driving-car-sim** github repo and we are trying to migrate **Standard Assets** over to our OpenSDC's **sdc-simulator** powered by **High Definition Rendering Pipeline (HDRP)**.

## Unity Editor Image Effects Integration

There are multiple image effects that we can configure and this Unity **apps/unity/sdc-simulator/Assets/Udacity_SDC_Assets/Editor/** asset folder
contains **ImageEffects** asset that comes with Unity Editor Inspector integration for each image effect.

- Antialiasing Editor
- BloomAndFlares Editor
- ...
- VignetteAndChromaticAberration

Check out more [ImageEffects Unity Editor Inspector Integrated Assets](./Editor/ImageEffects)

## Resources

- Perplexity.ai (AI assistant helping me with migrating Udacity's SDC simulator assets to our Unity 2022.3.50f1 HDRP SDC simulator project): https://www.perplexity.ai/search/you-are-a-software-simulation-Xh4OSupQQzaMOFc1tJBAaw