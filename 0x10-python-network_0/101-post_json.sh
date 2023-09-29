#!/bin/bash
# A bash script that sends a JSON POST request to a URL passed as argument.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
