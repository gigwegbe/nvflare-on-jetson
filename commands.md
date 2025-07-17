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
