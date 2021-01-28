# readme

This repository has a docker-compose files that allows you to create and delete Kubernetes cluster with 3 t3.small nodes. It contains a docker-compose to start spark jobs on the cluster.
You should have docker and docker-compose installed in your environment


## Prepare the environment

To successfully create the cluster, please enter your AWS user's Access_key and Secret_key (with the right permissions to use AWS resources), and the region where to create the resources, in the env file located in :
```
scripts
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
 ./stack.sh
```
it sets the environment variables and executes docker-compose.
### Delete Stack

To delete the AWS stack go to :
```
 ./delete.sh
```

### Run Spark job

To run a spark job go to :
```
 ./spark.sh
```

