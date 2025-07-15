## Running Federated Learning on Jetson Devices with NVFLARE
This repository provides a step-by-step guide to deploying NVIDIA FLARE end-to-end on real hardware. Follow along to set up a central server and three NVIDIA Jetson client devices for federated learning in an edge environment.

This project goes beyond simulations, demonstrating how to securely connect your devices over a physical network and run federated training examples, while also providing solutions for common deployment challenges.


- Slide - [Link](https://docs.google.com/presentation/d/1Wgd5xcCyv9OtaZZSlBwdCtBbzTv0dXWNgOvunR0-BBI/edit?usp=sharing)


### Getting Started 
This section will guide you through setting up your environment and deploying the NVFLARE system. 

#### Prerequisites
Before you begin, ensure you have:

- Four Physical Machines:

    - 1 x Server Machine (e.g., a desktop PC, cloud instance)

    - 3 x NVIDIA Jetson Client Devices (e.g., Jetson Nano, Xavier NX, Orin Nano)

- Operating System: Ubuntu LTS recommended on all machines.


- Network Connectivity: All four machines must be able to communicate with each other over a network (e.g., Wi-Fi, Ethernet).

- Basic NVFLARE Knowledge: Familiarity with NVIDIA FLARE concepts is beneficial - [Paper](https://arxiv.org/pdf/2210.13291) 
  
### Provisioning
```
nvflare provision -p my_project.yml -w ./prod_workspace
```

#### Distribute Credentials
```
./copy_out_tls.sh
```


### Admin 


### Server 


### Clients 







### Troubleshooting Common Issues
This section will be updated with common problems encountered during real-world deployment and their solutions, covering:

### References
- Provisioning 
-  