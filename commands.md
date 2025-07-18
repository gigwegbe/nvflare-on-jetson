```
> check_status client
----------------------------------------
| CLIENT | APP_NAME | JOB_ID | STATUS  |
----------------------------------------
| site-2 | ?        | ?      | No Jobs |
| site-1 | ?        | ?      | No Jobs |
| site-3 | ?        | ?      | No Jobs |
----------------------------------------
Done [132944 usecs] 2025-07-17 01:01:39.090863
> check_status client site-1
----------------------------------------
| CLIENT | APP_NAME | JOB_ID | STATUS  |
----------------------------------------
| site-1 | ?        | ?      | No Jobs |
----------------------------------------
Done [117793 usecs] 2025-07-17 01:01:52.698478
> list_jobs
No jobs found.
Done [78593 usecs] 2025-07-17 01:02:02.505810
> pwd site-1
/home/george/Documents/site-1
Done [143167 usecs] 2025-07-17 01:02:23.452714
> sys_info server
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 2076119040 |
| available         | 1575735296 |
| percent           | 24.1       |
| used              | 384851968  |
| free              | 1020563456 |
| active            | 433651712  |
| inactive          | 442834944  |
| buffers           | 38092800   |
| cached            | 632610816  |
| shared            | 29868032   |
| slab              | 103759872  |
| available_percent | 75.9       |
----------------------------------
Done [72391 usecs] 2025-07-17 01:02:35.836203
> sys_info site-1
Error: unknown target type site-1
Done [82952 usecs] 2025-07-17 01:02:44.688861
> sys_info client site-1
Client: site-1
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156657664 |
| available         | 3388084224 |
| percent           | 18.5       |
| used              | 570077184  |
| free              | 2571390976 |
| active            | 805842944  |
| inactive          | 527073280  |
| buffers           | 49958912   |
| cached            | 965230592  |
| shared            | 29986816   |
| slab              | 132096000  |
| available_percent | 75.6       |
----------------------------------
Done [110807 usecs] 2025-07-17 01:02:57.184639
> sys_info client site-2
Client: site-2
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156489728 |
| available         | 3443499008 |
| percent           | 17.2       |
| used              | 529235968  |
| free              | 2967175168 |
| active            | 489185280  |
| inactive          | 472559616  |
| buffers           | 46129152   |
| cached            | 613949440  |
| shared            | 22872064   |
| slab              | 105783296  |
| available_percent | 75.9       |
----------------------------------
Done [118329 usecs] 2025-07-17 01:03:09.602813
> sys_info client site-3
Client: site-3
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156432384 |
| available         | 3422662656 |
| percent           | 17.7       |
| used              | 542625792  |
| free              | 2604318720 |
| active            | 776704000  |
| inactive          | 529207296  |
| buffers           | 70512640   |
| cached            | 938975232  |
| shared            | 22921216   |
| slab              | 124203008  |
| available_percent | 75.9       |
----------------------------------
Done [119331 usecs] 2025-07-17 01:03:12.447255
```


#### API interaction 
```
> sys_info server 
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 2067730432 |
| available         | 1305690112 |
| percent           | 36.9       |
| used              | 642949120  |
| free              | 653094912  |
| active            | 613875712  |
| inactive          | 513527808  |
| buffers           | 46424064   |
| cached            | 725262336  |
| shared            | 34820096   |
| slab              | 115167232  |
| available_percent | 63.1       |
----------------------------------
Done [75433 usecs] 2025-07-18 00:11:40.041932
> sys_info clients site-1
Error: unknown target type clients
Done [79563 usecs] 2025-07-18 00:12:11.461698
> sys_info client site-1
Client: site-1
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156657664 |
| available         | 3399151616 |
| percent           | 18.2       |
| used              | 566804480  |
| free              | 2857603072 |
| active            | 524935168  |
| inactive          | 538550272  |
| buffers           | 34562048   |
| cached            | 697688064  |
| shared            | 29134848   |
| slab              | 113930240  |
| available_percent | 63.1       |
----------------------------------
Done [108454 usecs] 2025-07-18 00:12:15.864341
> sys_info client site-2
Client: site-2
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156489728 |
| available         | 3388907520 |
| percent           | 18.5       |
| used              | 583999488  |
| free              | 2862108672 |
| active            | 573595648  |
| inactive          | 447455232  |
| buffers           | 46526464   |
| cached            | 663855104  |
| shared            | 22876160   |
| slab              | 108888064  |
| available_percent | 63.2       |
----------------------------------
Done [118801 usecs] 2025-07-18 00:12:24.618782
> sys_info client site-3
Client: site-3
----------------------------------
| METRICS           | VALUE      |
----------------------------------
| total             | 4156432384 |
| available         | 3437236224 |
| percent           | 17.3       |
| used              | 534814720  |
| free              | 2929438720 |
| active            | 503083008  |
| inactive          | 491184128  |
| buffers           | 39804928   |
| cached            | 652374016  |
| shared            | 22937600   |
| slab              | 108498944  |
| available_percent | 63.1       |
----------------------------------
Done [105446 usecs] 2025-07-18 00:12:27.454320
> 

```

