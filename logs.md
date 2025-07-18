
### Log from server 
```
(nvflare-env) george@jetson-nano-2g:~/Documents/server1/startup$ ./start.sh 
(nvflare-env) george@jetson-nano-2g:~/Documents/server1/startup$ WORKSPACE set to /home/george/Documents/server1/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 21544
2025-07-17 13:15:38,462 - ServerDeployer - INFO - server heartbeat timeout set to 600
2025-07-17 13:15:39,230 - CoreCell - INFO - server: creating listener on grpc://0:8002
2025-07-17 13:15:39,599 - CoreCell - INFO - server: created backbone external listener for grpc://0:8002
2025-07-17 13:15:39,604 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:51021] is starting
2025-07-17 13:15:40,108 - CoreCell - INFO - server: created backbone internal listener for tcp://localhost:51021
2025-07-17 13:15:40,124 - conn_manager - INFO - Connector [CH00001 PASSIVE grpc://0:8002] is starting
2025-07-17 13:15:40,140 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 13:15:40,160 - FederatedServer - INFO - max_reg_duration=60.0
2025-07-17 13:15:40,166 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 13:15:40,168 - Server - INFO - added secure port at 0.0.0.0:8002
2025-07-17 13:15:40,169 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 13:15:40,172 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 13:15:40,175 - ObjectStreamer - INFO - registered processor_factory: channel='log_streaming' topic='*' _ChunkConsumerFactory
2025-07-17 13:15:40,176 - ServerDeployer - INFO - deployed FLARE Server.
2025-07-17 13:15:40,194 - hci - INFO - Starting Admin Server server1 on Port 8003
2025-07-17 13:15:40,195 - root - INFO - Server started
2025-07-17 13:15:40,670 - ServerState - INFO - Got the primary sp: server1 fl_port: 8002 SSID: ebc6125d-0a56-4688-9b08-355fe9e4d61a. Turning to hot.
2025-07-17 13:15:59,795 - conn_manager - INFO - Connection [CN00002 0.0.0.0:8002 <= ipv4:192.168.1.65:58348 SSL site-1] is created: PID: 21544
2025-07-17 13:16:02,656 - ClientManager - INFO - identity verified for client 'site-1'
2025-07-17 13:16:02,658 - ClientManager - INFO - authenticated client site-1: client_fqcn='site-1'
2025-07-17 13:16:02,660 - ClientManager - INFO - Client: New client site-1@192.168.1.65 joined. Sent token: b92742f9-9c20-476e-9a10-6e3087654214.  Total clients: 1
2025-07-17 13:16:47,705 - conn_manager - INFO - Connection [CN00003 0.0.0.0:8002 <= ipv4:192.168.1.67:39748 SSL site-2] is created: PID: 21544
2025-07-17 13:16:48,387 - ClientManager - INFO - identity verified for client 'site-2'
2025-07-17 13:16:48,390 - ClientManager - INFO - authenticated client site-2: client_fqcn='site-2'
2025-07-17 13:16:48,392 - ClientManager - INFO - Client: New client site-2@192.168.1.67 joined. Sent token: 470a7465-ba33-4b0d-bd7f-0d4906f384f7.  Total clients: 2
2025-07-17 13:28:41,935 - conn_manager - INFO - Connection [CN00004 0.0.0.0:8002 <= ipv4:192.168.1.66:48160 SSL site-3] is created: PID: 21544
2025-07-17 13:28:42,731 - ClientManager - INFO - identity verified for client 'site-3'
2025-07-17 13:28:42,734 - ClientManager - INFO - authenticated client site-3: client_fqcn='site-3'
2025-07-17 13:28:42,736 - ClientManager - INFO - Client: New client site-3@192.168.1.66 joined. Sent token: 35df0d3c-f62f-4e86-8e43-91a883102456.  Total clients: 3

```


