#!/bin/bash
# This script
curl -sI "$1" | grep -e "Allow: " | cut -c8-
