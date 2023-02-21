#!/bin/bash

echo "enter 1 for rock, 2 for paper, 3 for scissors"

read user_choice
user_choice=$(( $user_choice - 1 ))
computer_choice=$(( RANDOM % 3))

choices=("Rock" "Paper" "Scissors")

echo "You chose ${choices[$user_choice]} and the computer chose ${choices[$computer_choice]}"

if [[ $(( $user_choice - $computer_choice )) -eq 1 || $(( $computer_choice - $user_choice )) -eq 2 ]]; then
    echo "You won!"
elif [ $user_choice -eq $computer_choice ]; then
    echo "It's a tie!"
else
    echo "You lose!"
fi

