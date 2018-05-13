if [ "$EUID" -ne 0 ]; then
	echo "run this script as root"
fi

mv -v ./eel-vpn //bin/
chmod -v 740 //bin/eel-vpn
mkdir -v //opt/eel-vpn
mv -v ./* //opt/eel-vpn/
chown -v -R root //opt/eel-vpn/
chmod -v -R 740 //opt/eel-vpn/
