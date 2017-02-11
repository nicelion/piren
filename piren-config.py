import json
import os

config = []
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

def load():
    global d, occupied_pins, config
    with open('config.json') as json_data:
        d = json_data.read()

    config = json.loads(d)

    # print(config)

        # config.append(d)
        #
        # occupied_pins = d[0]["pins"].values()
        #
        # print(len(d[0]["sirens"]))
        #
        # print(d)







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
            elif int(wail) > 40 or int(wail) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(wail) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["wail"] = int(wail)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed wail pin to " + str(wail))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(wail) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "aux":
        aux = input("Enter pin number you would like to change aux to: ")

        try:
            int(aux)

            if int(aux) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(aux) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(aux) > 40 or int(aux) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["aux"] = int(aux)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed wail pin to " + str(aux))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(aux) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "aux_led":
        aux_led = input("Enter pin number you would like to change aux_led to: ")

        try:
            int(aux_led)

            if int(aux_led) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux_led) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(aux_led) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux_led) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(aux_led) > 40 or int(aux_led) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(aux_led) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["aux_led"] = int(aux_led)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed wail pin to " + str(aux_led))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(aux_led) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "horn":
        horn = input("Enter pin number you would like to change horn to: ")

        try:
            int(horn)

            if int(horn) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(horn) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(horn) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(horn) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(horn) > 40 or int(horn) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(horn) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["horn"] = int(horn)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed wail pin to " + str(horn))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(horn) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "manual_wail":
        manual_wail = input("Enter pin number you would like to change manual_wail to: ")

        try:
            int(manual_wail)

            if int(manual_wail) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(manual_wail) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(manual_wail) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(manual_wail) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(manual_wail) > 40 or int(manual_wail) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(horn) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["manual_wail"] = int(manual_wail)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed manual_wail pin to " + str(manual_wail))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(manual_wail) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "next":
        next = input("Enter pin number you would like to change next to: ")

        try:
            int(next)

            if int(next) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(next) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(next) > 40 or int(next) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["next"] = int(next)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed next pin to " + str(next))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(next) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()
    elif com == "next_brand":
        next_brand = input("Enter pin number you would like to change next_brand to: ")

        try:
            int(next_brand)

            if int(next_brand) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next_brand) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(next_brand) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next_brand) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(next_brand) > 40 or int(next_brand) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(next_brand) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["next_brand"] = int(next_brand)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed next_brand pin to " + str(next_brand))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(next_brand) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "phaser":
        phaser = input("Enter pin number you would like to change phaser to: ")

        try:
            int(phaser)

            if int(phaser) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(phaser) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(phaser) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(phaser) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(phaser) > 40 or int(phaser) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(phaser) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["phaser"] = int(phaser)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed phaser pin to " + str(phaser))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(phaser) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "prev_brand":
        prev_brand = input("Enter pin number you would like to change prev_brand to: ")

        try:
            int(prev_brand)

            if int(prev_brand) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(prev_brand) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(prev_brand) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(prev_brand) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(prev_brand) > 40 or int(prev_brand) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(horn) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["prev_brand"] = int(prev_brand)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed prev_brand pin to " + str(prev_brand))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(prev_brand) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "previous":
        previous = input("Enter pin number you would like to change previous to: ")

        try:
            int(previous)

            if int(previous) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(previous) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(previous) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(previous) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(previous) > 40 or int(previous) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(previous) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["previous"] = int(previous)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed previous pin to " + str(previous))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(previous) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "siren_led":
        siren_led = input("Enter pin number you would like to change siren_led to: ")

        try:
            int(siren_led)

            if int(siren_led) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(siren_led) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(siren_led) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(siren_led) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(siren_led) > 40 or int(siren_led) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(siren_led) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["siren_led"] = int(siren_led)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed siren_led pin to " + str(siren_led))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(siren_led) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "yelp":
        yelp = input("Enter pin number you would like to change yelp to: ")

        try:
            int(yelp)

            if int(yelp) in invalid_pins.keys():
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(yelp) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(yelp) in occupied_pins:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(yelp) + " already assigned. Please select a "
                                                                            "different pin number")
                pin()
            elif int(yelp) > 40 or int(yelp) <= 0:
                mprint(Colors.FAIL + "[ERROR]:" + Colors.ENDC + str(yelp) + " out of range. 1-40 are acceptable numbers")
                pin()
            else:
                config[0]["pins"]["yelp"] = int(yelp)

                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

                mprint(Colors.OKGREEN + "[SUCCESS]: " + Colors.ENDC + "Successfuly changed yelp pin to " + str(yelp))
                get_command()


        except ValueError:
            mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + str(yelp) + " could not be converted to an integer.\n"
                                                                         "Make sure you provide a valid GPIO pin number")
            pin()

    elif com == "exit":
        get_command()
    else:
        mprint(Colors.FAIL + "[ERROR]: " + Colors.ENDC + com + " not vaild. Please try again.")
        pin()

