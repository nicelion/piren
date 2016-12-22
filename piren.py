# piren.py
#
# by Ian Thompson on 12/2/16
# Part of the Piren Project
#
# (c) 2016 Ian Thompson
#

import pygame
import sirens
import RPi.GPIO as GPIO
from time import sleep
import setup
from collections import deque
import lcddriver


# Initialize game engine
pygame.mixer.pre_init(44100, -16, 2, 512)  # See READEME.md for more information
pygame.init()
pygame.mixer.init()
display = lcddriver.lcd()

dead = 'dead.wav'

brand = deque([1,0])
fed_sig_model = deque([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
code_3_model = deque([1, 0, 0, 0, 0])

auxiliary = False

CODE_3 = 'CODE_3'
FED_SIG = 'FED_SIG'
GALLS = 'GALlS'
WHELEN = 'WHELEN'
OTHER = 'OTHER'
HORNS = 'HORNS'


def set_brand():
    if brand[0] == 1:
        return CODE_3
    elif brand[1] == 1:
        return FED_SIG
    elif brand[2] == 1:
        return GALLS
    elif brand[3] == 1:
        return WHELEN
    elif brand[4] == 1:
        return OTHER
    elif brand[5] == 1:
        return HORNS



def set_wail():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return sirens.Code_3._3932_Scorpion.wail()
        if code_3_model[1] == 1:
            return sirens.Code_3.Mastercom.wail()
        if code_3_model[2] == 1:
            return sirens.Code_3.Mastercom_B.wail()
        if code_3_model[3] == 1:
            return sirens.Code_3.RLS.wail()
        if code_3_model[4] == 1:
            return sirens.Code_3.Vcon.wail()
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return sirens.Federal_Signal.EQ2B.wail()
        if fed_sig_model[1] == 1:
            return sirens.Federal_Signal.MS4000.wail()
        if fed_sig_model[2] == 1:
            return sirens.Federal_Signal.PA20.wail()
        if fed_sig_model[3] == 1:
            return sirens.Federal_Signal.PA150.wail()
        if fed_sig_model[4] == 1:
            return sirens.Federal_Signal.PA300.wail()
        if fed_sig_model[5] == 1:
            return sirens.Federal_Signal.PA640.wail()
        if fed_sig_model[6] == 1:
            return sirens.Federal_Signal.PA4000.wail()
        if fed_sig_model[7] == 1:
            return sirens.Federal_Signal.SS200_Mini.wail()
        if fed_sig_model[8] == 1:
            return sirens.Federal_Signal.SS2000SM.wail()
        if fed_sig_model[9] == 1:
            return sirens.Federal_Signal.SSP3000b.wail()
        if fed_sig_model[10] == 1:
            return sirens.Federal_Signal.SSP3000b_w_Rumbler.wail()
        if fed_sig_model[11] == 1:
            return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.wail()
def set_horn():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return sirens.Code_3._3932_Scorpion.horn()
        if code_3_model[1] == 1:
            return sirens.Code_3.Mastercom.horn()
        if code_3_model[2] == 1:
            return sirens.Code_3.Mastercom_B.horn()
        if code_3_model[3] == 1:
            return sirens.Code_3.RLS.horn()
        if code_3_model[4] == 1:
            return sirens.Code_3.Vcon.horn()
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return sirens.Federal_Signal.EQ2B.horn()
        if fed_sig_model[1] == 1:
            return sirens.Federal_Signal.MS4000.horn()
        if fed_sig_model[2] == 1:
            return sirens.Federal_Signal.PA20.horn()
        if fed_sig_model[3] == 1:
            return dead
        if fed_sig_model[4] == 1:
            return sirens.Federal_Signal.PA300.horn()
        if fed_sig_model[5] == 1:
            return sirens.Federal_Signal.PA640.horn()
        if fed_sig_model[6] == 1:
            return sirens.Federal_Signal.PA4000.horn()
        if fed_sig_model[7] == 1:
            return sirens.Federal_Signal.SS200_Mini.horn()
        if fed_sig_model[8] == 1:
            return sirens.Federal_Signal.SS2000SM.horn()
        if fed_sig_model[9] == 1:
            return sirens.Federal_Signal.SSP3000b.horn()
        if fed_sig_model[10] == 1:
            return sirens.Federal_Signal.SSP3000b_w_Rumbler.horn()
        if fed_sig_model[11] == 1:
            return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.horn()

def set_yelp():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return sirens.Code_3._3932_Scorpion.yelp()
        if code_3_model[1] == 1:
            return sirens.Code_3.Mastercom.yelp()
        if code_3_model[2] == 1:
            return sirens.Code_3.Mastercom_B.yelp()
        if code_3_model[3] == 1:
            return sirens.Code_3.RLS.yelp()
        if code_3_model[4] == 1:
            return sirens.Code_3.Vcon.yelp()
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return sirens.Federal_Signal.EQ2B.yelp()
        if fed_sig_model[1] == 1:
            return sirens.Federal_Signal.MS4000.yelp()
        if fed_sig_model[2] == 1:
            return sirens.Federal_Signal.PA20.yelp()
        if fed_sig_model[3] == 1:
            return sirens.Federal_Signal.PA150.yelp()
        if fed_sig_model[4] == 1:
            return sirens.Federal_Signal.PA300.yelp()
        if fed_sig_model[5] == 1:
            return sirens.Federal_Signal.PA640.yelp()
        if fed_sig_model[6] == 1:
            return sirens.Federal_Signal.PA4000.yelp()
        if fed_sig_model[7] == 1:
            return sirens.Federal_Signal.SS200_Mini.yelp()
        if fed_sig_model[8] == 1:
            return sirens.Federal_Signal.SS2000SM.yelp()
        if fed_sig_model[9] == 1:
            return sirens.Federal_Signal.SSP3000b.yelp()
        if fed_sig_model[10] == 1:
            return sirens.Federal_Signal.SSP3000b_w_Rumbler.yelp()
        if fed_sig_model[11] == 1:
            return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.yelp()

def set_phaser():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return sirens.Code_3._3932_Scorpion.phaser()
        if code_3_model[1] == 1:
            return sirens.Code_3.Mastercom.phaser()
        if code_3_model[2] == 1:
            return sirens.Code_3.Mastercom_B.phaser()
        if code_3_model[3] == 1:
            return sirens.Code_3.RLS.phaser()
        if code_3_model[4] == 1:
            return sirens.Code_3.Vcon.phaser()
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return sirens.Federal_Signal.EQ2B.phaser()
        if fed_sig_model[1] == 1:
            return sirens.Federal_Signal.MS4000.phaser()
        if fed_sig_model[2] == 1:
            return sirens.Federal_Signal.PA20.hilo()
        if fed_sig_model[3] == 1:
            return sirens.Federal_Signal.PA150.hilo()
        if fed_sig_model[4] == 1:
            return sirens.Federal_Signal.PA300.phaser()
        if fed_sig_model[5] == 1:
            return sirens.Federal_Signal.PA640.phaser()
        if fed_sig_model[6] == 1:
            return sirens.Federal_Signal.PA4000.phaser()
        if fed_sig_model[7] == 1:
            return dead
        if fed_sig_model[8] == 1:
            return sirens.Federal_Signal.SS2000SM.phaser()
        if fed_sig_model[9] == 1:
            return sirens.Federal_Signal.SSP3000b.phaser()
        if fed_sig_model[10] == 1:
            return sirens.Federal_Signal.SSP3000b_w_Rumbler.phaser()
        if fed_sig_model[11] == 1:
            return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.phaser()

def set_aux1():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return [dead, False]
        if code_3_model[1] == 1:
            return [dead, False]
        if code_3_model[2] == 1:
            print('actuals')
            return [sirens.Code_3.Mastercom_B.hilo(), True]
        if code_3_model[3] == 1:
            return [dead, False]
        if code_3_model[4] == 1:
            return [dead, False]
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return [dead, False]
        if fed_sig_model[1] == 1:
            return [dead, False]
        if fed_sig_model[2] == 1:
            return [sirens.Federal_Signal.PA20.yelp2(), True]
        if fed_sig_model[3] == 1:
            return [dead, False]
        if fed_sig_model[4] == 1:
            return [sirens.Federal_Signal.PA300.hilo(), True]
        if fed_sig_model[5] == 1:
            return [dead, False]
        if fed_sig_model[6] == 1:
            return [dead, False]
        if fed_sig_model[7] == 1:
            return [dead, False]
        if fed_sig_model[8] == 1:
            return [sirens.Federal_Signal.SS2000SM.hilo(), False]
        if fed_sig_model[9] == 1:
            return [sirens.Federal_Signal.SSP3000b.hilo(), False]
        if fed_sig_model[10] == 1:
            return [dead, False]
def set_aux2():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return [dead, False]
        if code_3_model[1] == 1:
            return [dead, False]
        if code_3_model[2] == 1:
            return [sirens.Code_3.Mastercom_B.hylo(), True]
        if code_3_model[3] == 1:
            return [dead, False]
        if code_3_model[4] == 1:
            return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return [dead, False]
        elif fed_sig_model[1] == 1:
            return [dead, False]
        elif fed_sig_model[2] == 1:
            return [sirens.Federal_Signal.PA20.yelp3(), True]
        elif fed_sig_model[3] == 1:
            return [dead, False]
        elif fed_sig_model[4] == 1:
            return [dead, False]
        if fed_sig_model[5] == 1:
            return [dead, False]
        if fed_sig_model[6] == 1:
            return [dead, False]
        if fed_sig_model[7] == 1:
            return [dead, False]
        if fed_sig_model[8] == 1:
            return [dead, False]
        if fed_sig_model[9] == 1:
            return [dead, False]
        if fed_sig_model[10] == 1:
            return [dead, False]
def set_aux3():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return [dead, False]
        if code_3_model[1] == 1:
            return [dead, False]
        if code_3_model[2] == 1:
            return [dead, False]
        if code_3_model[3] == 1:
            return [dead, False]
        if code_3_model[4] == 1:
            return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return [dead, False]
        elif fed_sig_model[1] == 1:
            return [dead, False]
        elif fed_sig_model[2] == 1:
            return [dead, False]
        elif fed_sig_model[3] == 1:
            return [dead, False]
        elif fed_sig_model[4] == 1:
            return [dead, False]
        if fed_sig_model[5] == 1:
            return [dead, False]
        if fed_sig_model[6] == 1:
            return [dead, False]
        if fed_sig_model[7] == 1:
            return [dead, False]
        if fed_sig_model[8] == 1:
            return [dead, False]
        if fed_sig_model[9] == 1:
            return [dead, False]
        if fed_sig_model[10] == 1:
            return [dead, False]
def set_aux4():
    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            return [dead, False]
        if code_3_model[1] == 1:
            return [dead, False]
        if code_3_model[2] == 1:
            return [dead, False]
        if code_3_model[3] == 1:
            return [dead, False]
        if code_3_model[4] == 1:
            return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            return [dead, False]
        elif fed_sig_model[1] == 1:
            return [dead, False]
        elif fed_sig_model[2] == 1:
            return [dead, False]
        elif fed_sig_model[3] == 1:
            return [dead, False]
        elif fed_sig_model[4] == 1:
            return [dead, False]
        if fed_sig_model[5] == 1:
            return [dead, False]
        if fed_sig_model[6] == 1:
            return [dead, False]
        if fed_sig_model[7] == 1:
            return [dead, False]
        if fed_sig_model[8] == 1:
            return [dead, False]
        if fed_sig_model[9] == 1:
            return [dead, False]
        if fed_sig_model[10] == 1:
            return [dead, False]

brand_name = set_brand()


def set_lcd():
    display.lcd_clear()
    set_brand()
    if brand_name == CODE_3:
        display.lcd_display_string('     Code 3', 1)
    elif brand_name == FED_SIG:
        display.lcd_display_string(' Federal Signal', 1)
    elif brand_name == GALLS:
        display.lcd_display_string('Galls', 1)
    elif brand_name == WHELEN:
        display.lcd_display_string('Whelen', 1)
    elif brand_name == OTHER:
        display.lcd_display_string('Other', 1)
    elif brand_name == HORNS:
        display.lcd_display_string('Horns', 1)

    if brand_name == CODE_3:
        if code_3_model[0] == 1:
            display.lcd_display_string(" 3932  Scorpion", 2)
        if code_3_model[1] == 1:
            display.lcd_display_string("   Mastercom", 2)
        if code_3_model[2] == 1:
            display.lcd_display_string("  Mastercom B", 2)
        if code_3_model[3] == 1:
            display.lcd_display_string("      RLS", 2)
        if code_3_model[4] == 1:
            display.lcd_display_string("      Vcon", 2)
    if brand_name == FED_SIG:
        if fed_sig_model[0] == 1:
            display.lcd_display_string("      EQ2B", 2)
        if fed_sig_model[1] == 1:
            display.lcd_display_string("    MS4000", 2)
        if fed_sig_model[2] == 1:
            display.lcd_display_string("      PA20", 2)
        if fed_sig_model[3] == 1:
            display.lcd_display_string("     PA150", 2)
        if fed_sig_model[4] == 1:
            display.lcd_display_string("     PA300", 2)
        if fed_sig_model[5] == 1:
            display.lcd_display_string("     PA640", 2)
        if fed_sig_model[6] == 1:
            display.lcd_display_string("    PA40000", 2)
        if fed_sig_model[7] == 1:
            display.lcd_display_string("   SS200 Mini", 2)
        if fed_sig_model[8] == 1:
            display.lcd_display_string("    SS2000SM", 2)
        if fed_sig_model[9] == 1:
            display.lcd_display_string("    SSP3000b", 2)
        if fed_sig_model[10] == 1:
            display.lcd_display_string("SSP3000b w Rumbler", 2)

horn = pygame.mixer.Sound(set_horn())
wail = pygame.mixer.Sound(set_wail())
m_wail = pygame.mixer.Sound(set_wail())
yelp = pygame.mixer.Sound(set_yelp())
phaser = pygame.mixer.Sound(set_phaser())

aux1 = pygame.mixer.Sound(set_aux1()[0])
aux1_is_usable = set_aux1()[1]
aux2 = pygame.mixer.Sound(set_aux2()[0])
aux2_is_usable = set_aux2()[1]
aux3 = pygame.mixer.Sound(set_aux3()[0])
aux3_is_usable = set_aux3()[1]
aux4 = pygame.mixer.Sound(set_aux4()[0])
aux4_is_usable = set_aux4()[1]

# GPIO Pin Numbers
class pin:
    # Sets up the pin numbers for what each button will do.
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

    aux = 26
    aux_led = 20
    



wail_playing = False
horn_playing = False
yelp_playing = False
phaser_playing = False
manual_wail_playing = False



# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin.wail, GPIO.IN)
GPIO.setup(pin.horn, GPIO.IN)
GPIO.setup(pin.phaser, GPIO.IN)
GPIO.setup(pin.yelp, GPIO.IN)
GPIO.setup(pin.manual_wail, GPIO.IN)
GPIO.setup(pin.siren_led, GPIO.OUT)
GPIO.setup(pin.next, GPIO.IN)
GPIO.setup(pin.previous, GPIO.IN)
GPIO.setup(pin.next_brand, GPIO.IN)
GPIO.setup(pin.prev_brand, GPIO.IN)
GPIO.setup(pin.aux, GPIO.IN)
GPIO.setup(pin.aux_led, GPIO.OUT)



def play_wail(channel):
    global wail_playing
    if GPIO.input(pin.wail) and not wail_playing:
        wail.play(-1)
        wail_playing = True

    else:
        wail.stop()
        wail_playing = False


def play_horn(channel):
    global horn_playing
    if GPIO.input(pin.horn) and not horn_playing:
        if auxiliary and aux1_is_usable:
            aux1.play(-1)
        else:
            horn.play(-1)
            wail.set_volume(0.25)
            horn_playing = True
    else:
        if auxiliary and aux1_is_usable:
            aux1.stop()
        else:
            horn.stop()
            wail.set_volume(1)
            horn_playing = False


def play_phaser(channel):
    global phaser_playing
    if GPIO.input(pin.phaser) and not phaser_playing:
        if auxiliary and aux2_is_usable:
            aux2.play(-1)
        else:
            phaser.play(-1)
            wail.set_volume(0.25)
            phaser_playing = True
    else:
        if auxiliary and aux2_is_usable:
            aux2.stop()
        else:
            phaser.stop()
            wail.set_volume(1)
            phaser_playing = False


def play_yelp(channel):
    global yelp_playing
    if GPIO.input(pin.yelp) and not yelp_playing:
        if wail_playing:
            wail.stop()
        yelp.play(-1)
        wail.set_volume(0)
        yelp_playing = True
    else:
        if wail_playing:
            wail.play(-1)
        yelp.stop()
        wail.set_volume(1)
        yelp_playing = False


def play_manual_wail(channel):
    global manual_wail_playing, wail_playing
    if GPIO.input(pin.manual_wail) and not manual_wail_playing and not wail_playing:
        m_wail.play(-1)
        manual_wail_playing = True
    else:
        m_wail.stop()
        manual_wail_playing = False


# Menu Controllers

def next_selection(channel):
    if GPIO.input(pin.next):
        global horn, wail, m_wail, yelp, phaser, lcd_string, brand_name, aux1, aux1_is_usable, aux2, aux2_is_usable
        global aux3, aux3_is_usable, aux4, aux4_is_usable
        if brand_name == FED_SIG:
            fed_sig_model.rotate(1)
            print('rotated fed sig 1')
        elif brand_name == CODE_3:
            code_3_model.rotate(1)
            print('rotated code 3 1')

        # # print(setup.fed_sig_model)
        wail.stop()
        horn.stop()
        m_wail.stop()
        yelp.stop()
        phaser.stop()
        horn = pygame.mixer.Sound(set_horn())
        wail = pygame.mixer.Sound(set_wail())
        m_wail = pygame.mixer.Sound(set_wail())
        yelp = pygame.mixer.Sound(set_yelp())
        phaser = pygame.mixer.Sound(set_phaser())

        aux1 = pygame.mixer.Sound(set_aux1()[0])
        aux1_is_usable = set_aux1()[1]
        aux2 = pygame.mixer.Sound(set_aux2()[0])
        aux2_is_usable = set_aux2()[1]
        aux3 = pygame.mixer.Sound(set_aux3()[0])
        aux3_is_usable = set_aux3()[1]
        aux4 = pygame.mixer.Sound(set_aux4()[0])
        aux4_is_usable = set_aux4()[1]

        set_lcd()



def prev_selection(channel):
    if GPIO.input(pin.previous):
        global horn, wail, m_wail, yelp, phaser, lcd_string, brand_name, aux1, aux1_is_usable, aux2, aux2_is_usable
        global aux3, aux3_is_usable, aux4, aux4_is_usable
        if brand_name == FED_SIG:
            fed_sig_model.rotate(-1)
            print('rotated fed sig -1')
        elif brand_name == CODE_3:
            code_3_model.rotate(-1)
            print('rotated code 3 -1')

        wail.stop()
        horn.stop()
        m_wail.stop()
        yelp.stop()
        phaser.stop()
        horn = pygame.mixer.Sound(set_horn())
        wail = pygame.mixer.Sound(set_wail())
        m_wail = pygame.mixer.Sound(set_wail())
        yelp = pygame.mixer.Sound(set_yelp())
        phaser = pygame.mixer.Sound(set_phaser())

        aux1 = pygame.mixer.Sound(set_aux1()[0])
        aux1_is_usable = set_aux1()[1]
        aux2 = pygame.mixer.Sound(set_aux2()[0])
        aux2_is_usable = set_aux2()[1]
        aux3 = pygame.mixer.Sound(set_aux3()[0])
        aux3_is_usable = set_aux3()[1]
        aux4 = pygame.mixer.Sound(set_aux4()[0])
        aux4_is_usable = set_aux4()[1]

        set_lcd()

def next_brand(channel):
    if GPIO.input(pin.next_brand):
        brand.rotate(1)

        global horn, wail, m_wail, yelp, phaser, lcd_string, brand_name, aux1, aux1_is_usable, aux2, aux2_is_usable
        global aux3, aux3_is_usable, aux4, aux4_is_usable
        brand_name = set_brand()

        wail.stop()
        horn.stop()
        m_wail.stop()
        yelp.stop()
        phaser.stop()
        horn = pygame.mixer.Sound(set_horn())
        wail = pygame.mixer.Sound(set_wail())
        m_wail = pygame.mixer.Sound(set_wail())
        yelp = pygame.mixer.Sound(set_yelp())
        phaser = pygame.mixer.Sound(set_phaser())

        aux1 = pygame.mixer.Sound(set_aux1()[0])
        aux1_is_usable = set_aux1()[1]
        aux2 = pygame.mixer.Sound(set_aux2()[0])
        aux2_is_usable = set_aux2()[1]
        aux3 = pygame.mixer.Sound(set_aux3()[0])
        aux3_is_usable = set_aux3()[1]
        aux4 = pygame.mixer.Sound(set_aux4()[0])
        aux4_is_usable = set_aux4()[1]


        set_lcd()
        set_brand()




        print(brand)

def prev_brand(channel):
    if GPIO.input(pin.prev_brand):
        brand.rotate(-1)

        global horn, wail, m_wail, yelp, phaser, lcd_string, brand_name, aux1, aux1_is_usable, aux2, aux2_is_usable
        global aux3, aux3_is_usable, aux4, aux4_is_usable
        brand_name = set_brand()

        wail.stop()
        horn.stop()
        m_wail.stop()
        yelp.stop()
        phaser.stop()
        horn = pygame.mixer.Sound(set_horn())
        wail = pygame.mixer.Sound(set_wail())
        m_wail = pygame.mixer.Sound(set_wail())
        yelp = pygame.mixer.Sound(set_yelp())
        phaser = pygame.mixer.Sound(set_phaser())

        aux1 = pygame.mixer.Sound(set_aux1()[0])
        aux1_is_usable = set_aux1()[1]
        aux2 = pygame.mixer.Sound(set_aux2()[0])
        aux2_is_usable = set_aux2()[1]
        aux3 = pygame.mixer.Sound(set_aux3()[0])
        aux3_is_usable = set_aux3()[1]
        aux4 = pygame.mixer.Sound(set_aux4()[0])
        aux4_is_usable = set_aux4()[1]

        set_lcd()
        set_brand()
        print(brand)

def set_auxillary(channel):
    global auxiliary

    if GPIO.input(pin.aux):
        auxiliary = True
        GPIO.output(pin.aux_led, GPIO.HIGH)

    else:
        auxiliary = False
        GPIO.output(pin.aux_led, GPIO.LOW)

GPIO.add_event_detect(pin.wail, GPIO.BOTH, callback=play_wail)
GPIO.add_event_detect(pin.horn, GPIO.BOTH, callback=play_horn)
GPIO.add_event_detect(pin.phaser, GPIO.BOTH, callback=play_phaser)
GPIO.add_event_detect(pin.yelp, GPIO.BOTH, callback=play_yelp)
GPIO.add_event_detect(pin.manual_wail, GPIO.BOTH, callback=play_manual_wail)

GPIO.add_event_detect(pin.next, GPIO.RISING, callback=next_selection, bouncetime=150)
GPIO.add_event_detect(pin.previous, GPIO.RISING, callback=prev_selection, bouncetime=150)

GPIO.add_event_detect(pin.next_brand, GPIO.RISING, callback=next_brand, bouncetime=300)
GPIO.add_event_detect(pin.prev_brand, GPIO.RISING, callback=prev_brand, bouncetime=300)
GPIO.add_event_detect(pin.aux, GPIO.BOTH, callback=set_auxillary)


def startup():
    display.lcd_display_string('   Welcome to', 1)
    display.lcd_display_string('     Piren', 2)

    print('Welcome to the Piren Project \nby Ian Thompson \n \nSirens provided by crazytaxi1000 from LCPDFR.com!')

    GPIO.output(pin.siren_led, GPIO.HIGH)
    GPIO.output(pin.aux_led, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(pin.siren_led, GPIO.LOW)
    GPIO.output(pin.aux_led, GPIO.LOW)
    sleep(0.1)
    GPIO.output(pin.siren_led, GPIO.HIGH)
    GPIO.output(pin.aux_led, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(pin.siren_led, GPIO.LOW)
    GPIO.output(pin.aux_led, GPIO.LOW)
    sleep(0.1)
    GPIO.output(pin.aux_led, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(pin.aux_led, GPIO.LOW)
    GPIO.output(pin.siren_led, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(pin.aux_led, GPIO.HIGH)
    GPIO.output(pin.siren_led, GPIO.LOW)
    sleep(0.1)
    GPIO.output(pin.aux_led, GPIO.LOW)
    GPIO.output(pin.siren_led, GPIO.LOW)
    display.lcd_clear()


try:
    print('Piren Started')
    startup()
    set_lcd()
    set_brand()
    while True:
        # When a siren, or multiple sirens, are playing, a led, of your color choice, will appear until the siren is
        # turned off. This acts as an indicator so that if for some reason, you are driving down the road and cant hear
        # the siren playing, you can easily be notified via the led.
        if wail_playing or yelp_playing or phaser_playing or manual_wail_playing:
            GPIO.output(pin.siren_led, GPIO.HIGH)
        else:
            GPIO.output(pin.siren_led, GPIO.LOW)

        set_brand()



        sleep(0.01)




except KeyboardInterrupt:
    display.lcd_clear()

finally:
    display.lcd_clear()
    GPIO.cleanup()

