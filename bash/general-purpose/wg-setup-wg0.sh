#!/bin/bash
ip link add dev wg0 type wireguard # you can change wg0 to whatever you want to name the interface
ip address add dev wg0 10.0.0.1 peer 10.0.0.2 # enter whatever peer private IPs you want here
wg setconf wg0 /etc/wireguard/name_of_config_file
ip link set up dev wg0
