import random
from colorama import Fore
import emoji
import numpy as np
import keyboard
import tqdm
import time
import math
import os
import subprocess
from getmac import get_mac_address as gma
import webbrowser
import art
import fileinput
import pyautogui
import re
import matplotlib as plt
import turtle as tur
import csv
import logging as logg
from string import ascii_letters
from PIL import Image

class sea:
    def imagine_color(self=None):
        img = Image.new(mode="RGB", size=(300, 600), color=(random.randint(0, 999) - 100, random.randint(0, 999) - 200, random.randint(0, 999) - 300, random.randint(0, 999) - 400))
        img.show()

    def ascii_imagine(self=None):
        asc = art.randart()
        for i in range(15):
            print(asc)

    def pick_random(self=None, lis=list):
        pick = random.choice(lis)

    def opertion(self=None, a=None):
        op = a + random.randint(0, a)
        print(op)

class land:
    def loop(self=None, loopfunc=None, rangeint=None):
        for i in range(rangeint):
            a = loopfunc