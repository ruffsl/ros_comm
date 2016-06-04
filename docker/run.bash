#!/bin/bash

docker run -it \
  -v /home/ruffsl/git/ruffsl/ros_comm:/root/sros/src/ruffsl/ros_comm:ro \
  -v /tmp/sros/.ros:/root/.ros \
  sros:sdemo bash
