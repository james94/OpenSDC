# Udacity Self-Driving Car Assets

Initially, these Udacity Self-Driving Car (SDC) assets came from their Unity 3D 2020_3 project, but we migrated them over to Unity 3D 2022.3.50f1.

## Outline

- Unity Threading
- SocketIO

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

## Resources

- Perplexity.ai (AI assistant helping me with migrating Udacity's SDC simulator assets to our Unity 2022.3.50f1 HDRP SDC simulator project): https://www.perplexity.ai/search/you-are-a-software-simulation-Xh4OSupQQzaMOFc1tJBAaw