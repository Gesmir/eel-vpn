#!/bin/sh

ovpnfolder="ovpn-data"

# preconditions
if [ "$EUID" -ne 0 ]; then
	echo "Please run as root"
	exit 1
fi

# script starts here
cd ./$ovpnfolder/

# no input <- selects a random vpn
if [[ $# -eq 0 ]]; then
	vpn=$(python pick-random-vpn.py)

	openvpn --config $vpn --auth-user-pass pass --daemon eel-vpn
	echo "openvpn is running with configfile:" $vpn
	exit 0
fi

# Use a random .ovpn in ./$ovpnfolder/
if [[ $1 == "start" ]]; then
	vpn=$(python pick-random-vpn.py)

	openvpn --config $vpn --auth-user-pass pass --daemon eel-vpn
	echo "openvpn is running with configfile:" $vpn
	exit 0
fi

# stop vpn <- kill openvpn
if [[ $1 == "stop" ]]; then
	killall openvpn

	if [ $? -eq 0 ]; then
		echo "stoped openvpn"
	fi
	exit 0
fi

# Search for String
vpn=$(python pick-country-vpn.py $1)

# true if nothing was found
if [[ $vpn == "1" ]]; then
	echo "could not find "$1
	exit 1
fi

openvpn --config $vpn --auth-user-pass pass --daemon eel-vpn
echo "openvpn is running with configfile:" $vpn
exit 0
