#!/bin/bash
sudo docker exec -it busy sh -c "cat /root/.kube/project-key.pem" > ~/.ssh/project-key.pem
cd ../spark-job/key-collector
sudo docker-compose kill
