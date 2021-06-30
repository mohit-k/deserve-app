# deserve-app
It is a simple hello world service written in python flask. Deployed in docker container: 

```
ubuntu@ip-:~$ sudo  docker ps 
CONTAINER ID   IMAGE               COMMAND           CREATED          STATUS          PORTS                                       NAMES
b70551aff05a   deserve-flask-app   "python api.py"   43 minutes ago   Up 43 minutes   0.0.0.0:9090->5000/tcp, :::9090->5000/tcp   deserve-flask-app1
```
```
ubuntu@ip-:~$ sudo docker ps 
CONTAINER ID   IMAGE               COMMAND           CREATED          STATUS          PORTS                                       NAMES
778a99388ca3   deserve-flask-app   "python api.py"   41 minutes ago   Up 41 minutes   0.0.0.0:9090->5000/tcp, :::9090->5000/tcp   deserve-flask-app2
```
