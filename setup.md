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

- Verify Python 3.10 Installation: 
```
python3.10 --version

```

- Create virtual environment: 
```
python3.10 -m venv nvflare-env
```

- Activate the virtual environment: 
```
 source nvflare-env/bin/activate
```

Other installations: 
```
sudo apt install libomp-dev
sudo apt install libopenmpi-dev
sudo apt install -y libssl-dev zlib1g-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libopenblas-base libopenblas-dev
```
```
sudo apt update
sudo apt install -y \
  build-essential \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  libffi-dev \
  liblzma-dev \
  libgdbm-dev \
  libncursesw5-dev \
  libdb-dev \
  tk-dev \
  uuid-dev \
  libnss3-dev \
  libgpm-dev \
  libncurses5-dev \
  libexpat1-dev
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


- Install Nvflare: 
```
pip install nvflare 
```

```
(nvflare-env) george@jetson-n4:~/NVFlare/examples/hello-world/hello-pt$ python3 fedavg_script_runner_pt.py 
Traceback (most recent call last):
  File "/home/george/NVFlare/examples/hello-world/hello-pt/fedavg_script_runner_pt.py", line 17, in <module>
    from nvflare.app_opt.pt.job_config.fed_avg import FedAvgJob
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/pt/job_config/fed_avg.py", line 20, in <module>
    from nvflare.app_opt.pt.job_config.base_fed_job import BaseFedJob
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/pt/job_config/base_fed_job.py", line 27, in <module>
    from nvflare.app_opt.tracking.tb.tb_receiver import TBAnalyticsReceiver
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/tracking/tb/tb_receiver.py", line 18, in <module>
    from torch.utils.tensorboard import SummaryWriter
  File "/home/george/nvflare-env/lib/python3.10/site-packages/torch/utils/tensorboard/__init__.py", line 4, in <module>
    LooseVersion = distutils.version.LooseVersion
AttributeError: module 'distutils' has no attribute 'version'



(nvflare-env) george@jetson-nano-2g:~/Desktop/NVFlare/examples/hello-world/hello-pt$ python3 fedavg_script_runner_pt.py 
Traceback (most recent call last):
  File "/home/george/Desktop/NVFlare/examples/hello-world/hello-pt/fedavg_script_runner_pt.py", line 17, in <module>
    from nvflare.app_opt.pt.job_config.fed_avg import FedAvgJob
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/pt/job_config/fed_avg.py", line 20, in <module>
    from nvflare.app_opt.pt.job_config.base_fed_job import BaseFedJob
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/pt/job_config/base_fed_job.py", line 27, in <module>
    from nvflare.app_opt.tracking.tb.tb_receiver import TBAnalyticsReceiver
  File "/home/george/nvflare-env/lib/python3.10/site-packages/nvflare/app_opt/tracking/tb/tb_receiver.py", line 18, in <module>
    from torch.utils.tensorboard import SummaryWriter
  File "/home/george/nvflare-env/lib/python3.10/site-packages/torch/utils/tensorboard/__init__.py", line 4, in <module>
    LooseVersion = distutils.version.LooseVersion
AttributeError: module 'distutils' has no attribute 'version'
```
- Line 200
```
       # Arg-check dataset related before checking samplers because we want to
        # tell users that iterable-style datasets are incompatible with custom
        # samplers first, so that they don't learn that this combo doesn't work
        # after spending time fixing the custom sampler errors.
        if isinstance(dataset, IterableDataset):
            self._dataset_kind = _DatasetKind.Iterable
            # NOTE [ Custom Samplers and IterableDataset ]
            #
            # `IterableDataset` does not support custom `batch_sampler` or
            # `sampler` since the key is irrelevant (unless we support
            # generator-style dataset one day...).

