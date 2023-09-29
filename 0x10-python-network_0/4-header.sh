#!/bin/bash
# Sends a GET REQUEST TO A GIVEN url with a header variable.
curl -sH "X-School-User-Id: 98" "${1}"