### Interaction from clients 
```
return sys_info
{'total': 4156657664, 'available': 3388084224, 'percent': 18.5, 'used': 570077184, 'free': 2571390976, 'active': 805842944, 'inactive': 527073280, 'buffers': 49958912, 'cached': 965230592, 'shared': 29986816, 'slab': 132096000}
```

```
return sys_info
{'total': 4156489728, 'available': 3388907520, 'percent': 18.5, 'used': 583999488, 'free': 2862108672, 'active': 573595648, 'inactive': 447455232, 'buffers': 46526464, 'cached': 663855104, 'shared': 22876160, 'slab': 108888064}


```

```
return sys_info
{'total': 4156432384, 'available': 3437236224, 'percent': 17.3, 'used': 534814720, 'free': 2929438720, 'active': 503083008, 'inactive': 491184128, 'buffers': 39804928, 'cached': 652374016, 'shared': 22937600, 'slab': 108498944}

```

### Starting job 
```
> check_status client
----------------------------------------
| CLIENT | APP_NAME | JOB_ID | STATUS  |
----------------------------------------
| site-1 | ?        | ?      | No Jobs |
| site-2 | ?        | ?      | No Jobs |
----------------------------------------
Done [155230 usecs] 2025-07-18 04:23:43.771360
> submit_job hello-pt_cifar10_fedavg
Submitted job: 8602a837-3161-4a0a-b104-4e6b0ffa69ad
Done [267952 usecs] 2025-07-18 04:23:52.390956
> check_status client
-------------------------------------------------------------------------
| CLIENT | APP_NAME   | JOB_ID                               | STATUS   |
-------------------------------------------------------------------------
| site-1 | app_site-1 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | starting |
| site-2 | app_site-2 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | starting |
-------------------------------------------------------------------------
Done [59066 usecs] 2025-07-18 04:23:54.687414
> check_status client
------------------------------------------------------------------------
| CLIENT | APP_NAME   | JOB_ID                               | STATUS  |
------------------------------------------------------------------------
| site-1 | app_site-1 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | started |
| site-2 | app_site-2 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | started |
------------------------------------------------------------------------
Done [103108 usecs] 2025-07-18 04:24:17.905772
> check_status client
------------------------------------------------------------------------
| CLIENT | APP_NAME   | JOB_ID                               | STATUS  |
------------------------------------------------------------------------
| site-1 | app_site-1 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | started |
| site-2 | app_site-2 | 8602a837-3161-4a0a-b104-4e6b0ffa69ad | started |
------------------------------------------------------------------------
Done [88817 usecs] 2025-07-18 04:24:19.739681
```


