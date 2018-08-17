import json
import os
from pprint import pprint
import time

commands = ["help", "end", "exit", "quit", "pin", "siren"]

# These pins are unavailable to be used by the Pi because they already have preset functions
invalid_pins = {1: "3.3v DC Power pin", 2: "5v DC Power pin", 4: "5v DC Power pin", 6: "Ground", 9: "Ground",
                14: "Ground", 17: "3.3v DC Power pin", 20: "Ground", 25: "Ground", 30: "Ground", 34: "Ground",
                39: "Ground"}

occupied_pins = {}

error_count = 0


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[97m'


def mprint(s):
    print(s + Colors.ENDC)

def save_json():
    with open('pins.json', 'w') as fp:
        json.dump(occupied_pins, fp, sort_keys=True, indent=4)

def confirm_pin_change(pin, function):
    res = input(Colors.BOLD + Colors.WARNING + "[CONFIRM!]: " + Colors.ENDC + "Do you want to change pin " + str(pin)
                + " to preform function " + str(function) + "? (y/n) ")


    if res == "y":
        return True
    elif res == "n":
        mprint(Colors.BOLD + Colors.FAIL + "ABORTING PIN CHANGE......")
        return False

def pin_already_used(pin):
    if pin in invalid_pins.keys():
        mprint(Colors.BOLD + Colors.FAIL + "[ERROR!]: " + Colors.ENDC + "Pin " + str(pin) + " is occupied by " +
              Colors.WARNING + invalid_pins[pin] + "!")
    elif pin in occupied_pins.values():

        for p in occupied_pins:
            l = occupied_pins[p]

            if l == pin:
                mprint(Colors.BOLD + Colors.FAIL + "[ERROR!]: " + Colors.ENDC + "Pin " + str(pin) + " is occupied by " +
                    Colors.WARNING + p + "!")


def pin():
    com = input("Enter pin function you would like to change (ex: wail) ")

    valid_coms = ["aux", "aux_led", "horn", "manual_wail", "next", "next_brand", "phaser", "prev_brand", "previous",
                  "siren_led", "wail", "yelp"]

    if com == "help":
        print("Valid keys are: " + str(valid_coms))
    elif com == "available_pins":
        print("Avalible pins are: ")
    elif com == "stop":
        get_command()
    elif com in valid_coms:

        pin = input("Enter pin number you would like to change wail to: ")

        try:
            int(pin)

            if int(pin) in invalid_pins.keys() or int(pin) in occupied_pins.values():
                pin_already_used(int(pin))
                pin()
            else:
                confirmed = confirm_pin_change(int(pin), com)

                if confirmed:
                    mprint(Colors.BOLD + Colors.OKGREEN + "[SUCCESS!]: " + Colors.ENDC +
                           "Successfully changed {} to work with pin {}!".format(com, pin))

                    occupied_pins[com] = int(pin)

                    print(occupied_pins)
                    save_json()

        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(pin) + " could not be converted to an integer. "
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()






def get_command():
    comm = input(Colors.WHITE + "Enter a command to get started: " + Colors.ENDC)

    if comm in commands:
        if comm == commands[0]:
            # help
            print('help')
        if comm == commands[1] or comm == commands[2] or commands == commands[3]:
            pass
        if comm == commands[4]:
            pin()
        if comm == commands[5]:
            add_siren()

    else:
        mprint(
            Colors.BOLD + Colors.WARNING + "[ERROR]: " + Colors.ENDC + "Command '" + comm + "' not valid. Pass 'help'"
                                                                                            "for help.")
    get_command()








def welcome():
    os.system("clear")
    mprint(Colors.BOLD + Colors.WHITE + "Welcome to piren-config by Nice Lion Technologies")
    mprint("Pass 'Help' for more information and commands")
    print("v0.1. Released 02-04-17. Copyright to Nice Lion Technologies and Ian Thompson\n")


with open('pins.json') as f:
    data = json.load(f)
    occupied_pins = data

welcome()
print(occupied_pins)
get_command()




