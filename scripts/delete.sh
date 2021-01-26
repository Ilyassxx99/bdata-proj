#!/bin/bash
sed -i 's/1/2/' ../stack-job/stack-destructor/docker-compose.yaml
cd ../stack-job/stack-destructor
cp ../../scripts/env ./.env
sudo docker-compose up