```
25-07-17 17:46:40,807 - DefaultJobScheduler - INFO - [identity=server, run=?] - Try to schedule job 8602a837-3161-4a0a-b104-4e6b0ffa69ad, get result: (scheduled).
2025-07-17 17:46:40,817 - JobRunner - INFO - [identity=server, run=?] - Got the job: 8602a837-3161-4a0a-b104-4e6b0ffa69ad from the scheduler to run
2025-07-17 17:46:40,866 - JobRunner - INFO - [identity=server, run=?] - Application app_server deployed to the server for job: 8602a837-3161-4a0a-b104-4e6b0ffa69ad
2025-07-17 17:46:40,890 - JobRunner - INFO - [identity=server, run=?] - App app_site-1 to be deployed to the clients: site-1 for run: 8602a837-3161-4a0a-b104-4e6b0ffa69ad
2025-07-17 17:46:40,913 - JobRunner - INFO - [identity=server, run=?] - App app_site-2 to be deployed to the clients: site-2 for run: 8602a837-3161-4a0a-b104-4e6b0ffa69ad
2025-07-17 17:46:41,049 - JobRunner - INFO - [identity=server, run=?] - Updated the schedule history of Job: 8602a837-3161-4a0a-b104-4e6b0ffa69ad
2025-07-17 17:46:41,092 - ServerProcessJobLauncher - INFO - Launch the job in process ID: 4334
2025-07-17 17:46:41,094 - ServerEngine - INFO - Launch job_id: 8602a837-3161-4a0a-b104-4e6b0ffa69ad  with job launcher: <class 'nvflare.app_common.job_launcher.server_process_launcher.ServerProcessJobLauncher'> 
2025-07-17 17:46:41,307 - JobRunner - INFO - [identity=server, run=?] - Started run: 8602a837-3161-4a0a-b104-4e6b0ffa69ad for clients: site-1,site-2
2025-07-17 17:46:41,320 - JobRunner - INFO - [identity=server, run=?] - Job: 8602a837-3161-4a0a-b104-4e6b0ffa69ad started to run, status changed to RUNNING.
2025-07-17 17:46:42,696 - runner_process - INFO - Runner_process started.
2025-07-17 17:46:42,722 - ServerDeployer - INFO - server heartbeat timeout set to 600
2025-07-17 17:46:43,862 - CoreCell - INFO - server.8602a837-3161-4a0a-b104-4e6b0ffa69ad: created backbone internal connector to tcp://localhost:3726 on parent
2025-07-17 17:46:43,864 - conn_manager - INFO - Connector [CH00001 ACTIVE tcp://localhost:3726] is starting
2025-07-17 17:46:43,866 - Cell - INFO - Register blob CB for channel='server_command', topic='*'
2025-07-17 17:46:43,868 - conn_manager - INFO - Connection [CN00002 127.0.0.1:36310 => 127.0.0.1:3726] is created: PID: 4334
2025-07-17 17:46:43,868 - conn_manager - INFO - Connection [CN00007 127.0.0.1:3726 <= 127.0.0.1:36310] is created: PID: 19351
2025-07-17 17:46:43,869 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 17:46:43,871 - ServerCommandAgent - INFO - ServerCommandAgent cell register_request_cb: server.8602a837-3161-4a0a-b104-4e6b0ffa69ad
2025-07-17 17:46:43,902 - IntimeModelSelector - INFO - model selection weights control: {}
2025-07-17 17:46:46,002 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 17:46:46,003 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 17:46:46,007 - AuxRunner - INFO - registered aux handler for topic __sync_runner__
2025-07-17 17:46:46,008 - AuxRunner - INFO - registered aux handler for topic __job_heartbeat__
2025-07-17 17:46:46,009 - AuxRunner - INFO - registered aux handler for topic __task_check__
2025-07-17 17:46:46,011 - AuxRunner - INFO - registered aux handler for topic RM.RELIABLE_REQUEST
2025-07-17 17:46:46,013 - AuxRunner - INFO - registered aux handler for topic RM.RELIABLE_REPLY
2025-07-17 17:46:46,015 - ReliableMessage - INFO - enabled reliable message: max_request_workers=20 query_interval=2.0
2025-07-17 17:46:46,016 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - Server runner starting ...
2025-07-17 17:46:46,018 - TBAnalyticsReceiver - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - Tensorboard records can be found in /home/george/Documents/server1/startup/../8602a837-3161-4a0a-b104-4e6b0ffa69ad/tb_events you can view it using `tensorboard --logdir=/home/george/Documents/server1/startup/../8602a837-3161-4a0a-b104-4e6b0ffa69ad/tb_events`
2025-07-17 17:46:46,020 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 17:46:46,021 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - starting workflow controller (<class 'nvflare.app_common.workflows.fedavg.FedAvg'>) ...
2025-07-17 17:46:46,023 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Initializing BaseModelController workflow.
2025-07-17 17:46:46,024 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Workflow controller (<class 'nvflare.app_common.workflows.fedavg.FedAvg'>) started
2025-07-17 17:46:46,026 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Beginning model controller run.
2025-07-17 17:46:46,028 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Start FedAvg.
2025-07-17 17:46:46,029 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - loading initial model from persistor
2025-07-17 17:46:46,031 - PTFileModelPersistor - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Both source_ckpt_file_full_name and ckpt_preload_path are not provided. Using the default model weights initialized on the persistor side.
2025-07-17 17:46:46,033 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Round 0 started.
2025-07-17 17:46:46,035 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Sampled clients: ['site-1', 'site-2']
2025-07-17 17:46:46,036 - FedAvg - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - Sending task train to ['site-1', 'site-2']
2025-07-17 17:46:46,038 - WFCommServer - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller] - scheduled task train
2025-07-17 17:46:48,100 - conn_manager - INFO - Connection [CN00008 0.0.0.0:8002 <= ipv4:192.168.1.65:58652 SSL site-1] is created: PID: 19351
2025-07-17 17:46:48,771 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller, peer=site-1, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - assigned task to client site-1: name=train, id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa
2025-07-17 17:46:48,776 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller, peer=site-1, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - sent task assignment to client. client_name:site-1 task_id:c0dcc403-de0a-4fc7-aea2-b6c4564608fa
2025-07-17 17:46:48,778 - GetTaskCommand - INFO - return task to client.  client_name: site-1  task_name: train   task_id: c0dcc403-de0a-4fc7-aea2-b6c4564608fa  sharable_header_task_id: c0dcc403-de0a-4fc7-aea2-b6c4564608fa
2025-07-17 17:46:50,449 - conn_manager - INFO - Connection [CN00009 0.0.0.0:8002 <= ipv4:192.168.1.67:40920 SSL site-2] is created: PID: 19351
2025-07-17 17:46:51,135 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller, peer=site-2, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=55cfaee1-a030-49ea-922f-7e98522cf031] - assigned task to client site-2: name=train, id=55cfaee1-a030-49ea-922f-7e98522cf031
2025-07-17 17:46:51,139 - ServerRunner - INFO - [identity=jetson_fl_project, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, wf=controller, peer=site-2, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=55cfaee1-a030-49ea-922f-7e98522cf031] - sent task assignment to client. client_name:site-2 task_id:55cfaee1-a030-49ea-922f-7e98522cf031
2025-07-17 17:46:51,142 - GetTaskCommand - INFO - return task to client.  client_name: site-2  task_name: train   task_id: 55cfaee1-a030-49ea-922f-7e98522cf031  sharable_header_task_id: 55cfaee1-a030-49ea-922f-7e98522cf031
```


