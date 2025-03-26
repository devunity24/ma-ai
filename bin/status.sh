#!/bin/bash

if [ -f server.pid ]; then
    if ps -p $(cat server.pid) > /dev/null; then
       echo "Server is running."
    else
       echo "Server is not running."
       rm server.pid
    fi
else
    echo "Server is not running."
fi