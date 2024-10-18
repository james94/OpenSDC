# Udacity Self-Driving Car Docker Notes

## Build SDC Starter GPU Docker Image

We will build the docker image:

~~~bash
cd OpenSDC/docker/ezaisdc/udacity-carnd-term1-starter

docker build -f Dockerfile.gpu -t udacity/carnd-term1-starter-kit-gpu .
~~~

- **NOTE**: this docker image was based on Udacity's SDC Starter Kit, but updated with a newer 12.4.1 Nvidia CUDA docker image, python 3.9.12, TensorFlow 2.17.0, OpenCV-Python 4.10.0.84, etc
- **NOTE**: I have used a similar docker image as the one we built for behavioral cloning, but the previous docker image had some older versions of the packages listed above

## Deploy SDC Starter GPU Docker Container

We launch docker container:

~~~bash
docker run -it --rm  --gpus all --entrypoint "/run.sh" -p 8888:8888 -v `pwd`:/src udacity/carnd-term1-starter-kit-gpu
~~~

Check we can access GPUs in TensorFlow Keras:

~~~bash
(carnd-term1-tf) root@07fb3cc13b63:/src# python
Python 3.9.12 (main, Jun  1 2022, 11:38:51)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2024-10-18 06:41:21.057415: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-10-18 06:41:21.068040: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-10-18 06:41:21.081092: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-10-18 06:41:21.085711: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-10-18 06:41:21.096250: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-10-18 06:41:21.658071: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
>>> tf.config.list_physical_devices("GPU")
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1729233722.680444     146 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729233722.709549     146 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729233722.709697     146 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
~~~

## Appendix

We can pull Udacity docker image:

~~~bash
docker pull udacity/carnd-term1-starter-kit
~~~

## Resources

Reference Udacity CarND-Term1-Starter-Kit: https://github.com/udacity/CarND-Term1-Starter-Kit
