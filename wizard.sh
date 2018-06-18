#!/bin/sh

if [ "$EUID" -ne 0 ]; then
    echo run this script as root
    exit 1
fi

mv -v ./eel_vpn //bin/
chmod -v 755 //bin/eel_vpn
mkdir -v //opt/eel_vpn
mv -v ./* //opt/eel_vpn/
chown -v -R root //opt/eel_vpn/
chmod -v -R 755 //opt/eel_vpn/
chmod -v 700 //opt/eel_vpn/ovpn-data/pass
