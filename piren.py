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
import horns


# Initialize
pygame.mixer.pre_init(44100, -16, 1, 512)  # See READEME.md for more information, however, this shouldn't be a problem
pygame.init()
pygame.mixer.init()
display = lcddriver.lcd()

# 'dead.wav' is a wav file, obviously, that has no sound. This is used when some siren models do not
# have certain sounds. For example, some siren models do not have a horn. So, when the horn button is
# pushed, the seemingly empty wav file is played. With out this, an error would be thrown.
dead = 'dead.wav'


# Brand and model information are put in a deque. Then, in the 'set_...' functions, seen below, the
# appropriate sounds can be set for each type of siren. Why deques might you ask? Good question.
# If you look below at the 'prev_...' or 'next_...' towards the bottom, you can see the 1 can be
# moved 1 or -1 just by using the deque.rotate() function. This is extremely easier than using a
# simple list.
#
# The one in the deque represents the active brand or model. See the 'set_...' functions below for a
# little more information
brand = deque([1, 0, 0, 0, 0, 0, 0])
fed_sig_model = deque([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
code_3_model = deque([1, 0, 0, 0, 0])
galls_model = deque([1, 0])
whelen_model = deque([1, 0, 0, 0, 0, 0, 0, 0, 0])
feniex_model = deque([1, 0])
other_model = deque([1, 0, 0, 0, 0, 0, 0, 0])
horns_model = deque([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

auxiliary = False

CODE_3 = 'CODE_3'
FED_SIG = 'FED_SIG'
GALLS = 'GALlS'
WHELEN = 'WHELEN'
OTHER = 'OTHER'
HORNS = 'HORNS'
FENIEX = 'FENIEX'

def set_brand():  # Sets the brand name for the selected siren. See above.
    if brand[0] == 1:
        return CODE_3
    elif brand[1] == 1:
        return FED_SIG
    elif brand[2] == 1:
        return GALLS
    elif brand[3] == 1:
        return WHELEN
    elif brand[4] == 1:
        return FENIEX
    elif brand[5] == 1:
        return OTHER
    elif brand[6] == 1:
        return HORNS


def set_wail():  # Sets what siren will be used for wail.
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
        if fed_sig_model[12] == 1:
            return sirens.Federal_Signal.Unitrol_80k.wail()
        if fed_sig_model[13] == 1:
            return sirens.Federal_Signal.Unitrol_8001.wail()
        if fed_sig_model[14] == 1:
            return sirens.Federal_Signal.Unitrol_Omega_90.wail()
    if brand_name == GALLS:
        if galls_model[0] == 1:
            return sirens.Galls.ST160_Street_Thunder.wail()
        if galls_model[1] == 1:
            return sirens.Galls.ST300_Command_Center.wail()
    if brand_name == WHELEN:
        if whelen_model[0] == 1:
            return sirens.Whelen._295HF100.wail()
        if whelen_model[1] == 1:
            return sirens.Whelen.Alpha.wail()
        if whelen_model[2] == 1:
            return sirens.Whelen.Alpha_22m.wail()
        if whelen_model[3] == 1:
            return sirens.Whelen.Beta.wail()
        if whelen_model[4] == 1:
            return sirens.Whelen.Cencom_Gold.wail()
        if whelen_model[5] == 1:
            return sirens.Whelen.Cencom_Sapphire.wail()
        if whelen_model[6] == 1:
            return sirens.Whelen.Cencom_Sapphire_Howler.wail()
        if whelen_model[7] == 1:
            return sirens.Whelen.Epsilon_EPSL_1.wail()
        if whelen_model[8] == 1:
            return sirens.Whelen.Gamma_2.wail()
    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            return sirens.Feniex.Storm_100w.wail()
        elif feniex_model[1] == 1:
            return sirens.Feniex.Storm_Pro.wail()
    if brand_name == OTHER:
        if other_model[0] == 1:
            return sirens.Other.AS350_Heli.siren()
        elif other_model[1] == 1:
            return sirens.Other.Carson_SA441.wail()
        elif other_model[2] == 1:
            return sirens.Other.NA_SI100M.wail()
        elif other_model[3] == 1:
            return sirens.Other.Powercall_DX5.wail()
        elif other_model[4] == 1:
            return sirens.Other.Unitrol_480k.wail()
        elif other_model[5] == 1:
            return sirens.Other.CHP_Moto_Sirens.wail()
        elif other_model[6] == 1:
            return sirens.Other.Mototola_Spectra.wail()
        elif other_model[7] == 1:
            return sirens.Other.Tomar_940.wail()
        else:
            return dead
    if brand_name == HORNS:
        if horns_model[0] == 1:
            return horns.dixie_horn()
        if horns_model[1] == 1:
            return horns.GTA4_Horn()
        if horns_model[2] == 1:
            return horns.ice_cream()
        if horns_model[3]:
            return horns.bad_boys()
        if horns_model[4] == 1:
            return horns.ecto1()
        if horns_model[5] == 1:
            return horns.move()
        if horns_model[6] == 1:
            return horns.pull_over()
        if horns_model[7] == 1:
            return horns.rap_horn()
        if horns_model[8] == 1:
            return horns.trombone()
        if horns_model[9] == 1:
            return horns.train_horn()
        if horns_model[10] == 1:
            return horns.horn()



def set_horn():  # Sets which sound will be used for the horn.
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
        if fed_sig_model[12] == 1:
            return sirens.Federal_Signal.Unitrol_80k.horn()
        if fed_sig_model[13] == 1:
            return sirens.Federal_Signal.Unitrol_8001.horn()
        if fed_sig_model[14] == 1:
            return sirens.Federal_Signal.Unitrol_Omega_90.horn()
    if brand_name == GALLS:
        if galls_model[0] == 1:
            return sirens.Galls.ST160_Street_Thunder.horn()
        if galls_model[1] == 1:
            return sirens.Galls.ST300_Command_Center.horn()
    if brand_name == WHELEN:
        if whelen_model[0] == 1:
            return sirens.Whelen._295HF100.horn()
        if whelen_model[1] == 1:
            return sirens.Whelen.Alpha.horn()
        if whelen_model[2] == 1:
            return sirens.Whelen.Alpha_22m.horn()
        if whelen_model[3] == 1:
            return sirens.Whelen.Beta.horn()
        if whelen_model[4] == 1:
            return sirens.Whelen.Cencom_Gold.horn()
        if whelen_model[5] == 1:
            return sirens.Whelen.Cencom_Sapphire.horn()
        if whelen_model[6] == 1:
            return sirens.Whelen.Cencom_Sapphire_Howler.horn()
        if whelen_model[7] == 1:
            return sirens.Whelen.Epsilon_EPSL_1.horn()
        if whelen_model[8] == 1:
            return sirens.Whelen.Gamma_2.horn()
    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            return sirens.Feniex.Storm_100w.horn()
        elif feniex_model[1] == 1:
            return sirens.Feniex.Storm_Pro.horn()
    if brand_name == OTHER:
        if other_model[1] == 1:
            return sirens.Other.Carson_SA441.horn()
        elif other_model[2] == 1:
            return sirens.Other.NA_SI100M.hilo()
        elif other_model[3] == 1:
            return sirens.Other.Powercall_DX5.horn()
        elif other_model[4] == 1:
            return sirens.Other.Unitrol_480k.horn()
        elif other_model[6] == 1:
            return sirens.Other.Mototola_Spectra.horn()
        elif other_model[7] == 1:
            return sirens.Other.Tomar_940.horn()
        else:
            return dead
    if brand_name == HORNS:
        if horns_model[0] == 1:
            return horns.dixie_horn()
        if horns_model[1] == 1:
            return horns.GTA4_Horn()
        if horns_model[2] == 1:
            return horns.ice_cream()
        if horns_model[3]:
            return horns.bad_boys()
        if horns_model[4] == 1:
            return horns.ecto1()
        if horns_model[5] == 1:
            return horns.move()
        if horns_model[6] == 1:
            return horns.pull_over()
        if horns_model[7] == 1:
            return horns.rap_horn()
        if horns_model[8] == 1:
            return horns.trombone()
        if horns_model[9] == 1:
            return horns.train_horn()
        if horns_model[10] == 1:
            return horns.horn()


def set_yelp():  # Sets which sound will be used for yelp
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
        if fed_sig_model[12] == 1:
            return sirens.Federal_Signal.Unitrol_80k.yelp()
        if fed_sig_model[13] == 1:
            return sirens.Federal_Signal.Unitrol_8001.yelp()
        if fed_sig_model[14] == 1:
            return sirens.Federal_Signal.Unitrol_Omega_90.yelp()
    if brand_name == GALLS:
        if galls_model[0] == 1:
            return sirens.Galls.ST160_Street_Thunder.yelp()
        if galls_model[1] == 1:
            return sirens.Galls.ST300_Command_Center.yelp()
    if brand_name == WHELEN:
        if whelen_model[0] == 1:
            return sirens.Whelen._295HF100.yelp()
        if whelen_model[1] == 1:
            return sirens.Whelen.Alpha.yelp()
        if whelen_model[2] == 1:
            return sirens.Whelen.Alpha_22m.power_call()
        if whelen_model[3] == 1:
            return sirens.Whelen.Beta.yelp()
        if whelen_model[4] == 1:
            return sirens.Whelen.Cencom_Gold.yelp()
        if whelen_model[5] == 1:
            return sirens.Whelen.Cencom_Sapphire.yelp()
        if whelen_model[6] == 1:
            return sirens.Whelen.Cencom_Sapphire_Howler.yelp()
        if whelen_model[7] == 1:
            return sirens.Whelen.Epsilon_EPSL_1.yelp()
        if whelen_model[8] == 1:
            return sirens.Whelen.Gamma_2.warble()
    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            return sirens.Feniex.Storm_100w.yelp()
        elif feniex_model[1] == 1:
            return sirens.Feniex.Storm_Pro.yelp()
    if brand_name == OTHER:
        if other_model[1] == 1:
            return sirens.Other.Carson_SA441.yelp()
        elif other_model[2] == 1:
            return sirens.Other.NA_SI100M.yelp()
        elif other_model[3] == 1:
            return sirens.Other.Powercall_DX5.yelp()
        elif other_model[4] == 1:
            return sirens.Other.Unitrol_480k.yelp()
        elif other_model[5] == 1:
            return sirens.Other.CHP_Moto_Sirens.yelp()
        elif other_model[6] == 1:
            return sirens.Other.Mototola_Spectra.yelp()
        elif other_model[7] == 1:
            return sirens.Other.Tomar_940.yelp()
        else:
            return dead
    if brand_name == HORNS:
        return dead


def set_phaser():  # Sets which sound will be used for the phaser
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
        if fed_sig_model[12] == 1:
            return sirens.Federal_Signal.Unitrol_80k.hetro()
        if fed_sig_model[13] == 1:
            return sirens.Federal_Signal.Unitrol_8001.phaser()
        if fed_sig_model[14] == 1:
            return sirens.Federal_Signal.Unitrol_Omega_90.hetro()
    if brand_name == GALLS:
        if galls_model[0] == 1:
            return sirens.Galls.ST160_Street_Thunder.thunder()
        if galls_model[1] == 1:
            return sirens.Galls.ST300_Command_Center.phaser()
    if brand_name == WHELEN:
        if whelen_model[0] == 1:
            return sirens.Whelen._295HF100.phaser()
        if whelen_model[1] == 1:
            return sirens.Whelen.Alpha.phaser()
        if whelen_model[2] == 1:
            return sirens.Whelen.Alpha_22m.wail2()
        if whelen_model[3] == 1:
            return sirens.Whelen.Beta.phaser()
        if whelen_model[4] == 1:
            return sirens.Whelen.Cencom_Gold.phaser()
        if whelen_model[5] == 1:
            return sirens.Whelen.Cencom_Sapphire.phaser()
        if whelen_model[6] == 1:
            return sirens.Whelen.Cencom_Sapphire_Howler.phaser()
        if whelen_model[7] == 1:
            return sirens.Whelen.Epsilon_EPSL_1.phaser()
        if whelen_model[8] == 1:
            return sirens.Whelen.Gamma_2.phaser()
    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            return sirens.Feniex.Storm_100w.phaser()
        elif feniex_model[1] == 1:
            return sirens.Feniex.Storm_Pro.phaser()
    if brand_name == OTHER:
        if other_model[1] == 1:
            return sirens.Other.Carson_SA441.phaser()
        elif other_model[2] == 1:
            return sirens.Other.NA_SI100M.riot()
        elif other_model[3] == 1:
            return sirens.Other.Powercall_DX5.phaser()
        elif other_model[4] == 1:
            return sirens.Other.Unitrol_480k.hilo()
        elif other_model[6] == 1:
            return sirens.Other.Mototola_Spectra.hilo()
        elif other_model[7] == 1:
            return sirens.Other.Tomar_940.phaser()
        else:
            return dead

    if brand_name == HORNS:
        return dead


def set_aux1():  # Sets what sound, if any, will be used as an auxillary sound. See below.

    # Returns a list: [Str, Bool]
    # The first element returned is the string to the auxillary sound,
    # The second being a bool, which will indicate if the selected
    # siren has an auxiliary siren.

    if brand_name == CODE_3:
        if code_3_model[2] == 1:
            return [sirens.Code_3.Mastercom_B.hilo(), True]
        else:
            return [dead, False]
    if brand_name == FED_SIG:
        if fed_sig_model[2] == 1:
            return [sirens.Federal_Signal.PA20.yelp2(), True]
        if fed_sig_model[4] == 1:
            return [sirens.Federal_Signal.PA300.hilo(), True]
        if fed_sig_model[8] == 1:
            return [sirens.Federal_Signal.SS2000SM.hilo(), False]
        if fed_sig_model[9] == 1:
            return [sirens.Federal_Signal.SSP3000b.hilo(), False]
        if fed_sig_model[11] == 1:
            return [sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.sweep2(), True]
        if fed_sig_model[13] == 1:
            return [sirens.Federal_Signal.Unitrol_8001.hilo(), True]
        if fed_sig_model[14] == 1:
            return [sirens.Federal_Signal.Unitrol_8001.hilo(), True]
        else:
            return [dead, False]
    if brand_name == GALLS:
        if galls_model[0] == 1:
            return [sirens.Galls.ST160_Street_Thunder.hilo(), True]
        if galls_model[1] == 1:
            return [sirens.Galls.ST300_Command_Center.hilo(), True]
        else:
            return [dead, False]
    if brand_name == WHELEN:
        if whelen_model[1] == 1:
            return [sirens.Whelen.Alpha.hilo(), True]
        elif whelen_model[2] == 1:
            return [sirens.Whelen.Alpha_22m.power_call_2(), True]
        elif whelen_model[4] == 1:
            return [sirens.Whelen.Cencom_Gold.hilo(), True]
        elif whelen_model[7] == 1:
            return [sirens.Whelen.Epsilon_EPSL_1.hilo(), True]
        elif whelen_model[8] == 1:
            return [sirens.Whelen.Gamma_2.riot(), True]
        else:
            return [dead, False]
    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            return [sirens.Feniex.Storm_100w.mech(), True]
        elif feniex_model[1] == 1:
            return [sirens.Feniex.Storm_Pro.hilo(), True]
        else:
            return [dead, False]
    if brand_name == OTHER:
        if other_model[1]:
            return [sirens.Other.Carson_SA441.hilo(), True]
        elif other_model[3] == 1:
            return [sirens.Other.Powercall_DX5.hilo(), True]
        elif other_model[7] == 1:
            return [sirens.Other.Tomar_940.alert(), True]
        else:
            return [dead, False]
    if brand_name == HORNS:
        return [dead, False]

def set_aux2():
    # Returns a list: [Str, Bool]
    # The first element returned is the string to the auxillary sound,
    # The second being a bool, which will indicate if the selected
    # siren has an auxiliary siren.

    if brand_name == CODE_3:
        if code_3_model[2] == 1:
            return [sirens.Code_3.Mastercom_B.hylo(), True]
        else:
            return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[2] == 1:
            return [sirens.Federal_Signal.PA20.yelp3(), True]
        if fed_sig_model[11] == 1:
            return [sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.sweep1(), True]
        if fed_sig_model[13] == 1:
            return [sirens.Federal_Signal.Unitrol_8001.sweep(), True]
        if fed_sig_model[14] == 1:
            return [sirens.Federal_Signal.Unitrol_8001.sweep(), True]
        else:
            return [dead, False]
    if brand_name == GALLS:
        return [dead, False]
    if brand_name == WHELEN:
        return [dead, False]
    if brand_name == FENIEX:
        if feniex_model[1] == 1:
            return [sirens.Feniex.Storm_Pro.mech(), True]
        else:
            return [dead, False]
    if brand_name == OTHER:
        if other_model[3] == 1:
            return [sirens.Other.Powercall_DX5.inter(), True]
        elif other_model[7] == 1:
            return [sirens.Other.Tomar_940.hetro(), True]
        else:
            return [dead, False]
    if brand_name == HORNS:
        return [dead, False]


def set_aux3():
    # Returns a list: [Str, Bool]
    # The first element returned is the string to the auxillary sound,
    # The second being a bool, which will indicate if the selected
    # siren has an auxiliary siren.

    if brand_name == CODE_3:
        return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[11] == 1:
            return [sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.hetro(), True]
        else:
            return [dead, False]
    if brand_name == GALLS:
        return [dead, False]
    if brand_name == WHELEN:
        return [dead, False]
    if brand_name == FENIEX:
        if feniex_model[1] == 1:
            return [sirens.Feniex.Storm_Pro.pcall(), True]
        else:
            return [dead, False]
    if brand_name == OTHER:
        if other_model[3] == 1:
            return [sirens.Other.Powercall_DX5.pcall(), True]
        elif other_model[7] == 1:
            return [sirens.Other.Tomar_940.hilo(), True]
        else:
            return [dead, False]
    if brand_name == HORNS:
        return [dead, False]

def set_aux4():
    # Returns a list: [Str, Bool]
    # The first element returned is the string to the auxillary sound,
    # The second being a bool, which will indicate if the selected
    # siren has an auxiliary siren.

    if brand_name == CODE_3:
        return [dead, False]
    elif brand_name == FED_SIG:
        if fed_sig_model[11] == 1:
            return [sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.Uhilo(), True]
        else:
            return [dead, False]
    if brand_name == GALLS:
        return [dead, False]
    if brand_name == WHELEN:
        return [dead, False]
    if brand_name == FENIEX:
        if feniex_model[1] == 1:
            return [sirens.Feniex.Storm_Pro.yelp2(), True]
        else:
            return [dead, False]
    if brand_name == OTHER:
        if other_model[3] == 1:
            return [sirens.Other.Powercall_DX5.pcall2(), True]
        elif other_model[7] == 1:
            return [sirens.Other.Tomar_940.yelp2(), True]
        else:
            return [dead, False]
    if brand_name == HORNS:
        return [dead, False]


brand_name = set_brand()


def set_lcd():
    # This function is called every time the brand, or model, is changed.
    # White space in the lcd_display_string() is so it will be centered on the lcd
    # The simple python equation of "(16 - len(str)) / 2" gives the correct amount of white
    # space so that the text can be centered.

    display.lcd_clear()
    set_brand()
    if brand_name == CODE_3:
        display.lcd_display_string('     Code 3', 1)
    elif brand_name == FED_SIG:
        display.lcd_display_string(' Federal Signal', 1)
    elif brand_name == GALLS:
        display.lcd_display_string('     Galls', 1)
    elif brand_name == WHELEN:
        display.lcd_display_string('     Whelen', 1)
    elif brand_name == FENIEX:
        display.lcd_display_string('     Feniex', 1)
    elif brand_name == OTHER:
        display.lcd_display_string('     Other', 1)
    elif brand_name == HORNS:
        display.lcd_display_string('     Horns', 1)

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
        if fed_sig_model[11] == 1:
            display.lcd_display_string("Touchmaster Delta", 2)
        if fed_sig_model[12] == 1:
            display.lcd_display_string("  Unitrol 80k", 2)
        if fed_sig_model[13] == 1:
            display.lcd_display_string("  Unitrol 8001", 2)
        if fed_sig_model[14] == 1:
            display.lcd_display_string("Unitrol Omega 90", 2)
    if brand_name == GALLS:
        if galls_model[0] == 1:
            display.lcd_display_string("ST160 Street Thunder", 2)
        if galls_model[1] == 1:
            display.lcd_display_string("ST300 Command Center", 2)
    if brand_name == WHELEN:
        if whelen_model[0] == 1:
            display.lcd_display_string('    295HF100', 2)
        if whelen_model[1] == 1:
            display.lcd_display_string('     Alpha', 2)
        if whelen_model[2] == 1:
            display.lcd_display_string('   Alpha 22m', 2)
        if whelen_model[3] == 1:
            display.lcd_display_string('      Beta', 2)
        if whelen_model[4] == 1:
            display.lcd_display_string('  Cencom Gold', 2)
        if whelen_model[5] == 1:
            display.lcd_display_string('Cencom Sapphire', 2)
        if whelen_model[6] == 1:
            display.lcd_display_string('Cencom Sapphire Howler', 2)
        if whelen_model[7] == 1:
            display.lcd_display_string(' Epsilon EPSL 1', 2)
        if whelen_model[8] == 1:
            display.lcd_display_string('    Gamma 2', 2)

    if brand_name == FENIEX:
        if feniex_model[0] == 1:
            display.lcd_display_string('   Storm 100w', 2)
        if feniex_model[1] == 1:
            display.lcd_display_string(' Storm Pro 200w', 2)


    if brand_name == OTHER:
        if other_model[0] == 1:
            display.lcd_display_string('AS350 Helicopter', 2)
        if other_model[1] == 1:
            display.lcd_display_string('  Carson SA441', 2)
        if other_model[2] == 1:
            display.lcd_display_string('   N.A. SI100', 2)
        if other_model[3] == 1:
            display.lcd_display_string(' Powercall DX5', 2)
        if other_model[4] == 1:
            display.lcd_display_string('  Unitrol 480k', 2)
        if other_model[5] == 1:
            display.lcd_display_string(' CHP Motorcycle', 2)
        if other_model[6] == 1:
            display.lcd_display_string('Mototola Spectra', 2)
        if other_model[7] == 1:
            display.lcd_display_string('   Tomar 940', 2)

    if brand_name == HORNS:
        if horns_model[0] == 1:
            display.lcd_display_string('   Dixie Horn', 2)
        if horns_model[1] == 1:
             display.lcd_display_string(' Liberty City', 2)
        if horns_model[2] == 1:
             display.lcd_display_string('Ice Cream Truck', 2)
        if horns_model[3] == 1:
             display.lcd_display_string('    Bad Boys', 2)
        if horns_model[4] == 1:
             display.lcd_display_string('     Ecto1', 2)
        if horns_model[5] == 1:
             display.lcd_display_string('    Move Out', 2)
        if horns_model[6] == 1:
             display.lcd_display_string('   Pull Over', 2)
        if horns_model[7] == 1:
             display.lcd_display_string('    Rap Horn', 2)
        if horns_model[8] == 1:
             display.lcd_display_string('  Sad Trombone', 2)
        if horns_model[9] == 1:
             display.lcd_display_string('  Train Horn', 2)
        if horns_model[10] == 1:
             display.lcd_display_string('      Horn', 2)



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
    
# Siren playing Booleans
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
        if auxiliary and aux3_is_usable:
            aux3.play(-1)
        else:
            if wail_playing:
                wail.stop()
            yelp.play(-1)
            wail.set_volume(0)
            yelp_playing = True
    else:
        if auxiliary and aux3_is_usable:
            aux3.stop()
        if wail_playing:
            wail.play(-1)
        yelp.stop()
        wail.set_volume(1)
        yelp_playing = False


def play_manual_wail(channel):
    global manual_wail_playing, wail_playing
    if GPIO.input(pin.manual_wail):
        if auxiliary and aux4_is_usable:
            aux4.play(-1)

        # if not manual_wail_playing and not wail_playing and not aux4_is_usable and not auxiliary:
        else:
            m_wail.play(-1)
            manual_wail_playing = True
    else:
        if auxiliary and aux4_is_usable:
            aux4.stop()
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
        elif brand_name == GALLS:
            galls_model.rotate(1)
        elif brand_name == WHELEN:
            whelen_model.rotate(1)
        elif brand_name == FENIEX:
            feniex_model.rotate(11)            
        elif brand_name == OTHER:
            other_model.rotate(1)
        elif brand_name == HORNS:
            horns_model.rotate(1)
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
        elif brand_name == GALLS:
            galls_model.rotate(-1)
        elif brand_name == WHELEN:
            whelen_model.rotate(-1)
        elif brand_name == FENIEX:
            feniex_model.rotate(-1)
        elif brand_name == OTHER:
            other_model.rotate(-1)
        elif brand_name == HORNS:
            horns_model.rotate(-1)


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

