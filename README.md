# eel_vpn

small  python script for switching, random picking, random picking after x time of a vpn via openvpn. The python script works without the other files.

## Usage

You can either use eel_vpn.py as a standalone script or as a bash command.

### 1. Standalone script

The certificate must be in the same folder of the [location of .ovpn file]

```bash
$ sudo eel_vpn.py -c [searchphrase] -l [location of .ovpn file] -p [location of the pass file]
```



### 2. Bash command 

When you run the wizard ```$ sudo sh wizard.sh``` , you can call eel_vpn anywhere. The Program now lies in ```/opt/eel_vpn/```. You can put your ovpn files, cetificat and pass in ```/opt/eel_vpn/ovpn-data/```. **Please make sure that you change the premisions of your pass file to -rwx------ (700)**. The wizard will do it for the dummy file ```/ovpn-data/pass``` .

**TLDR**:

1. run the wizzard ```$ sudo sh wizard.sh```
2. Change the pass file with your pass file ```/opt/eel_vpn/ovpn-data/pass```.
3. Put .ovpn files in ```/opt/eel_vpn/ovpn-data/``` 
4. you can now call the script anywhere ```$ sudo eel_vpn``` (pick a random ovpn config file)



## Help

| Parameter        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| -h, --help       | shows help message, see below                                |
| -c, --choose     | Choose a random ovpn file which contains the string parsed as argument.<br />Default value will pick any ovpn file. |
| -l, --folder_loc | Location folder which contains the ovpn files, default is './ovpn-data/' |
| -p, --pass_loc   | Location of the pass file, default is './ovpn-data/pass'     |
| -t, --time       | Changes config every 'argument passed' amount of seconds.    |
| -s, --stop       | kill all openvpn                                             |

#### -h output:

```bash
usage: eel_vpn.py [-h] [-c CHOOSE] [-s] [-t TIME] [-l FOLDER_LOC]
                  [-p PASS_LOC]

optional arguments:
  -h, --help            show this help message and exit
  -c CHOOSE, --choose CHOOSE
                        choose a vpn which contains the argument parsed, will
                        pick a random vpn without
  -s, --stop            killall vpn
  -t TIME, --time TIME  usage: '-t 120'; changes vpn every 2 minutes
  -l FOLDER_LOC, --folder_loc FOLDER_LOC
                        usage: '-f //etc/openvpn/server'; static path the
                        folder which contains the .ovpn config files
  -p PASS_LOC, --pass_loc PASS_LOC
                        usage: '-p //etc/openvpn/pass'; static path to the
                        pass file
```



### Dependencies
- python3
- openvpn