### Log from client 1 
```
(nvflare-env) george@jetson-n2:~/Documents/site-1/startup$ WORKSPACE set to /home/george/Documents/site-1/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 8033
2025-07-18 00:08:45,659 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-18 00:08:45,667 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-18 00:08:45,681 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-18 00:08:45,701 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-18 00:08:45,704 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-18 00:08:45,814 - CoreCell - INFO - site-1: created backbone external connector to grpc://server1:8002
2025-07-18 00:08:45,820 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:45358] is starting
2025-07-18 00:08:46,209 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-18 00:08:46,323 - CoreCell - INFO - site-1: created backbone internal listener for tcp://localhost:45358
2025-07-18 00:08:46,335 - conn_manager - INFO - Connector [CH00001 ACTIVE grpc://server1:8002] is starting
2025-07-18 00:08:46,342 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-18 00:08:46,348 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-18 00:08:46,353 - FederatedClient - INFO - Wait for engine to be created.
2025-07-18 00:08:46,374 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-18 00:08:46,376 - conn_manager - INFO - Connection [CN00002 N/A => server1:8002] is created: PID: 8033
2025-07-18 00:08:46,787 - Authenticator - INFO - verified server identity 'server1'
2025-07-18 00:08:47,227 - Authenticator - INFO - Verified received token and signature successfully
2025-07-18 00:08:47,231 - FederatedClient - INFO - Successfully registered client:site-1 for project jetson_fl_project. Token:d8dc70cf-9450-4cba-9fad-9bd948fe7ecb SSID:ebc6125d-0a56-4688-9b08-355fe9e4d61a
2025-07-18 00:08:47,236 - FederatedClient - INFO - Got engine after 0.882779598236084 seconds
2025-07-18 00:08:47,239 - FederatedClient - INFO - Got the new primary SP: grpc://server1:8002
```
### Log from client 2
```
(nvflare-env) george@jetson-n3:~/Documents/site-2/startup$ ./start.sh 
(nvflare-env) george@jetson-n3:~/Documents/site-2/startup$ WORKSPACE set to /home/george/Documents/site-2/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 6844
2025-07-17 06:52:39,978 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 06:52:39,987 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 06:52:40,007 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 06:52:40,021 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 06:52:40,024 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 06:52:40,158 - CoreCell - INFO - site-2: created backbone external connector to grpc://server1:8002
2025-07-17 06:52:40,164 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:42557] is starting
2025-07-17 06:52:40,530 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 06:52:40,668 - CoreCell - INFO - site-2: created backbone internal listener for tcp://localhost:42557
2025-07-17 06:52:40,679 - conn_manager - INFO - Connector [CH00001 ACTIVE grpc://server1:8002] is starting
2025-07-17 06:52:40,686 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-17 06:52:40,688 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-17 06:52:40,691 - FederatedClient - INFO - Wait for engine to be created.
2025-07-17 06:52:40,709 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 06:52:40,711 - conn_manager - INFO - Connection [CN00002 N/A => server1:8002] is created: PID: 6844
2025-07-17 06:52:41,121 - Authenticator - INFO - verified server identity 'server1'
2025-07-17 06:52:41,555 - Authenticator - INFO - Verified received token and signature successfully
2025-07-17 06:52:41,558 - FederatedClient - INFO - Successfully registered client:site-2 for project jetson_fl_project. Token:76346918-3656-4c0c-91ce-3512ad5b5fe2 SSID:ebc6125d-0a56-4688-9b08-355fe9e4d61a
2025-07-17 06:52:41,561 - FederatedClient - INFO - Got engine after 0.870030403137207 seconds
2025-07-17 06:52:41,563 - FederatedClient - INFO - Got the new primary SP: grpc://server1:8002
```
### Log from client 3 
```
(nvflare-env) george@jetson-n4:~/Documents/site-3/startup$ ./start.sh 
(nvflare-env) george@jetson-n4:~/Documents/site-3/startup$ WORKSPACE set to /home/george/Documents/site-3/startup/..
PYTHONPATH is /local/custom:
start fl because of no pid.fl
new pid 6593
2025-07-17 11:40:17,751 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Request
2025-07-17 11:40:17,756 - AuxRunner - INFO - registered aux handler for topic ObjectStreamer.Abort
2025-07-17 11:40:17,760 - Cell - INFO - Register blob CB for channel='aux_communication', topic='*'
2025-07-17 11:40:17,763 - AuxRunner - INFO - registered aux handler for topic fed.event
2025-07-17 11:40:17,766 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 11:40:17,890 - CoreCell - INFO - site-3: created backbone external connector to grpc://server1:8002
2025-07-17 11:40:17,896 - conn_manager - INFO - Connector [CH00002 PASSIVE tcp://0:60952] is starting
2025-07-17 11:40:18,269 - Communicator - INFO - Waiting for the client cell to be created.
2025-07-17 11:40:18,399 - CoreCell - INFO - site-3: created backbone internal listener for tcp://localhost:60952
2025-07-17 11:40:18,409 - conn_manager - INFO - Connector [CH00001 ACTIVE grpc://server1:8002] is starting
2025-07-17 11:40:18,415 - Cell - INFO - Register blob CB for channel='server_command', topic='get_task'
2025-07-17 11:40:18,418 - Cell - INFO - Register blob CB for channel='server_command', topic='submit_update'
2025-07-17 11:40:18,421 - FederatedClient - INFO - Wait for engine to be created.
2025-07-17 11:40:18,441 - GrpcDriver - INFO - created secure channel at server1:8002
2025-07-17 11:40:18,443 - conn_manager - INFO - Connection [CN00002 N/A => server1:8002] is created: PID: 6593
2025-07-17 11:40:18,859 - Authenticator - INFO - verified server identity 'server1'
2025-07-17 11:40:19,323 - Authenticator - INFO - Verified received token and signature successfully
2025-07-17 11:40:19,326 - FederatedClient - INFO - Successfully registered client:site-3 for project jetson_fl_project. Token:35df0d3c-f62f-4e86-8e43-91a883102456 SSID:ebc6125d-0a56-4688-9b08-355fe9e4d61a
2025-07-17 11:40:19,332 - FederatedClient - INFO - Got engine after 0.9113898277282715 seconds
2025-07-17 11:40:19,334 - FederatedClient - INFO - Got the new primary SP: grpc://server1:8002

```




