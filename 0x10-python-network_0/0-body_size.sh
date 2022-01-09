#!/bin/bash
#script that takes in a URL, sends a request to that URL, 
#and displays the size 
curl "$1" -sI |grep "Content-Length"| cut -d ':' -f 2 | cut -d ' ' -f 2
