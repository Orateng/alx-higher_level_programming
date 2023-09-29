#!/bin/bash
# Display all HTTP methods of a given URL the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
