## Building pytorch from scatch

#Installing PyTorch 
https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048

git clone --recursive --branch v1.10.0  http://github.com/pytorch/pytorch


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