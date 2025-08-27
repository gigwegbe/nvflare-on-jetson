## Running Federated Learning on Jetson Devices with NVFLARE
This repository provides a step-by-step guide to deploying NVIDIA FLARE end-to-end on real hardware. Follow along to set up a central server and three NVIDIA Jetson client devices for federated learning in an edge environment.

This project goes beyond simulations, demonstrating how to securely connect your devices over a physical network and run federated training examples, while also providing solutions for common deployment challenges.


- Slide - [Link](https://docs.google.com/presentation/d/1Wgd5xcCyv9OtaZZSlBwdCtBbzTv0dXWNgOvunR0-BBI/edit?usp=sharing)
- Poster - [Link](https://github.com/gigwegbe/nvflare-on-jetson/blob/main/assets/nvflare-poster-dli.pdf)
  
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
george@Georges-MacBook-Pro nvflare-on-jetson % nvflare provision -p jetson-project.yml -w ./prod_workspace
Project yaml file: /Users/george/Documents/github/nvflare-on-jetson/jetson-project.yml.
INFO: Generated results can be found under /Users/george/Documents/github/nvflare-on-jetson/./prod_workspace/jetson_fl_project/prod_00. 
```

Directory structure: 
```
george@Georges-MacBook-Pro prod_workspace % tree 
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
  george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/server1   george@jetson-nano-2g.local:/home/george/Documents
  ```
- site-1   -> Client1 
  ```
  george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-1   george@jetson-n2.local:/home/george/Documents
  ```
- site-2   -> Client2
  ```
  george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-2   george@jetson-n3.local:/home/george/Documents
  ```
- site-3   -> Client3 
  ```
  george@Georges-MacBook-Pro prod_workspace % scp -r  jetson_fl_project/prod_00/site-3   george@jetson-n4.local:/home/george/Documents
  ```
Note: The `admin@nvidia.com` maybe situated in the provisioning machine or server depending on device setup. 

<!-- ```
./copy_out_tls.sh
``` -->



### Admin 
In the admin machine create and activate the python 3.10 or higher virtual environment and install the dependencies in it. 
 ```
(env-admin) george@Georges-MacBook-Pro nvflare-on-jetson % pip install -r requirements.txt 
 ```

Make use you have update the ip address of the server(Check toubleshoot section for that).

Run the command below to connect to the server and use the login with the credential: 

```
(env-admin) george@Georges-MacBook-Pro prod_workspace % ./jetson_fl_project/prod_00/admin@nvidia.com/startup/fl_admin.sh
User Name: admin@nvidia.com
Trying to obtain server address
Obtained server address: server1:8003
Trying to login, please wait ...
Logged into server at server1:8003 with SSID: ebc6125d-0a56-4688-9b08-355fe9e4d61a
Type ? to list commands; type "? cmdName" to show usage of a command.
> 
```

### Server 
Do the above for the server too. 
```
(nvflare-env) george@jetson-nano-2g:~/Documents$ pip install -r requirements.txt
```

#### Enable Network connectivity on the server 
Ensure that ports 8002 (for client-server communication) and 8003 (for admin-server communication) are open for inbound connections on Server. 
```
sudo apt update
sudo apt install ufw
```
```
sudo ufw allow 8002/tcp
sudo ufw allow 8003/tcp
sudo ufw enable # if firewall is inactive
```

Verify the status of the firewall: 
```
(nvflare-env) george@jetson-nano-2g:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
8002/tcp                   ALLOW       Anywhere                  
8003/tcp                   ALLOW       Anywhere   
```
Noted: You might need to restart server. 

#### Start the server 

```
(nvflare-env) george@jetson-nano-2g:~/Documents/server1/startup$ ./start.sh 
(nvflare-env) george@jetson-nano-2g:~/Documents/server1/startup$ WORKSPACE set to /home/george/Documents/server1/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 8692
2025-07-16 23:42:11,420 - ServerDeployer - INFO - server heartbeat timeout set to 600
2025-07-16 23:42:12,190 - CoreCell - INFO - server: creating listener on grpc://0:8002
2025-07-16 23:42:12,776 - CoreCell - INFO - server: created backbone external listener for grpc://0:8002
2025-07-16 23:42:12,781 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:63449] is starting
2025-07-16 23:42:13,284 - CoreCell - INFO - server: created backbone internal listener for tcp://localhost:63449
2025-07-16 23:42:13,294 - conn_manager - INFO - Connector [CH00001 PASSIVE grpc://0:8002] is starting
2025-07-16 23:42:13,305 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-16 23:42:13,309 - FederatedServer - INFO - max_reg_duration=60.0
2025-07-16 23:42:13,312 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-16 23:42:13,315 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-16 23:42:13,319 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-16 23:42:13,352 - ObjectStreamer - INFO - registered processor_factory: channel='log_streaming' topic='*' _ChunkConsumerFactory
2025-07-16 23:42:13,359 - ServerDeployer - INFO - deployed FLARE Server.
2025-07-16 23:42:13,424 - Server - INFO - added secure port at 0.0.0.0:8002
2025-07-16 23:42:13,433 - hci - INFO - Starting Admin Server server1 on Port 8003
2025-07-16 23:42:13,433 - root - INFO - Server started
2025-07-16 23:42:13,816 - ServerState - INFO - Got the primary sp: server1 fl_port: 8002 SSID: ebc6125d-0a56-4688-9b08-355fe9e4d61a. Turning to hot.
```

### Clients 
Do the above for the clients too. 
```
(nvflare-env) george@jetson-n2:~/Documents$ pip install -r requirements-client.txt
```

```
(nvflare-env) george@jetson-n3:~/Documents$ pip install -r requirements-client.txt
```

```
(nvflare-env) george@jetson-n4:~/Documents$ pip install -r requirements-client.txt
```


```
(nvflare-env) george@jetson-n2:~/Documents$  site-1/startup/start.sh
(nvflare-env) george@jetson-n2:~/Documents$ WORKSPACE set to /home/george/Documents/site-1/startup/..
PYTHONPATH is /local/custom:
start fl because process of 31312 does not exist
new pid 31704
2025-07-17 00:14:51,125 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 00:14:51,141 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 00:14:51,159 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 00:14:51,164 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 00:14:51,166 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 00:14:51,276 - CoreCell - INFO - site-1: created backbone external connector to grpc://server1:8002
2025-07-17 00:14:51,281 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:35607] is starting
2025-07-17 00:14:51,669 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 00:14:51,784 - CoreCell - INFO - site-1: created backbone internal listener for tcp://localhost:35607
2025-07-17 00:14:51,802 - conn_manager - INFO - Connector [CH00001 ACTIVE grpc://server1:8002] is starting
2025-07-17 00:14:51,812 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-17 00:14:51,817 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-17 00:14:51,821 - FederatedClient - INFO - Wait for engine to be created.
2025-07-17 00:14:51,844 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 00:14:51,846 - conn_manager - INFO - Connection [CN00002 N/A => server1:8002] is created: PID: 31704
2025-07-17 00:14:52,661 - Authenticator - INFO - verified server identity 'server1'
2025-07-17 00:14:53,107 - Authenticator - INFO - Verified received token and signature successfully
2025-07-17 00:14:53,112 - FederatedClient - INFO - Successfully registered client:site-1 for project jetson_fl_project. Token:0b3bb022-6e66-451a-817a-13c83c3876ec SSID:ebc6125d-0a56-4688-9b08-355fe9e4d61a
2025-07-17 00:14:53,116 - FederatedClient - INFO - Got engine after 1.2956831455230713 seconds
2025-07-17 00:14:53,118 - FederatedClient - INFO - Got the new primary SP: grpc://server1:8002
```




### Troubleshooting Common Issues: 
This section will be updated with common problems encountered during real-world deployment and their solutions, covering:

### 1 ufw issues: 
Encountering involves the Uncomplicated Firewall (UFW) failing to enable due to a problem in the IPv6 rules. You can disable IPv6 in UFW if you're not using it. Open UFW config:
```
sudo nano /etc/default/ufw
```
Find the line:
```
IPV6=yes
```
Change it to:
```
IPV6=no
```
Save and exit, then reload UFW:
```
sudo ufw disable
sudo ufw enable

```

#### Admin unable to connect to server: 
```
(env-admin) george@Georges-MacBook-Pro prod_workspace % ./jetson_fl_project/prod_00/admin@nvidia.com/startup/fl_admin.sh   
User Name: admin@nvidia.com
Trying to obtain server address
Obtained server address: server1:8003
Trying to login, please wait ...
Trying to login, please wait ...
Trying to login, please wait ...
Trying to login, please wait ...
```

Add the line to `sudo nano /etc/hosts`:
```
192.168.1.64 server1   # Add the ip-address of the server-1
```
### Client unable to connect to server: 
```
(nvflare-env) george@jetson-n2:~/Documents$ WORKSPACE set to /home/george/Documents/site-1/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 31036
2025-07-17 00:05:54,821 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 00:05:54,823 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 00:05:54,825 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 00:05:54,827 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 00:05:54,829 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 00:05:55,220 - CoreCell - INFO - site-1: created backbone external connector to grpc://server1:8002
2025-07-17 00:05:55,226 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:10711] is starting
2025-07-17 00:05:55,331 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 00:05:55,729 - CoreCell - INFO - site-1: created backbone internal listener for tcp://localhost:10711
2025-07-17 00:05:55,774 - conn_manager - INFO - Connector [CH00001 ACTIVE grpc://server1:8002] is starting
2025-07-17 00:05:55,784 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-17 00:05:55,793 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-17 00:05:55,797 - FederatedClient - INFO - Wait for engine to be created.
2025-07-17 00:05:55,844 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 00:05:55,849 - conn_manager - INFO - Connection [CN00002 N/A => server1:8002] is created: PID: 31036
2025-07-17 00:05:55,857 - conn_manager - INFO - Connection [CN00002 Not Connected] is closed PID: 31036
2025-07-17 00:05:55,859 - GrpcDriver - INFO - CLIENT: finished connection [CN00002 Not Connected]
2025-07-17 00:05:55,994 - Authenticator - INFO - re-challenge after 2.0 seconds
2025-07-17 00:05:56,873 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 00:05:56,878 - conn_manager - INFO - Connection [CN00003 N/A => server1:8002] is created: PID: 31036
2025-07-17 00:05:56,885 - conn_manager - INFO - Connection [CN00003 Not Connected] is closed PID: 31036
2025-07-17 00:05:56,886 - GrpcDriver - INFO - CLIENT: finished connection [CN00003 Not Connected]
2025-07-17 00:05:58,006 - Authenticator - INFO - re-challenge after 2.0 seconds
2025-07-17 00:05:58,901 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 00:05:58,908 - conn_manager - INFO - Connection [CN00004 N/A => server1:8002] is created: PID: 31036
2025-07-17 00:05:58,919 - conn_manager - INFO - Connection [CN00004 Not Connected] is closed PID: 31036
2025-07-17 00:05:58,923 - GrpcDriver - INFO - CLIENT: finished connection [CN00004 Not Connected]
```

Kill the process run the `stop_fl.sh` script: 
```
(nvflare-env) george@jetson-n3:~/Documents/site-2/startup$ ./stop_fl.sh 
```
Add the line to `sudo nano /etc/hosts`:
```
192.168.1.64 server1   # Add the ip-address of the server-1
```
### References
- [Provisioning in NVIDIA FLARE](https://nvflare.readthedocs.io/en/2.6.0/programming_guide/provisioning_system.html)
- [Operating NVFLARE - Admin Client, Commands, FLARE API](https://nvflare.readthedocs.io/en/2.6.0/real_world_fl/operation.html)
- [Experimenting with Novel Distributed Applications Using NVIDIA Flare 2.1](https://developer.nvidia.com/blog/experimenting-with-novel-distributed-applications-using-nvidia-flare-2-1)
- [NVFLARE Overview](https://nvflare.readthedocs.io/en/2.1.0/user_guide/overview.html)