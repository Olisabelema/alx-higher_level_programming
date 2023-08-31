#!/bin/bash
# This script takes a URL, sends a GET request using curl, and displays the body of the response for a 200 status code.

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
    curl -s "$1"
fi
