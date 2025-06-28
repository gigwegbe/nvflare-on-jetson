## Building pytorch from scatch

#Installing PyTorch 
- https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048
- https://i7y.org/en/pytorch-build-on-jetson-nano/

git clone --recursive --branch v1.10.0  http://github.com/pytorch/pytorch

### Apply patch 
```
patch -p1 < pytorch-patch.patch
```
### Installing TorchVision 
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048/15



### Build swap file (4GB)
```
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Check swap file 
```
free -h
```

### Enviroment variables 
``` 
export USE_NCCL=0
export USE_DISTRIBUTED=1      
export USE_QNNPACK=0
export USE_PYTORCH_QNNPACK=0
export TORCH_CUDA_ARCH_LIST="5.3;6.2;7.2" 
export PYTORCH_BUILD_NUMBER=1.10.0
```

