#!/bin/bash
cd ../stack-job
sudo docker build   -t ilyassifez/bdataprojectpython:stacky .
sudo docker push ilyassifez/bdataprojectpython:stacky
