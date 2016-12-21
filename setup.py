# piren.py
#
# by Ian Thompson on 12/2/16
# Part of the Piren Project
#
# (c) 2016 Ian Thompson

from collections import deque
import sirens
from time import sleep

# case = deque([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

case = deque([1, 0, 0])

def set_wail():
    if case[0] == 1:
        return sirens.Federal_Signal.SSP3000b_w_Rumbler.wail()
    if case[1] == 1:
        return sirens.Federal_Signal.SSP3000b.wail()
    if case[2] == 1:
        return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.wail()

def set_horn():
    if case[0] == 1:
        return sirens.Federal_Signal.SSP3000b_w_Rumbler.horn()
    if case[1] == 1:
        return sirens.Federal_Signal.SSP3000b.horn()
    if case[2] == 1:
        return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.horn()

def set_yelp():
    if case[0] == 1:
        return sirens.Federal_Signal.SSP3000b_w_Rumbler.yelp()
    if case[1] == 1:
        return sirens.Federal_Signal.SSP3000b.yelp()
    if case[2] == 1:
        return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.yelp()


def set_phaser():
    if case[0] == 1:
        return sirens.Federal_Signal.SSP3000b_w_Rumbler.phaser()
    if case[1] == 1:
        return sirens.Federal_Signal.SSP3000b.phaser()
    if case[2] == 1:
        return sirens.Federal_Signal.Touchmaster_Touchmaster_Delta.phaser()


wail = set_wail()
horn = set_horn()
yelp = set_yelp()
phaser = set_phaser()


