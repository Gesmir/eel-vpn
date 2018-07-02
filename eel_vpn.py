#!/bin/python3

# Script for random picking / searching a ovpn file
# and connecting to a vpn via openvpn
# use eel_vpn.py -h for instructions
#
# Copyright:    (c) 2018 Eric Wenzke
# Licence:      CC BY-SA 3.0 DE

from sys import exit
from subprocess import call, check_output, CalledProcessError
from os import chdir, listdir, geteuid, getcwd, kill
from re import search
from random import choice
from argparse import ArgumentParser
from time import sleep


parser = ArgumentParser()
parser.add_argument("-c", "--choose",
                    help="choose a vpn which contains the argument parsed, will pick a random vpn without",
                    default="all")
parser.add_argument("-s", "--stop",
                    help="killall vpn",
                    default=False,
                    action="store_true")
parser.add_argument("-t", "--time",
                    type=int,
                    help="usage: '-t 120'; changes vpn every 2 minutes")
parser.add_argument("-l", "--folder_loc",
                    help="usage: '-l //etc/openvpn/server'; \
                    static path the folder which contains the .ovpn config files",
                    default="//opt/eel_vpn/ovpn-data/")
parser.add_argument("-p", "--pass_loc",
                    help="usage: '-p //etc/openvpn/pass'; static path to the pass file",
                    default="//opt/eel_vpn/ovpn-data/pass")

args = parser.parse_args()


def killall_ovpn():
    pid_list = []
    try:
        pid_list = get_pid("eel_vpn")
    except CalledProcessError:
        return
    for pid in pid_list:
        try:
            kill(pid, 0)
        except OSError:
            continue


def get_pid(process_name):
    return map(int, check_output(check_output(["pidof", process_name])).split())


def exit_when_list_is_empty(ovpn_list):
    if len(ovpn_list) is 0:
        print("can not find file which contains: " + args.choose + " in: " + args.folder_loc)
        exit(1)


def get_ovpn_list(search_phrase):
    ovpn_list = []
    chdir(args.folder_loc)

    for file in listdir("."):
        if bool(search(search_phrase, file)) and bool(search(".*.ovpn", file)):
            ovpn_list.append(file)

    exit_when_list_is_empty(ovpn_list)
    return ovpn_list


def get_random_ovpn_file():
    return choice(get_ovpn_list(".*.ovpn"))


def get_certain_ovpn_file(search_phrase):
    return choice(get_ovpn_list(search_phrase))


def ovpn_exec(ovpn_file):
    print("connecting to vpn with config: " + ovpn_file)
    call(["openvpn",
          "--config",
          ovpn_file,
          "--auth-user-pass",
          args.pass_loc,
          "--daemon",
          "eel-vpn"])


def exit_if_not_root():
    if geteuid() is 0:
        return
    else:
        print("You need root privileges to run openvpn command")
        exit(2)


def get_ovpn_file():
    if args.choose == "all":
        return get_random_ovpn_file()
    else:
        return get_certain_ovpn_file(args.choose)


# script starts here
if args.stop is True:
    killall_ovpn()
    exit(0)

exit_if_not_root()

if args.time is not None:
    print("Stop program with Ctrl+C")
    print("When stopped all vpn connections will be killed")
    try:
        while True:
            killall_ovpn()  # kill existing vpn to avoid duplicated process
            ovpn_exec(get_ovpn_file())
            sleep(args.time)
    except KeyboardInterrupt:
        print("goodbye, btw. you'r not save anymore")
    finally:
        killall_ovpn()

else:
    killall_ovpn()      # kill existing vpn to avoid duplicated process
    ovpn_exec(get_ovpn_file())

exit(0)
