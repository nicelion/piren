import json
import os

config = []
commands = ["help", "end", "exit", "quit", "pin"]

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

def load():
    global d, occupied_pins, config
    with open('config.json') as json_data:
        d = json.load(json_data)
        config.append(d)

        occupied_pins = d[0]["pins"].values()
        print(45 in occupied_pins)




def verify_change(pin, function):
    responce = input("Are you sure you want to ")

def pin():
    com = input("Enter pin function you would like to change (ex: wail) ")

    if com == "wail":
        wail = input("Enter pin number you would like to change wail to: ")

        try:
            int(wail)

            if int(wail) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(wail) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(wail) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(wail) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()

            else:
                d[0]["pins"]["wail"] = int(wail)

                with open('config.json', 'w') as outfile:
                    json.dump(d, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed wail pin to " + str(wail))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(wail) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()





def get_command():
    comm = input(Colors.WHITE + "Enter a command to get started: " + Colors.ENDC)

    if comm in commands:
        if comm == commands[0]:
            # help
            pass
        if comm == commands[1] or comm == commands[2] or commands == commands[3]:
            pass
        if comm == commands[4]:
            pin()

    else:
        mprint(Colors.BOLD + Colors.WARNING + "[ERROR]: " + Colors.ENDC + "Command '" + comm + "' not valid. Pass 'help'"
                                                                                               "for help.")
        get_command()



os.system("clear")
mprint(Colors.BOLD + Colors.WHITE + "Welcome to piren-config by Nice Lion Technologies")
mprint("Pass 'Help' for more information and commands")
print("v0.1. Released 02-04-17. Copyright to Nice Lion Technologies and Ian Thompson\n")
load()
get_command()




