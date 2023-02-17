#!/bin/bash

name=$1
attribute=$2

user=$(whoami)
date=$(date)
directory=$(pwd)

echo "Good afternoon $name
You're looking good today"
sleep 1
echo "You have a sick $attribute"
sleep 2

echo "you are logged in as $user and are in directory $directory on $date"
