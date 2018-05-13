# eel-vpn
small bash & python script for switching, random picking, random picking after x time of a vpn with openvpn

## Before Usage
1. place your ovpn config files in the `./ovpn-data/` directory
2. place your certificat in `./ovpn-data/`
3. edit `./ovpn-data/pass`, if you don't want to enter your login everytime
4. `sudo wizard.sh`

## Usage
`eel-vpn --help`

`sudo eel-vpn start` <- pick a random ovpn file and connect

`sudo eel-vpn stop` <- `killall openvpn`

`sudo eel-vpn start 1m`	<- select a new vpn every minute

`sudo eel-vpn foo` <- select a random ovpn file which contains 'foo'

`sudo eel-vpn foo 1h` <- select a random ovpn file which contains 'foo' every hour

**valid time:**

'120s' 	<- 120 secounds

'78m' 	<- 78 minutes

'12h'	<- 12 hours

'1d'	<- every day

### Dependencies
- python
- openvpn
