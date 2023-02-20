#!/bin/bash

num=$(( RANDOM % 2 ))

echo "choose 0 or 1"

read num_user

if [ $num_user -eq $num ]; then
    echo "equals"
else
    echo "not equals"
fi

another_num=$(( RANDOM % 10 ))

echo "pick number between 0 and 9"
read another_num_user


if [ $another_num_user -eq $another_num ]; then
    echo "equals"
else 
    echo "not equals"
fi

echo $another_num

echo "enter a number for something"

read something

case $something in
    1)
        height=180
        weight=200
        ;;
    2)
        height=130
        weight=300
        ;;
    3) height=10
       weight=180
       ;;
esac

echo "$height $weight"

echo $something

