#!/bin/bash

if [ -f server.pid ]; then
    kill $(cat server.pid)
    rm server.pid
    echo "Server stopped."
else
    echo "Server is not running."
fi