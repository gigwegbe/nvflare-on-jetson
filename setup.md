- Update the renewly flashed SD card:
```
sudo apt-get update
```

- Download Python 3.11 source:
```
sudo wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz
sudo tar xzf Python-3.10.14.tgz
cd Python-3.10.14
```

- Build and Install: 
```
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall
```

- Create virtual environment: 
```
python3.10 -m venv nvflare-env
```

- Activate the virtual environment: 
```
 source myenv/bin/activate
```

Other installations: 
```
pip install --upgrade pip setuptools wheel
pip install numpy
pip install Pillow==10.4.0
pip install gdown 
gdown --id 1lMSZu_hARJDpfZuJHc64Hb3OXntlRO-- -O torch-1.7.0a0-cp38-cp38-linux_aarch64.whl
pip install torch-1.7.0a0-cp38-cp38-linux_aarch64.whl
sudo apt install libopenmpi-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libopenblas-base libopenblas-dev
```

- Test Pytorch 
```
(myenv) george@george-desktop:~$ python
Python 3.8.0 (default, Dec  9 2021, 17:53:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> 
```

- Install Torchvision 
```
git clone --branch v0.8.1 https://github.com/pytorch/vision.git
cd vision 
python setup.py install
```

- Install Nvflare: 
```
pip install nvflare 
```