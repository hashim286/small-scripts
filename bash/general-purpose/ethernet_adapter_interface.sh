#!/bin/bash
ip link set (interface name) up
ip address add dev (interface name from line 2) (private IP)/(CIDR)
ip link set (wifi interface) down
route add default gw (default gateway IP) (interface name from line 2)
