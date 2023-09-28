#!/bin/bash
# Get the byte size of the HTTO
# response header for a given URL.
curl -s "$1" | wc -c
