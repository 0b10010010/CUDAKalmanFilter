# CUDAKalmanFilter

### Table of Contents
**[Getting Started](#getting-started)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Installation Instructions](#installation-instructions)**<br>

## Getting Started
writed something briefly about what KF is.

## Prerequisites

Before getting started with CUDA, make sure your graphics card is [CUDA-capable](https://developer.nvidia.com/cuda-gpus). If your machine's GPU is listed, your card is CUDA-capable.

## Installation Instructions

At the time of my initial installtion, [CUDA 10.0](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal) was the most recent version. Make sure to choose the right operating system, distro and version if using Linux, and installer type of your choice. I downloaded deb(local) file and used the following commends:
```
sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```

For any trouble shooting or more information, this detailed [documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) might be helpful with installing CUDA on your machine.

After you have successfully installed CUDA, run gpu_example.py python program to test your installation.
This code was acquired from NVIDIA's [webpage](https://developer.nvidia.com/how-to-cuda-python).
