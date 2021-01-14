# readme

This repository has a docker-compose files that allows you to create and delete EKS cluster with 5 t2.micro nodes autoscaled between 3 and 7. It contains a docker-compose to start spark jobs on the EKS cluster.
You should have docker and docker-compose installed in your environment


## Prepare the environment

To successfully create the cluster, please enter your AWS user's Access_key and Secret_key (with the right permissions to use AWS resources), and the region where to create the resources, in the .env file located in :
```
- stack-job/stack-creator/.env
- stack-job/stack-destructor/.env
```
Th .env file should look like this :
```
ACCESS_KEY=<Your access key>
SECRET_KEY=<Your secret key>
REGION=<Your region>
```
## Running the containers

### Create Stack

To create the AWS stack go to :
```
 stack-job/stack-creator
```
and execute :
```
 docker-compose up
```
### Delete Stack

To delete the AWS stack go to :
```
 stack-job/stack-destructor
```
and execute :
```
 docker-compose up
```
### Run Spark job

To run a spark job go to :
```
 spark-job/
```
and execute :
```
 docker-compose up
```
