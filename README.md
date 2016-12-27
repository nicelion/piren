# Piren
Turn your Raspberry Pi into a siren box for your car! Featuring sirens from Whelen, Code 3, Federal Signal, Galls, and more!

![Siren Logo](https://i.imgur.com/m5sKdwH.png)


- [About](#about)
- [Installation](#installation)
- [Requirements and Prerequisites](#requirements-and-prerequisites)
- [Setup](#setup)
- [Sirens](#sirens)


## About

Piren turns your Raspberry Pi into a siren box, like one you would see in a police car or fire truck. Piren comes with multiple sirens from different siren boxes.

Check us out at [/r/piren](http://www.reddit.com/r/piren) on reddit!


## Installation

Installing Piren is easy, if you already have git installed on your Pi. Which should be pre-installed.
Simply run

```git clone https://github.com/nicelion/piren.git ```

and Piren will be installed! Just like that.

Now you'll need to ```cd``` into the 'piren' directory. You'll then need to run the install script that installs the files that make the LCD work correctly. Enter the following into the terminal:

```./install_lcd_depencedncies.sh```

Wait for it to install, and once you have your buttons and LCD attached to the GPIO pins, run the ```piren.py``` and test to see if it works.

```sudo python3 piren.py```

**NOTE:** You must use

```sudo``` to run ```piren.py```

## Requirements and Prerequisites

Piren has a couple of dependencies that need to be installed before you can use Piren.

#### Software
* PyGame

#### Hardware

* Raspberry Pi 2 or newer
* 16x2 LCD display
* Working buttons attatched to the GPIO pins

## Setup

Piren is really cool, but unfortunately, it can take a while to set up. The software side is easy, as noted above, but the physical aspect of it, can be time consuming. But, this is a Raspberry Pi project, so you have the time.

Piren comes with many sirens installed, as well as some different horns you can use. Piren should be installed on your Raspberry Pi 2 or newer.

You may have to go in and change the pygame mixer initialization so the sirens sound right. If the default setup does not work, try the following two:
```
    pygame.mixer.pre_init(48000, -16, 1, 1024)
    pygame.mixer.pre_init(48000, -16, 1, 512)

```
**Note:** After further inspections, this shouldn't  be a problem anymore.

### Getting Piren to run when the Pi is booted
When you install Piren, you of course are going to want to have Piren run when you first boot up your Pi. Especially because this will be in your car and you won't have a keyboard to run Piren.

You will need to edit the rc.local file to run Piren at start up. Please read [this article](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) for more information. The rc.local file is a shell file that is run every time the Pi is booted.

Run the following command in the terminal:

```sudo nano /etc/rc.local```

(You can use any text editor, I use vim, but for this example, I use nano because that is the most common/)

Nano or vim or whatever text editor you use will open and it should look like this:

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

exit 0

```

You'll then need to add the following after the if statement and before the ```exit 0```:

```
cd /home/pi/piren
sudo python3 piren.py &
```

Obviously if you have changed the directory name, you'll need to edit where you change directory to in the rc.local file. The "&" after the line that executes the python script is so that other processes can run, even before Piren exits, as Piren will not exit until a keyboard interrupt or the pi is shut down.

### Circuitry
The following will be explained using a breadboard, howver, a breadboard should only be used for testing as connections are not always secure. Bumps and rattling from driving around could losen connections, potentially causing sirens to go off when they shouldn't. (Which may get you in legal trouble.)

#### Buttons

The following image is an example of the circuit you need to create for the buttons. Keep in mind, while buying parts, you need to create this exact circuit for every single button and switch.


**HOWEVER: The 100nf capacitor is not needed. If you want to add it, you can, but works just fine without it.**
![button circut](http://raspi.tv/wp-content/uploads/2014/07/both700.png)

This image is not mine, and you can find the article I used, which is really helpful, [here](http://raspi.tv/2014/rpi-gpio-update-and-detecting-both-rising-and-falling-edges), which explains a little more of whats going on in this circuit. You should of course change the GPIO pin to the correct one, which you can read more about, right below.

```
# GPIO Pin Numbers
class pin:
    wail = 25
    horn = 24
    phaser = 18
    yelp = 5
    manual_wail = 27
    siren_led = 12

    # Selection fed_sig_model
    next = 17
    previous = 9

    # Selection Brand
    next_brand = 11
    prev_brand = 8

    # Aux
    aux = 26
    aux_led = 20

```

When you go to make your circuits, just connect the right button, to the right GPIO pin, to recive the function. Below is a YouTube better explain the process.

#### GPIO Pins and Their Preset Functions
If you install Piren, and don't change anything, below are preset pins and their functions. You, of course can change them, if you want. But, if you are installing on a fresh Pi and aren't using the GPIO pins for anything else, it will probably be easier to use the default ones.

## Parts List

These are the parts I used. Obviously, you don't need to get the *exact* buttons and wires I used, but I do recomend them. The LCD I recomend, I strongly recomended. If you buy one thing off line, I recomend it be the LCD. Reason being: it comes with a i2c backpack, which needs to be soldered on. The backpack allows you to only need 4 GPIO pins for use.

I was able to go to a local RadioShack to get most of the buttons. Fortunately, the were going out of business, (kind of sad really) and all there stuff was 60% off. After following these links, the seem to be sold out online, but they should be available at your RadioShack.

- [RadioShack Momentary Pushbutton Switches (2-Pack) | $3.99](https://www.radioshack.com/collections/switches/products/pk2-spst-push-sw) x2. (I used these to switch the brand and models)
- [RadioShack SQ No Push Switch | $3.49](https://www.radioshack.com/collections/switches/products/sq-no-push-switch) x4 (Used for the phaser and wails and other sirens.)
- [RadioShack SPST RED Switch | $3.49](https://www.radioshack.com/collections/switches/products/spst-red-switch) x1 (Used for the horn)
- [RadioShack Pushon/Pushoff Switch | $3.99](https://www.radioshack.com/collections/switches/products/pushon-pushoff-sw) x1 (Used as the modifier for multiple sirens.)
- [RadioShack SPST Micromini Switch | $4.49](https://www.radioshack.com/collections/switches/products/spst-micromini-sw) x1 (Used for the wail loop)

## Sirens

Piren comes loaded with many sirens that are perfectly looped and from various different brands. Below is a list of all the sirens Piren has. Special thanks to crazytaxi1000 from LCPDFR.com for providinng the sirens. You can visit his LCPDFR profile [here](http://www.lcpdfr.com/profile/167825-crazytaxi1000/) and view the [United States Siren Mega Pack](http://www.lcpdfr.com/files/file/13561-united-states-siren-mega-pack-for-sirenmastery-54-siren-models/?&tab=comments#comment-123187) on LCPDFR's website. Again, a huge thanks to him for providing the sirens!

#### Code 3
- 3932 Scorpion
- Mastercom
- Mastercom B
- RLS
- Vcon

#### Federal Signal
- EQ2B
- MS4000
- PA15
- PA20
- PA150 
- PA200
- PA300
- PA500
- PA640
- PA4000
- SS200 Mini
- SS2000SM Smart Siren
- SSP3000b Smart Siren Platinum
- SSP3000b with Rumbler
- Touchmaster_Touchmaster Delta
- Unitrol 80k
- Unitrol 8001
- Unitrol Omega 90

#### Galls
- ST160 Street Thunder
- ST300 Command Center

#### Whelen
- 295HF100
- 295HFSA1
- 295HFSA6
- 295SDSA1
- 295SLSA1
- 295SLSA6
- Alpha
- Alpha 22m Mechanical
- Beta
- Cencom Gold
- Cencom Sapphire
- Cencom Sapphire Howler
- Epsilon EPSL-1
- Gamma 2 (Issue with the yelp siren, so it is not used.)

#### Other

##### Sirens
- AS350 Helicopter Siren
- Carson SA441
- North American SI100M
- Powercall DX5
- Unitrol 480k

##### Horns
- Train Horn
- Air Horn
- Rap Air Horn
- Dixie Horn
- GTA 4 Horn as seen in GTAV
- Sad Trombone as seen in GTAV
- Ice Cream Truck Song

