#!/bin/bash
# This script takes a URL and displays the size of the response
curl -sI "$1" | grep -e "Content-Length:" | cut -c17-
