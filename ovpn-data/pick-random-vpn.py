import os
import re
import sys
import random

vpnlist = []

for file in os.listdir("."):
	if bool(re.search('.*ovpn', file)):
		vpnlist.append(file);

print(random.choice(vpnlist))
sys.exit()