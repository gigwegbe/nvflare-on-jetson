## Running Federated Learning on Jetson Devices with NVFLARE
This repository provides a step-by-step guide to deploying NVIDIA FLARE end-to-end on real hardware. Follow along to set up a central server and three NVIDIA Jetson client devices for federated learning in an edge environment.

This project goes beyond simulations, demonstrating how to securely connect your devices over a physical network and run federated training examples, while also providing solutions for common deployment challenges.


- Slide - [Link](https://docs.google.com/presentation/d/1Wgd5xcCyv9OtaZZSlBwdCtBbzTv0dXWNgOvunR0-BBI/edit?usp=sharing)


### Getting Started 
This section will guide you through setting up your environment and deploying the NVFLARE system. 

#### Prerequisites
Before you begin, ensure you have:

- Four Physical Machines:

    - 1 x Server Machine ( Jetson Nano 2GB)

    - 3 x NVIDIA Jetson Client Devices (Jetson Nano 4GB)

- Operating System: Ubuntu LTS recommended on all machines.


- Network Connectivity: All four machines must be able to communicate with each other over a network (e.g., Wi-Fi, Ethernet).

- Basic NVFLARE Knowledge: Familiarity with NVIDIA FLARE concepts is beneficial - [Paper](https://arxiv.org/pdf/2210.13291) 
  
### Provisioning
Depending on the number of devices to be provisioned update the ip-address of the devices in the `jetson-project.yml` file. 
```
nvflare provision -p jetson-project.yml -w ./prod_workspace
```

Output: 
```
(env-admin) george@Georges-MacBook-Pro nvflare-on-jetson % nvflare provision -p jetson-project.yml -w ./prod_workspace
Project yaml file: /Users/george/Documents/github/nvflare-on-jetson/jetson-project.yml.
INFO: Generated results can be found under /Users/george/Documents/github/nvflare-on-jetson/./prod_workspace/jetson_fl_project/prod_00. 
```

Directory structure: 
```
(env-admin) george@Georges-MacBook-Pro prod_workspace % tree 
.
└── jetson_fl_project
    ├── prod_00
    │   ├── admin@nvidia.com
    │   │   ├── local
    │   │   ├── startup
    │   │   │   ├── client.crt
    │   │   │   ├── client.key
    │   │   │   ├── fed_admin.json
    │   │   │   ├── fl_admin.sh
    │   │   │   ├── readme.txt
    │   │   │   ├── rootCA.pem
    │   │   │   ├── signature.json
    │   │   │   └── system_info.ipynb
    │   │   └── transfer
    │   ├── server1
    │   │   ├── local
    │   │   │   ├── authorization.json.default
    │   │   │   ├── log_config.json.default
    │   │   │   ├── privacy.json.sample
    │   │   │   └── resources.json.default
    │   │   ├── readme.txt
    │   │   ├── startup
    │   │   │   ├── fed_server.json
    │   │   │   ├── rootCA.pem
    │   │   │   ├── server.crt
    │   │   │   ├── server.key
    │   │   │   ├── signature.json
    │   │   │   ├── start.sh
    │   │   │   ├── stop_fl.sh
    │   │   │   └── sub_start.sh
    │   │   └── transfer
    │   ├── site-1
    │   │   ├── local
    │   │   │   ├── authorization.json.default
    │   │   │   ├── log_config.json.default
    │   │   │   ├── privacy.json.sample
    │   │   │   └── resources.json.default
    │   │   ├── readme.txt
    │   │   ├── startup
    │   │   │   ├── client.crt
    │   │   │   ├── client.key
    │   │   │   ├── fed_client.json
    │   │   │   ├── rootCA.pem
    │   │   │   ├── signature.json
    │   │   │   ├── start.sh
    │   │   │   ├── stop_fl.sh
    │   │   │   └── sub_start.sh
    │   │   └── transfer
    │   ├── site-2
    │   │   ├── local
    │   │   │   ├── authorization.json.default
    │   │   │   ├── log_config.json.default
    │   │   │   ├── privacy.json.sample
    │   │   │   └── resources.json.default
    │   │   ├── readme.txt
    │   │   ├── startup
    │   │   │   ├── client.crt
    │   │   │   ├── client.key
    │   │   │   ├── fed_client.json
    │   │   │   ├── rootCA.pem
    │   │   │   ├── signature.json
    │   │   │   ├── start.sh
    │   │   │   ├── stop_fl.sh
    │   │   │   └── sub_start.sh
    │   │   └── transfer
    │   ├── site-3
    │   │   ├── local
    │   │   │   ├── authorization.json.default
    │   │   │   ├── log_config.json.default
    │   │   │   ├── privacy.json.sample
    │   │   │   └── resources.json.default
    │   │   ├── readme.txt
    │   │   ├── startup
    │   │   │   ├── client.crt
    │   │   │   ├── client.key
    │   │   │   ├── fed_client.json
    │   │   │   ├── rootCA.pem
    │   │   │   ├── signature.json
    │   │   │   ├── start.sh
    │   │   │   ├── stop_fl.sh
    │   │   │   └── sub_start.sh
    │   │   └── transfer
    │   └── start_all.sh
    └── state
        └── cert.json
```

#### Distribute Credentials
Copy each site to their respective devices: 
- server1 -> Server 
  ```
  (env-admin) george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/server1   george@jetson-nano-2g.local:/home/george/Documents
  ```
- site-1   -> Client1 
  ```
  (env-admin) george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-1   george@jetson-n2.local:/home/george/Documents
  ```
- site-2   -> Client2
  ```
  (env-admin) george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-2   george@jetson-n3.local:/home/george/Documents
  ```
- site-3   -> Client3 
  ```
  (env-admin) george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-3   george@jetson-n4.local:/home/george/Documents
  ```
Note: The `admin@nvidia.com` maybe situated in the provisioning machine or server depending on device setup. 

<!-- ```
./copy_out_tls.sh
``` -->



### Admin 


### Server 


### Clients 







### Troubleshooting Common Issues
This section will be updated with common problems encountered during real-world deployment and their solutions, covering:

### References
- [Provisioning in NVIDIA FLARE](https://nvflare.readthedocs.io/en/2.6.0/programming_guide/provisioning_system.html)
- [Operating NVFLARE - Admin Client, Commands, FLARE API](https://nvflare.readthedocs.io/en/2.6.0/real_world_fl/operation.html)