### Log with Pytorch 
```
025-07-17 17:16:32,089 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - finished processing client result by controller
2025-07-17 17:16:32,092 - SubmitUpdateCommand - INFO - submit_update process. client_name:site-2   task_id:516aabf5-535e-4ed8-9c73-97cd07772d75
2025-07-17 17:16:32,147 - WFCommServer - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - task train exit with status TaskCompletionStatus.OK
2025-07-17 17:16:32,337 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - aggregating 2 update(s) at round 0
2025-07-17 17:16:32,344 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - Start persist model on server.
2025-07-17 17:16:32,359 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - End persist model on server.
2025-07-17 17:16:32,361 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - Round 1 started.
2025-07-17 17:16:32,363 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - Sampled clients: ['site-1', 'site-2']
2025-07-17 17:16:32,365 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - Sending task train to ['site-1', 'site-2']
2025-07-17 17:16:32,367 - WFCommServer - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=516aabf5-535e-4ed8-9c73-97cd07772d75] - scheduled task train
2025-07-17 17:16:33,805 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-1, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - assigned task to client site-1: name=train, id=95332e5c-794a-4f78-9f58-c6b14dfadc28
2025-07-17 17:16:33,807 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-1, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - sent task assignment to client. client_name:site-1 task_id:95332e5c-794a-4f78-9f58-c6b14dfadc28
2025-07-17 17:16:33,809 - GetTaskCommand - INFO - return task to client.  client_name: site-1  task_name: train   task_id: 95332e5c-794a-4f78-9f58-c6b14dfadc28  sharable_header_task_id: 95332e5c-794a-4f78-9f58-c6b14dfadc28
2025-07-17 17:16:34,154 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - assigned task to client site-2: name=train, id=20c08adf-f55b-430f-a5ac-7f9dc3628b90
2025-07-17 17:16:34,158 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - sent task assignment to client. client_name:site-2 task_id:20c08adf-f55b-430f-a5ac-7f9dc3628b90
2025-07-17 17:16:34,159 - GetTaskCommand - INFO - return task to client.  client_name: site-2  task_name: train   task_id: 20c08adf-f55b-430f-a5ac-7f9dc3628b90  sharable_header_task_id: 20c08adf-f55b-430f-a5ac-7f9dc3628b90
2025-07-17 17:36:40,292 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-1, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - got result from client site-1 for task: name=train, id=95332e5c-794a-4f78-9f58-c6b14dfadc28
2025-07-17 17:36:40,296 - IntimeModelSelector - WARNING - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-1, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - validation metric not existing in site-1
2025-07-17 17:36:40,433 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-1, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - finished processing client result by controller
2025-07-17 17:36:40,435 - SubmitUpdateCommand - INFO - submit_update process. client_name:site-1   task_id:95332e5c-794a-4f78-9f58-c6b14dfadc28
2025-07-17 17:36:54,753 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - got result from client site-2 for task: name=train, id=20c08adf-f55b-430f-a5ac-7f9dc3628b90
2025-07-17 17:36:54,757 - IntimeModelSelector - WARNING - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - validation metric not existing in site-2
2025-07-17 17:36:54,895 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - finished processing client result by controller
2025-07-17 17:36:54,897 - SubmitUpdateCommand - INFO - submit_update process. client_name:site-2   task_id:20c08adf-f55b-430f-a5ac-7f9dc3628b90
2025-07-17 17:36:54,946 - WFCommServer - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - task train exit with status TaskCompletionStatus.OK
2025-07-17 17:36:55,098 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - aggregating 2 update(s) at round 1
2025-07-17 17:36:55,105 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - Start persist model on server.
2025-07-17 17:36:55,113 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - End persist model on server.
2025-07-17 17:36:55,115 - FedAvg - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller, peer=site-2, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer_rc=OK, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - Finished FedAvg.
2025-07-17 17:36:55,117 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - Workflow: controller finalizing ...
2025-07-17 17:36:55,120 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - ABOUT_TO_END_RUN fired
2025-07-17 17:36:55,124 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - Firing CHECK_END_RUN_READINESS ...
2025-07-17 17:36:56,964 - conn_manager - INFO - Connection [CN00005 Not Connected] is closed PID: 19351
2025-07-17 17:36:57,136 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - END_RUN fired
2025-07-17 17:36:57,143 - ReliableMessage - INFO - ReliableMessage is shutdown
2025-07-17 17:36:57,147 - ObjectStreamer - INFO - Stream Runer is Shut Down
2025-07-17 17:36:57,149 - ServerRunner - INFO - [identity=jetson_fl_project, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, wf=controller] - Server runner finished.
2025-07-17 17:36:57,375 - conn_manager - INFO - Connection [CN00006 Not Connected] is closed PID: 19351
2025-07-17 17:36:58,762 - FederatedServer - INFO - Server app stopped.


2025-07-17 17:37:00,286 - conn_manager - INFO - Connection [CN00004 Not Connected] is closed PID: 19351
2025-07-17 17:37:00,286 - conn_manager - INFO - Connection [CN00002 Not Connected] is closed PID: 19737
```



