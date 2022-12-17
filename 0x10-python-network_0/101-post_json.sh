#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.
curl -s "$1" -X POST -d "$2"
