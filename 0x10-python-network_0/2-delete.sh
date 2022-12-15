#!bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response.
crul -s "$1" DELETE