```
2025-07-18 04:14:11,055 - MPM - INFO - MPM: Good Bye!
2025-07-18 04:14:15,434 - JobExecutor - INFO - run (896b8203-1e74-48da-b6a8-b34a4cc19dd3): child worker process finished with RC 0
cd Desktop/62025-07-18 04:23:53,511 - ClientEngine - INFO - Starting client app. rank: 0
2025-07-18 04:23:53,541 - ClientProcessJobLauncher - INFO - Launch the job in process ID: 26385
2025-07-18 04:23:53,544 - JobExecutor - INFO - Launched job 8602a837-3161-4a0a-b104-4e6b0ffa69ad with job launcher: <class 'nvflare.app_common.job_launcher.client_process_launcher.ClientProcessJobLauncher'> 
2025-07-18 04:23:53,546 - JobExecutor - INFO - run (8602a837-3161-4a0a-b104-4e6b0ffa69ad): waiting for child worker process to finish.
2025-07-18 04:23:56,152 - worker_process - INFO - Worker_process started.
2025-07-18 04:23:58,865 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-18 04:23:58,870 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-18 04:23:58,872 - AuxRunner - INFO - registered aux handler for topic __end_run__
2025-07-18 04:23:58,873 - AuxRunner - INFO - registered aux handler for topic __do_task__
2025-07-18 04:24:00,381 - CoreCell - INFO - site-1.8602a837-3161-4a0a-b104-4e6b0ffa69ad: created backbone internal connector to tcp://localhost:56094 on parent
2025-07-18 04:24:00,386 - CoreCell - INFO - site-1.8602a837-3161-4a0a-b104-4e6b0ffa69ad: created backbone external connector to grpc://server1:8002
2025-07-18 04:24:00,387 - conn_manager - INFO - Connector [CH00001 ACTIVE tcp://localhost:56094] is starting
2025-07-18 04:24:00,389 - conn_manager - INFO - Connector [CH00002 ACTIVE grpc://server1:8002] is starting
2025-07-18 04:24:00,392 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-18 04:24:00,394 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-18 04:24:00,394 - conn_manager - INFO - Connection [CN00002 127.0.0.1:59244 => 127.0.0.1:56094] is created: PID: 26385
2025-07-18 04:24:00,395 - conn_manager - INFO - Connection [CN00004 127.0.0.1:56094 <= 127.0.0.1:59244] is created: PID: 14864
2025-07-18 04:24:00,396 - FederatedClient - INFO - Wait for client_runner to be created.
2025-07-18 04:24:00,400 - FederatedClient - INFO - Got client_runner after 0.0034673213958740234 seconds
2025-07-18 04:24:00,404 - FederatedClient - INFO - Got the new primary SP: grpc://server1:8002
2025-07-18 04:24:00,407 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-18 04:24:00,421 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-18 04:24:00,432 - conn_manager - INFO - Connection [CN00003 N/A => server1:8002] is created: PID: 26385
2025-07-18 04:24:00,449 - ClientAppRunner - INFO - notified status 2 to site-1 in 0.026561737060546875 seconds after 1 tries
2025-07-18 04:24:00,450 - AuxRunner - INFO - registered aux handler for topic __sync_runner__
2025-07-18 04:24:00,452 - AuxRunner - INFO - registered aux handler for topic __job_heartbeat__
2025-07-18 04:24:00,453 - AuxRunner - INFO - registered aux handler for topic __task_check__
2025-07-18 04:24:00,957 - ClientRunner - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - syncing to parent server ...
2025-07-18 04:24:01,045 - ClientRunner - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - synced to parent server in 0.5901029109954834 seconds
2025-07-18 04:24:01,056 - AuxRunner - INFO - registered aux handler for topic RM.RELIABLE_REQUEST
2025-07-18 04:24:01,059 - AuxRunner - INFO - registered aux handler for topic RM.RELIABLE_REPLY
2025-07-18 04:24:01,062 - ReliableMessage - INFO - enabled reliable message: max_request_workers=20 query_interval=2.0
2025-07-18 04:24:01,066 - TaskScriptRunner - INFO - start task run() with full path: /home/george/Documents/site-1/startup/../8602a837-3161-4a0a-b104-4e6b0ffa69ad/app_site-1/custom/src/hello-pt_cifar10_fl.py
2025-07-18 04:24:01,066 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-18 04:24:01,069 - ClientRunner - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - client runner started
2025-07-18 04:24:01,209 - Communicator - INFO - Received from server. getTask: train size: 251.5KB (251534 Bytes) time: 0.131573 seconds
2025-07-18 04:24:01,212 - FederatedClient - INFO - pull_task completed. Task name:train Status:True 
2025-07-18 04:24:01,213 - ClientRunner - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad] - got task assignment: name=train, id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa
2025-07-18 04:24:01,217 - ClientRunner - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - invoking task executor PTInProcessClientAPIExecutor
2025-07-18 04:24:01,220 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - execute for task (train)
2025-07-18 04:24:01,224 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - send data to peer
2025-07-18 04:24:01,226 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - sending payload to peer
2025-07-18 04:24:01,232 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, peer=jetson_fl_project, peer_run=8602a837-3161-4a0a-b104-4e6b0ffa69ad, task_name=train, task_id=c0dcc403-de0a-4fc7-aea2-b6c4564608fa] - Waiting for result from peer
2025-07-18 04:24:04,288 - TaskScriptRunner - INFO - Files already downloaded and verified
2025-07-18 04:24:05,551 - TaskScriptRunner - INFO - current_round=0
2025-07-18 04:24:29,932 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 0, Loss: 0.0001959008773167928
2025-07-18 04:25:29,647 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 3000, Loss: 0.519110667993625

```

