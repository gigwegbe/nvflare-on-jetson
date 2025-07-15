# Running Federated Learning on Jetson Devices with NVFLARE
This repository provides a step-by-step guide to deploying NVIDIA FLARE end-to-end on real hardware. Follow along to set up a central server and three NVIDIA Jetson client devices for federated learning in an edge environment.

This project goes beyond simulations, demonstrating how to securely connect your devices over a physical network and run federated training examples, while also providing solutions for common deployment challenges.





- Slide - [Link](https://docs.google.com/presentation/d/1Wgd5xcCyv9OtaZZSlBwdCtBbzTv0dXWNgOvunR0-BBI/edit?usp=sharing)


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







### Troubleshooting 


### References
- Provisioning 
-  