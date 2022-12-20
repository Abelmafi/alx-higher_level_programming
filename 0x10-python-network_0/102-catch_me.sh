#!/bin/bash
# This script send request to URL that causes the server to respond with a msg!
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