```
4dfadc28
2025-07-18 03:53:46,242 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - invoking task executor PTInProcessClientAPIExecutor
2025-07-18 03:53:46,244 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - execute for task (train)
2025-07-18 03:53:46,246 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - send data to peer
2025-07-18 03:53:46,249 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - sending payload to peer
2025-07-18 03:53:46,251 - PTInProcessClientAPIExecutor - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - Waiting for result from peer
2025-07-18 03:53:46,632 - TaskScriptRunner - INFO - current_round=1
2025-07-18 03:53:46,696 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 0, Loss: 0.00014482701818148295
2025-07-18 03:54:46,085 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 3000, Loss: 0.5052243726948897
2025-07-18 03:55:44,964 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 6000, Loss: 0.5050454246153434
2025-07-18 03:56:43,685 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 9000, Loss: 0.5073450659513473
2025-07-18 03:57:42,270 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 12000, Loss: 0.5076050264537334
2025-07-18 03:57:52,052 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 0, Loss: 0.00018570494651794434
2025-07-18 03:58:50,832 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 3000, Loss: 0.5180494626760482
2025-07-18 03:59:49,737 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 6000, Loss: 0.5311826535811027
2025-07-18 04:00:48,571 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 9000, Loss: 0.5130947829981645
2025-07-18 04:01:47,259 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 12000, Loss: 0.510798398921887
2025-07-18 04:01:56,976 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 0, Loss: 0.00018657875061035156
2025-07-18 04:02:55,634 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 3000, Loss: 0.5238199149866899
2025-07-18 04:03:53,171 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 6000, Loss: 0.5292133011966944
2025-07-18 04:04:50,180 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 9000, Loss: 0.5154398984213671
2025-07-18 04:05:47,300 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 12000, Loss: 0.5112644909620285
2025-07-18 04:05:56,861 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 0, Loss: 0.00014604377746582032
2025-07-18 04:06:53,810 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 3000, Loss: 0.5122856138447921
2025-07-18 04:07:50,963 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 6000, Loss: 0.5148601025988658
2025-07-18 04:08:48,173 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 9000, Loss: 0.5096245551357667
2025-07-18 04:09:45,052 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 12000, Loss: 0.5149580699602763
2025-07-18 04:09:54,548 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 0, Loss: 0.00014514864484469096
2025-07-18 04:10:51,509 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 3000, Loss: 0.5240455301652353
2025-07-18 04:11:48,496 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 6000, Loss: 0.5185391445259253
2025-07-18 04:12:45,609 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 9000, Loss: 0.5167911142359177
2025-07-18 04:13:42,718 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 12000, Loss: 0.5225828957160313
2025-07-18 04:13:52,165 - TaskScriptRunner - INFO - Finished Training
2025-07-18 04:13:52,182 - InProcessClientAPI - INFO - Try to send local model back to peer 
2025-07-18 04:13:52,588 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - finished processing task
2025-07-18 04:13:52,591 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - try #1: sending task result to server
2025-07-18 04:13:52,594 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - checking task with server ...
2025-07-18 04:13:52,614 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - start to send task result to server
2025-07-18 04:13:52,617 - FederatedClient - INFO - Starting to push execute result.
2025-07-18 04:13:52,822 - Communicator - INFO - SubmitUpdate to: server. size: 251.6KB (251615 Bytes). time: 0.203568 seconds
2025-07-18 04:13:52,825 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=95332e5c-794a-4f78-9f58-c6b14dfadc28] - task result sent to server
2025-07-18 04:14:07,508 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - received request from Server to end current RUN
2025-07-18 04:14:09,128 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - started end-run events sequence
2025-07-18 04:14:09,131 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - ABOUT_TO_END_RUN fired
2025-07-18 04:14:09,134 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - Firing CHECK_END_RUN_READINESS ...
2025-07-18 04:14:09,137 - InProcessClientAPI - WARNING - ask to stop job: reason: END_RUN received
2025-07-18 04:14:09,206 - InProcessClientAPI - WARNING - request to stop the job for reason END_RUN received
2025-07-18 04:14:09,212 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - END_RUN fired
2025-07-18 04:14:09,214 - ReliableMessage - INFO - ReliableMessage is shutdown
2025-07-18 04:14:09,215 - ObjectStreamer - INFO - Stream Runer is Shut Down
2025-07-18 04:14:09,239 - conn_manager - INFO - Connection [CN00003 Not Connected] is closed PID: 14864
2025-07-18 04:14:09,243 - conn_manager - INFO - Connection [CN00002 Not Connected] is closed PID: 14888
2025-07-18 04:14:09,310 - conn_manager - INFO - Connection [CN00003 Not Connected] is closed PID: 14888
2025-07-18 04:14:09,313 - GrpcDriver - INFO - CLIENT: finished connection [CN00003 Not Connected]
2025-07-18 04:14:09,315 - FederatedClient - INFO - Shutting down client run: site-1
2025-07-18 04:14:09,538 - ClientRunner - INFO - [identity=site-1, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - Client is stopping ...
2025-07-18 04:14:11,055 - MPM - INFO - MPM: Good Bye!
2025-07-18 04:14:15,434 - JobExecutor - INFO - run (896b8203-1e74-48da-b6a8-b34a4cc19dd3): child worker process finished with RC 0
```


