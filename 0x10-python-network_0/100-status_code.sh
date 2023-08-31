#!/bin/bash
# This script sends a request to a URL provided as an argument and displays only the status code of the response.

response=$(curl -sw "%{http_code}" -o /dev/null "$1")
echo "$response"