### List jobs 

```
> list_jobs
-----------------------------------------------------------------------------------------------------------------------------------------------------
| JOB ID                               | NAME                    | STATUS                       | SUBMIT TIME                      | RUN DURATION   |
-----------------------------------------------------------------------------------------------------------------------------------------------------
| 165d5ccd-1aaf-4aca-9e7e-508442b7cac5 | hello-numpy-sag         | FINISHED:COMPLETED           | 2025-07-17T14:21:26.795288+02:00 | 0:00:14.132451 |
| 932f7a3c-37ef-410e-a7dc-38f670463ea2 | hello-numpy-sag         | FINISHED:COMPLETED           | 2025-07-17T14:25:07.393024+02:00 | 0:00:14.190063 |
| f81414c5-6d45-461d-bf08-ebe12341e572 | hello-numpy-sag         | FINISHED:COMPLETED           | 2025-07-17T14:26:08.627866+02:00 | 0:00:14.484507 |
| 0299913f-7f2c-42ff-912a-eef6692d5b59 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:16:23.425761+02:00 | 0:00:06.817484 |
| 79c51db1-3dba-4f2a-822a-967c22cb841e | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:18:22.139019+02:00 | 0:00:12.482420 |
| f0f97dd7-0035-49a4-a9e9-16ee3450e834 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:21:32.715497+02:00 | 0:00:10.390130 |
| 664310e2-0f99-4600-9317-e934495ea97f | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:27:18.977372+02:00 | 0:00:09.536210 |
| 7985485f-758d-4515-92c5-230e7e6a9776 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:30:47.713341+02:00 | 0:00:10.140792 |
| 9195c2ff-cac7-4b0a-a7f7-f7ce84c6b567 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:31:48.878503+02:00 | 0:00:09.246538 |
| 207f44dd-097e-4bec-92ba-f978ac02e074 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:32:24.913223+02:00 | 0:00:09.558159 |
| d2ad58a6-07fb-430a-a53f-fb840506e767 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:33:28.634633+02:00 | 0:00:09.514883 |
| 0f1377a8-dd9c-4f6e-975d-235e7a8b42c7 | hello-pt                | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T15:35:45.631859+02:00 | 0:00:09.570898 |
| 0d43033c-dddf-496a-9882-766a69b06fd8 | hello-pt_cifar10_fedavg | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T16:01:50.994576+02:00 | 0:00:15.902358 |
| f5f567f2-c084-4701-8020-ba9bd2be7c51 | hello-pt_cifar10_fedavg | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T16:08:19.626263+02:00 | 0:00:15.444728 |
| 2a512a12-c897-4fcd-a355-e9c9f46fc781 | hello-pt_cifar10_fedavg | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T16:11:17.818989+02:00 | 0:00:15.942705 |
| d13e1025-2e9c-4fdb-aeb2-28e296ede448 | hello-pt_cifar10_fedavg | FINISHED:EXECUTION_EXCEPTION | 2025-07-17T16:17:52.516171+02:00 | 0:00:15.508238 |
| 896b8203-1e74-48da-b6a8-b34a4cc19dd3 | hello-pt_cifar10_fedavg | RUNNING                      | 2025-07-17T16:55:04.063185+02:00 | 0:26:59.452235 |
-----------------------------------------------------------------------------------------------------------------------------------------------------
Done [81213 usecs] 2025-07-18 03:59:15.816974

```