```


```
        # Arg-check dataset related before checking samplers because we want to
        # tell users that iterable-style datasets are incompatible with custom
        # samplers first, so that they don't learn that this combo doesn't work
        # after spending time fixing the custom sampler errors.
        if hasattr(dataset, "__iter__") and not hasattr(dataset, "__len__"):
        #if isinstance(dataset, IterableDataset):
            self._dataset_kind = _DatasetKind.Iterable
            # NOTE [ Custom Samplers and IterableDataset ]
            #
            # `IterableDataset` does not support custom `batch_sampler` or
            # `sampler` since the key is irrelevant (unless we support
            # generator-style dataset one day...).
```


```
git clone https://github.com/NVIDIA/NVFlare.git
```


```
(nvflare-env) george@jetson-nano-2g:~/Desktop/NVFlare/examples/hello-world/hello-pt$ python3 fedavg_script_runner_pt.py 
Adding convert_to_fed_event to client
Adding convert_to_fed_event to client
2025-07-08 04:41:57,636 - IntimeModelSelector - INFO - model selection weights control: {}
2025-07-08 04:41:59,770 - TBAnalyticsReceiver - INFO - Tensorboard records can be found in /tmp/nvflare/jobs/workdir/server/simulate_job/tb_events you can view it using `tensorboard --logdir=/tmp/nvflare/jobs/workdir/server/simulate_job/tb_events`
2025-07-08 04:41:59,774 - FedAvg - INFO - Initializing BaseModelController workflow.
2025-07-08 04:41:59,778 - FedAvg - INFO - Beginning model controller run.
2025-07-08 04:41:59,779 - FedAvg - INFO - Start FedAvg.
2025-07-08 04:41:59,781 - FedAvg - INFO - loading initial model from persistor
2025-07-08 04:41:59,782 - PTFileModelPersistor - INFO - Both source_ckpt_file_full_name and ckpt_preload_path are not provided. Using the default model weights initialized on the persistor side.
2025-07-08 04:41:59,785 - FedAvg - INFO - Round 0 started.
2025-07-08 04:41:59,786 - FedAvg - INFO - Sampled clients: ['site-1', 'site-2']
2025-07-08 04:41:59,788 - FedAvg - INFO - Sending task train to ['site-1', 'site-2']
2025-07-08 04:42:06,889 - TaskScriptRunner - INFO - start task run() with full path: /tmp/nvflare/jobs/workdir/site-1/simulate_job/app_site-1/custom/src/hello-pt_cifar10_fl.py
2025-07-08 04:42:06,920 - TaskScriptRunner - INFO - start task run() with full path: /tmp/nvflare/jobs/workdir/site-2/simulate_job/app_site-2/custom/src/hello-pt_cifar10_fl.py
2025-07-08 04:42:06,942 - PTInProcessClientAPIExecutor - INFO - execute for task (train)
2025-07-08 04:42:06,949 - PTInProcessClientAPIExecutor - INFO - send data to peer
2025-07-08 04:42:06,953 - PTInProcessClientAPIExecutor - INFO - sending payload to peer
2025-07-08 04:42:06,960 - PTInProcessClientAPIExecutor - INFO - Waiting for result from peer
2025-07-08 04:42:06,972 - PTInProcessClientAPIExecutor - INFO - execute for task (train)
2025-07-08 04:42:06,979 - PTInProcessClientAPIExecutor - INFO - send data to peer
2025-07-08 04:42:06,984 - PTInProcessClientAPIExecutor - INFO - sending payload to peer
2025-07-08 04:42:06,990 - PTInProcessClientAPIExecutor - INFO - Waiting for result from peer
2025-07-08 04:42:08,772 - TaskScriptRunner - INFO - Files already downloaded and verified
2025-07-08 04:42:09,148 - TaskScriptRunner - INFO - Files already downloaded and verified
2025-07-08 04:42:10,507 - TaskScriptRunner - INFO - current_round=0
2025-07-08 04:42:14,321 - TaskScriptRunner - INFO - current_round=0
2025-07-08 04:48:17,082 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 0, Loss: 0.0001877482533454895
2025-07-08 04:48:17,097 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 0, Loss: 0.0001888811190923055
2025-07-08 04:49:52,822 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 3000, Loss: 0.5116449602991342
2025-07-08 04:50:05,570 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 3000, Loss: 0.5088813133984804
2025-07-08 04:50:54,118 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 6000, Loss: 0.487222075338165
2025-07-08 04:51:09,419 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 6000, Loss: 0.4869432836075624
2025-07-08 04:51:54,524 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 9000, Loss: 0.4873730070590973
2025-07-08 04:52:14,893 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 9000, Loss: 0.48527060945828754
2025-07-08 04:52:58,282 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 12000, Loss: 0.48672460558017094
2025-07-08 04:53:11,924 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 0, Loss: 0.00015197251240412393
2025-07-08 04:53:21,538 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 12000, Loss: 0.485289328550299
2025-07-08 04:53:32,637 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 0, Loss: 0.00013955562313397725
2025-07-08 04:54:18,091 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 3000, Loss: 0.48854459516704085
2025-07-08 04:54:36,195 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 3000, Loss: 0.49119863538692393
2025-07-08 04:55:22,662 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 6000, Loss: 0.49486620659132796
2025-07-08 04:55:42,018 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 6000, Loss: 0.493706921984752
2025-07-08 04:56:25,965 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 9000, Loss: 0.492066622659564
2025-07-08 04:56:46,870 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 9000, Loss: 0.4884060854663452
2025-07-08 04:57:32,366 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 12000, Loss: 0.49343871090312796
2025-07-08 04:57:43,739 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 0, Loss: 0.00013262978196144104
2025-07-08 04:57:55,930 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 12000, Loss: 0.49618857439359026
2025-07-08 04:58:09,407 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 0, Loss: 0.0001458761195341746
2025-07-08 04:58:51,334 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 3000, Loss: 0.4957287537058194
2025-07-08 04:59:14,202 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 3000, Loss: 0.5000829518089692
2025-07-08 05:00:03,934 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 6000, Loss: 0.49299873840808867
2025-07-08 05:00:23,769 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 6000, Loss: 0.5005329737638434
2025-07-08 05:01:09,981 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 9000, Loss: 0.5010821553766728
2025-07-08 05:01:28,454 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 9000, Loss: 0.5122630733400583
2025-07-08 05:02:18,029 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 12000, Loss: 0.4965154392222563
2025-07-08 05:03:05,813 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 0, Loss: 0.0002070971727371216
2025-07-08 05:03:23,283 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 12000, Loss: 0.5001176288674275
2025-07-08 05:03:34,006 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 0, Loss: 0.00018594239155451456
2025-07-08 05:04:19,907 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 3000, Loss: 0.4984336083481709
2025-07-08 05:04:38,514 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 3000, Loss: 0.513949430535237
2025-07-08 05:05:26,096 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 6000, Loss: 0.5196638933966558
2025-07-08 05:05:47,248 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 6000, Loss: 0.5057245024542014
2025-07-08 05:06:34,637 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 9000, Loss: 0.5024643106609583
2025-07-08 05:06:55,421 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 9000, Loss: 0.5056450599431992
2025-07-08 05:07:45,787 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 12000, Loss: 0.5052566191752752
2025-07-08 05:07:56,691 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 0, Loss: 0.00014303019642829894
2025-07-08 05:08:07,585 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 12000, Loss: 0.5075500449091196
2025-07-08 05:08:36,480 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 0, Loss: 0.00014496246973673502
2025-07-08 05:09:48,871 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 3000, Loss: 0.5183022035360336
2025-07-08 05:10:09,090 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 3000, Loss: 0.511626027772824
2025-07-08 05:10:55,735 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 6000, Loss: 0.5063521952976783
2025-07-08 05:11:16,761 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 6000, Loss: 0.5217132466882467
2025-07-08 05:12:02,879 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 9000, Loss: 0.515636206338803
2025-07-08 05:12:23,488 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 9000, Loss: 0.5191753000368674
2025-07-08 05:13:12,584 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 12000, Loss: 0.5212670568724473
2025-07-08 05:13:25,440 - TaskScriptRunner - INFO - Finished Training
```