def check_path(path):
    if os.path.exists(path):
        return True
    else:
        return False

def add_siren():
    dead = "dead.wav"

    print("\nYou will be asked to provide information on the siren you would like to add. You will be asked the "
          "brand name, model name, and paths to all the sirens.\nFor example, the program will ask you for the wail"
          " siren path. If your siren does not have a wail, you can replace it with something else. You do not need "
          "to provide a wail siren path when it asks you to provide a wail path. Whatever sound you add, will play when"
          " the wail button is pushed. Take a look at the read me for more information.\n")

    brand = input("Enter brand name: ")

    model = input("Enter model: ")

    wail = input("Path to wail (If none, return): ")
    if wail == "":
        wail = dead
    else:
        if check_path(wail):
            pass
        else:
            print("'" + wail + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    yelp = input("Path to yelp (If none, return): ")
    if yelp == "":
        yelp = dead
    else:
        if check_path(yelp):
            pass
        else:
            print("'" + yelp + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    horn = input("Path to horn (If none, return): ")
    if horn == "":
        horn = dead
    else:
        if check_path(horn):
            pass
        else:
            print("'" + horn + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    phaser = input("Path to phaser (If none, return): ")
    if phaser == "":
        phaser = dead
    else:
        if check_path(phaser):
            pass
        else:
            print("'" + phaser + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    aux1 = input("Path to aux1 (If none, return): ")

    if aux1 == "":
        aux1 = dead
    else:
        if check_path(aux1):
            pass

        else:
            print("'" + yelp + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    aux2 = input("Path to aux2 (If none, return): ")
    if aux2 == "":
        aux2 = dead
    else:
        if check_path(aux2):
            pass
        else:
            print("'" + aux2 + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    aux3 = input("Path to aux3 (If none, return): ")
    if aux3 == "":
        aux3 = dead
    else:
        if check_path(aux3):
            pass
        else:
            print("'" + aux3 + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                           " to add.")
            add_siren()

    aux4 = input("Path to aux4 (If none, return): ")
    if aux4 == "":
        aux4 = dead
    else:

        if check_path(aux4):
            pass
        else:
            print("'" + aux4 + "' is not a valid path. Please be sure to add the sound files first, then use this program"
                               " to add.")
            add_siren()

    print([brand, model, wail, yelp, horn, aux1, aux2, aux3, aux4])

    confirm = input("Do you want to add this siren? (y/n): ")

    if confirm == 'y':

        key = "siren" + str(len(config[0]['sirens']) + 1)
        siren = {"name": brand, "model": model, "horn": horn, "phaser": phaser, "wail": wail,
                 "yelp": yelp, "aux1": aux1, "aux2": aux2, "aux3": aux3, "aux4": aux4}

        config[0]["sirens"][key] = siren

        with open('config.json', 'w') as outfile:
                    json.dump(config, outfile, indent=4, sort_keys=True)

    elif confirm == 'n':
        get_command()





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
        if comm == commands[5]:
            add_siren()

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