```
f9dc3628b90] - sending payload to peer
2025-07-17 10:35:54,017 - PTInProcessClientAPIExecutor - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - Waiting for result from peer
2025-07-17 10:35:54,446 - TaskScriptRunner - INFO - current_round=1
2025-07-17 10:35:54,529 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 0, Loss: 0.00017979856332143147
2025-07-17 10:36:55,049 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 3000, Loss: 0.5064592345654965
2025-07-17 10:37:53,620 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 6000, Loss: 0.5001070880442857
2025-07-17 10:38:52,173 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 9000, Loss: 0.5169823877712091
2025-07-17 10:39:50,481 - TaskScriptRunner - INFO - Epoch: 0/5, Iteration: 12000, Loss: 0.5162799322158098
2025-07-17 10:40:00,249 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 0, Loss: 0.00013546022772789002
2025-07-17 10:40:58,483 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 3000, Loss: 0.5129478663901488
2025-07-17 10:41:57,069 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 6000, Loss: 0.5130249375104904
2025-07-17 10:42:55,435 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 9000, Loss: 0.5122410743584236
2025-07-17 10:43:53,625 - TaskScriptRunner - INFO - Epoch: 1/5, Iteration: 12000, Loss: 0.5190140879650911
2025-07-17 10:44:03,391 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 0, Loss: 0.00018033170700073242
2025-07-17 10:45:01,917 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 3000, Loss: 0.5136859742601713
2025-07-17 10:46:00,454 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 6000, Loss: 0.5172104550053676
2025-07-17 10:46:58,760 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 9000, Loss: 0.5179144467314084
2025-07-17 10:47:56,975 - TaskScriptRunner - INFO - Epoch: 2/5, Iteration: 12000, Loss: 0.5157985760668914
2025-07-17 10:48:06,761 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 0, Loss: 0.00011127264300982158
2025-07-17 10:49:05,271 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 3000, Loss: 0.5155854311188062
2025-07-17 10:50:03,822 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 6000, Loss: 0.5236955174207687
2025-07-17 10:51:02,068 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 9000, Loss: 0.5293789760967096
2025-07-17 10:52:00,586 - TaskScriptRunner - INFO - Epoch: 3/5, Iteration: 12000, Loss: 0.5194493475655715
2025-07-17 10:52:10,355 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 0, Loss: 0.00018807776769002278
2025-07-17 10:53:08,741 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 3000, Loss: 0.5218420486847559
2025-07-17 10:54:07,284 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 6000, Loss: 0.5193994519710541
2025-07-17 10:55:05,691 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 9000, Loss: 0.5168277079164982
2025-07-17 10:56:04,535 - TaskScriptRunner - INFO - Epoch: 4/5, Iteration: 12000, Loss: 0.5330372496644656
2025-07-17 10:56:14,391 - TaskScriptRunner - INFO - Finished Training
2025-07-17 10:56:14,409 - InProcessClientAPI - INFO - Try to send local model back to peer 
2025-07-17 10:56:14,441 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - finished processing task
2025-07-17 10:56:14,444 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - try #1: sending task result to server
2025-07-17 10:56:14,446 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - checking task with server ...
2025-07-17 10:56:14,478 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - start to send task result to server
2025-07-17 10:56:14,481 - FederatedClient - INFO - Starting to push execute result.
2025-07-17 10:56:14,677 - Communicator - INFO - SubmitUpdate to: server. size: 251.6KB (251615 Bytes). time: 0.194854 seconds
2025-07-17 10:56:14,680 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, task_name=train, task_id=20c08adf-f55b-430f-a5ac-7f9dc3628b90] - task result sent to server
2025-07-17 10:56:14,907 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3, peer=jetson_fl_project, peer_run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - received request from Server to end current RUN
2025-07-17 10:56:16,690 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - started end-run events sequence
2025-07-17 10:56:16,698 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - ABOUT_TO_END_RUN fired
2025-07-17 10:56:16,702 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - Firing CHECK_END_RUN_READINESS ...
2025-07-17 10:56:16,705 - InProcessClientAPI - WARNING - ask to stop job: reason: END_RUN received
2025-07-17 10:56:16,917 - InProcessClientAPI - WARNING - request to stop the job for reason END_RUN received
2025-07-17 10:56:16,927 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - END_RUN fired
2025-07-17 10:56:16,929 - ReliableMessage - INFO - ReliableMessage is shutdown
2025-07-17 10:56:16,931 - ObjectStreamer - INFO - Stream Runer is Shut Down
2025-07-17 10:56:16,949 - conn_manager - INFO - Connection [CN00003 Not Connected] is closed PID: 12853
2025-07-17 10:56:16,968 - conn_manager - INFO - Connection [CN00002 Not Connected] is closed PID: 12876
2025-07-17 10:56:17,075 - conn_manager - INFO - Connection [CN00003 Not Connected] is closed PID: 12876
2025-07-17 10:56:17,078 - GrpcDriver - INFO - CLIENT: finished connection [CN00003 Not Connected]
2025-07-17 10:56:17,081 - FederatedClient - INFO - Shutting down client run: site-2
2025-07-17 10:56:17,521 - ClientRunner - INFO - [identity=site-2, run=896b8203-1e74-48da-b6a8-b34a4cc19dd3] - Client is stopping ...
2025-07-17 10:56:19,052 - MPM - INFO - MPM: Good Bye!
2025-07-17 10:56:28,434 - JobExecutor - INFO - run (896b8203-1e74-48da-b6a8-b34a4cc19dd3): child worker process finished with RC 0
```