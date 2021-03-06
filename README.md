# CUDAKalmanFilter

### Table of Contents
**[Getting Started](#getting-started)**<br>
**[Prerequisites](#prerequisites)**<br>
**[Installation Instructions](#installation-instructions)**<br>

## Getting Started

write something about how gpu's have more threads compared to cpu's and how this advantage can accelerate the processing time of complex multi-dimensional arrays. 
write something briefly about what KF is.

For now, I would like to explore the possibilities of deploying multiple instances of Kalman Filtering for a groupd of simulated signals. With KF tracking multiple signals simultaneously, it should show the benfits of using GPU rather than CPU, given the intensity of array calculations.

## Prerequisites

Before getting started with CUDA, make sure your graphics card is [CUDA-capable](https://developer.nvidia.com/cuda-gpus). If your machine's GPU is listed, your card is CUDA-capable.

## Installation Instructions

At the time of my initial installtion, [CUDA 10.0](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=debnetwork) was the most recent version. Make sure to choose the right operating system, distro and version if using Linux, and installer type of your choice. I downloaded deb(network) file and used the following commends:
```
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```
After installation is complete, add CUDA to your PATH in .bashrc file. (Also note that I am using version 10.0 here)
```
export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda-10.0
```
Then reboot your system to finish the installation, and check the version of your installation:

`nvcc --version`

Finally, run `gpu_example.py` python program to test your installation which is in [test](https://github.com/0b10010010/CUDAKalmanFilter/blob/master/test) folder to compare the performance between your CPU and GPU.
<sup>&dagger;: This code was acquired from NVIDIA's [webpage](https://developer.nvidia.com/how-to-cuda-python).</sup><br>

My machine's performance comparison with gpu_example.py:
```console
alexk@AW15R2:~/Desktop/KSU_ME/CUDAKalmanFilter/test$ python gpu_example.py
VectorAdd_CPU took 8.951272 seconds
VectorAdd_GPU took 0.283154 seconds
```

For any trouble shooting or more information, this detailed [documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) might be helpful with installing CUDA on your machine.
