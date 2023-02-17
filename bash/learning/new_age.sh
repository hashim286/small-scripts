#!/bin/bash

echo "what is your name"
read name

echo "what is your age"
read age

random_num=$(( RANDOM % $age ))

new_age=$(( $age + $random_num ))

echo "your new age is $new_age"
