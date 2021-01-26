#!/bin/bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/project-key.pem
ssh -i "~/.ssh/project-key.pem" -oStrictHostKeyChecking=no ubuntu@$1
