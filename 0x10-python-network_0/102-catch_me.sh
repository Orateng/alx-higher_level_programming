#!/bin/bash
# Makes a requesrt to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
