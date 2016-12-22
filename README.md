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


## Installation

``` not avalible```

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
- Gamma 2

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

