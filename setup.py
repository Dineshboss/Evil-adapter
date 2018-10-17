#!/usr/bin/env python

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser(description="Usage of MODE Changer author by Dinesh")
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MODE")
    parser.add_argument("-m", "--mode", dest="mode", help="New MODE")
    options= parser.parse_args()
    if not options.interface:
        parser.error("Please specify interface, use --help for more info")
        parser.parse_args()
    elif not options.mode:
        parser.error("Please specify mode, use --help for more info")
        parser.parse_args()
    return options


def change_mode(interface, mode):
    print("[+] Changing MODE for " + interface + " to " + mode)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", mode])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    iwconfig_result = subprocess.check_output(["iwconfig", interface])
    regex_final_result = re.search(r"\W\D\D\D\D:\D\D\D\D\D\D\D\s", iwconfig_result.decode('utf-8'))
    if regex_final_result:
        return regex_final_result.group(0)
    else:
        print("[-] Could not read mode")


options = get_arguments()

current_mode = get_current_mac(options.interface)
print("[+] Current MODE = " + str(current_mode))

change_mode(options.interface, options.mode)

current_mode = get_current_mac(options.interface)
if current_mode == options.mode:
    print("[+] MODE successfully changed to " + current_mode)
else:
    print("[+] MODE successfully changed to " + current_mode)
