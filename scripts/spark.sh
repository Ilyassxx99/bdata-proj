#!/bin/bash
sudo cp filesample.txt /var/lib/docker/volumes/stack-creator_mykubeconfig/_data
cd ../spark-job/spark-creator
cp ../../scripts/env ./.env
sudo docker-compose up
