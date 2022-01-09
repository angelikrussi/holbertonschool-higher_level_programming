#!/bin/bash
# script that sends a DELETE request to the URL
curl "$1" -sI  | grep "Allow" | cut -d " " -f 2-
