import os
import re
import sys
import random

if len(sys.argv) is 1:
	print("insert command with a country as argument, for example:")
	print("python pick-random-country.py us")
	sys.exit(1)

vpnlist = []
regex = ".*" + sys.argv[1] + ".*ovpn"

for file in os.listdir("."):
	if bool(re.search(regex.upper(), file.upper())):
		vpnlist.append(file);

if len(vpnlist) == 0:
	print("1")
	sys.exit()

print(random.choice(vpnlist))
sys.exit()