#!/bin/bash
# A bash script that takes a URL, sends a POST request to the passed URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
