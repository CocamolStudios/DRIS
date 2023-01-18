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
import diatcode
import tinypod

class keywords1:
    a = keyboard.is_pressed("~")
    Plf = bin(a)
    sd = None
    mav = None
    rss = None
    feno = str(random.randint(1, 4000) * 12 - 9 + random.randint(0,99999999999) - 9999999 - 999999 - 99999 - 9999 * 456 + random.randint(0, 56) // 2 - 100)
    asd = None

class commands:
    cd = None
    bod = None
    vaf = None
    mac = None
    netc = None
    wef = None
    WaD = None
    ico = None
    loc = None
    cass = None
    dof = None
    dir = None

class cursor:
    """This class is made to sort and keep the code clean and has only one function"""

    def inputs(self):
        """The input function forms the entire interactive system of the IDE. Part of it is mostly input < / >, which is where almost half of the IDE code is written. I call it "100 mile road"."""
        print(keywords1.feno, Fore.RED + "DON'T SHARE THIS WITH ANYONE ", Fore.GREEN + "- FENO")
        print(Fore.RESET + "")
        while True:
            a = input(Fore.GREEN + "~")
            if a == "plf":
                print(Fore.BLUE + "plf" + Fore.RED + "*")
                time.sleep(0.03)
                print(Fore.RESET + keywords1.Plf)

            elif a == "sd.":
                b = keywords1.sd = open(str(input("path:")), input("mode:"))
                print(Fore.RESET + b)

            elif a == "mav":
                keywords1.mav = bin(open(input("path:")), input("mode:"))
                print(Fore.RESET + keywords1.mav)

            elif a == "rss":
                rss = keywords1.rss
                rss = hex(int((input("Any:"))))
                print(Fore.RESET + rss)

            elif a == "op":
                print(Fore.WHITE + "op." + Fore.BLUE + bin(int(input("address:"))) + Fore.RESET + "")

            elif a == "asd":
                asd = keywords1.asd
                l = []
                a2 = int(input("int:"))
                for i in range(a2):
                    b = int(input("int:"))
                    l.append(b)
                print(Fore.WHITE + "asd.", max(l), Fore.RESET + "")

            elif a == "q:":
                break

            elif a == "/":
                while True:
                    b = input(Fore.WHITE + "/")
                    if b == "cd":
                        cd = commands.cd
                        cd = os.scandir(str(input("system's path:")))
                        print(cd)

                    elif b == "bod":
                        bod = commands.bod
                        bod = subprocess.Popen(str(input("path:")))

                    elif b == "mac":
                        mac = commands.mac
                        mac = gma()
                        print(mac)

                    elif b == "q>":
                        print(Fore.BLUE + "~~~~~~~~~``~~~~~~~~~")
                        break

                    elif b == "netc":
                        netc = commands.netc
                        netc = subprocess.call(str(input(Fore.RED + "$")))
                        print(Fore.RESET + "")

                    elif b == "wef":
                        wef = commands.wef
                        wef = webbrowser.open(str(input("url:")))

                    elif b == "WaD":
                        wad = commands.WaD
                        wad = hash(input(Fore.BLUE + "=>"))
                        print(wad)
                        print(
                            Fore.RED + "DO NOT SHARE THIS IF OBJECT IS HAVE A SECURITY REFERENCE - " + Fore.YELLOW + "HASH SECURITY ADVICE")

                    elif b == "ico":
                        ico = commands.ico
                        ico = subprocess.Popen(str(input("program path:")))

                    elif b == "loc":
                        print(Fore.RED + "^" + Fore.BLUE + "#" + Fore.YELLOW + "$")
                        loc = commands.loc
                        print(Fore.GREEN + "")
                        art.tprint("LOC")
                        time.sleep(0.0002)
                        print(Fore.RED + "loc is a simple ide for DRIS, The loc module can act like an IDE.")
                        b2 = input(Fore.MAGENTA + ";")
                        if b2 == "texted:":

                            while True:
                                no_of_lines = int(input(Fore.WHITE + "No of lines:"))
                                lines = ""
                                name_of_file = input("What is your desired filename for the file?")
                                for i in range(no_of_lines):
                                    c = input(Fore.BLUE + ">")
                                    lines += c + "\n"

                                f = open(name_of_file, 'w')
                                f.write(lines)
                                f.close()

                        elif b2 == "q>>":
                            break

                        elif b2 == "run:":
                            d = open(input("filename:"), 'r')

                        elif b2 == "del:":
                            os.remove(input("path:"))

                    elif b == "cass":
                        myScreenshot = pyautogui.screenshot()
                        myScreenshot.save(input("path:"))

                    elif b == "dof":
                        dof = commands.dof
                        dof = len(input(Fore.MAGENTA + "text:"))
                        dof1 = dof * dof ** 2
                        dof2 = dof1 / dof
                        print(Fore.BLUE + dof2)
                        print(Fore.RESET + "")

                    elif b == "dir":
                        print('in Dev...')

                    elif b == "regexp":
                        art.tprint(Fore.GREEN + "RegExp")
                        print(
                            Fore.RED + "Writing and testing regular expressions with RegExp implemented with the re module.")
                        c2 = str(input(Fore.BLUE + "text:"))
                        c3 = re.compile(str(input("RegExp:")))
                        print("Calling mode:")
                        print("match")
                        print("search")
                        print("findall")
                        print("finditer")
                        c4 = input("Calling mode:")
                        if c4 == 'match':
                            result = c3.match(a)
                            print(result)

                        elif c4 == 'search':
                            result = c3.search(a)
                            print(result)

                        elif c4 == 'findall':
                            result = c3.findall(a)
                            print(result)

                        elif c4 == 'finditer':
                            result = c3.finditer(a)
                            print(result)

                    elif b == "graphic":
                        print("in Dev...")

                    elif b == "csvd":
                        art.tprint(Fore.BLUE + "CSVD")
                        print(
                            Fore.RED + "csvd is an internal library for DRIS that allows you to work more easily and quickly with the csv module in Python")
                        print(Fore.RESET + "")
                        b3 = str(input("filename:"))
                        b4 = str(input("mode:"))
                        if b4 == 'r':
                            with open(b3, b4) as csvfile:
                                data = csv.reader(csvfile)
                                for line in data:
                                    print(line)

                        elif b4 == 'w':
                            with open(b3, b4) as csvfile:
                                data = csv.writer(csvfile, list(input("")))

                                for line in data:
                                    print(line)

                    elif b == "caesar":
                        print(Fore.GREEN + "")
                        art.tprint("Caesar")
                        print(
                            Fore.RED + "Caesar is a built-in DRIS library, a cryptographic method belonging to Julius Caesar, which was useful in its time, but is not of much use now.")
                        print(Fore.BLUE + "")
                        string = str(input("string:"))
                        key = int(input("tab count:"))

                        # encrypt
                        alpha = ascii_letters
                        result = ''
                        for ch in string:
                            if ch not in alpha:
                                result += ch
                            else:
                                new_key = (alpha.index(ch) + key) % len(alpha)
                                result += alpha[new_key]

                        print(Fore.RESET + result)

                        string = str(input("string:"))
                        key = int(input("tab count:"))
                        # decrypt
                        key *= -1
                        alpha = ascii_letters
                        result = ''
                        for ch in string:
                            if ch not in alpha:
                                result += ch
                            else:
                                new_key = (alpha.index(ch) + key) % len(alpha)
                                result += alpha[new_key]

                        print(Fore.RESET + result)

                    elif b == "diatcode":
                        b5 = input("select:")
                        if b5 == "var":
                            t = int(input("var1:"))
                            t2 = int(input("var2:"))
                            t3 = str(input("op:"))
                            t4 = []
                            diatcode.var(var1=t, var2=t2, op=t3, var3=t4)
                            print(t4)

                        elif b5 == "passing":
                            t = input(Fore.RED + "input:")
                            t2 = input("input2:")
                            diatcode.passing(inp=t, inprow=t2)
                            print(Fore.RESET + "")

                        elif b5 == "match":
                            t = input("a:")
                            t2 = input("b:")
                            diatcode.match(a=t, b=t2)

                        elif b5 == "alt_o":
                            t = str(input())

                        elif b5 == "func":
                            t = input("select:")
                            if t == "m":
                                t = int(input("r:"))
                                diatcode.functions.m_sequence(r=t)

                            elif t == "push":
                                t = int(input("number:"))
                                t2 = int(input("number2:"))
                                diatcode.functions.push(n=t, k=t2)

                            elif t == "g":
                                t = int(input("num:"))
                                t2 = int(input("base:"))
                                t3 = int(input("q:"))
                                diatcode.functions.g_logarithm(num=t, base=t2, q=t3)

                            elif t == "alpha":
                                print("in Dev...")
                                # TODO : writing the code

                            elif t == "m_f":
                                t = int(input("x:"))
                                t2 = int(input("y:"))
                                diatcode.functions.m_function(x=t, y=t2)

                            elif t == "l":
                                t = int(input("n:"))
                                diatcode.functions.l(n=t)

                            elif t == "r":
                                t = int(input("n:"))
                                t2 = int(input("li:"))
                                t3 = [random.randint(0, t2), random.randint(0, t), random.randint(0, t * t2),
                                      random.randint(0, t * t2 + t), random.randint(0, t ^ t + t2 * t),
                                      random.randint(0, 72736486236473276426364887408745784564257626596946976056480608516084605868460814806584385629452986459640238020480085620605000000000000000000000000000000000000000000000737289349283982639864836943975962986389483642382973697236529846589698680362610),
                                      random.randint(0, 634623694236427367423967652763974697362965765629467962379642976492222222222222222222222222263747649724795792459724659240000000000000000000000000000000035863586385863858638586300000000038357838559284697364726913640163641394917367367926954603865683757846564976592342611), ]
                                diatcode.functions.r(li=t2, n=t, lis=t3)

                            elif t == "up":
                                t = int(input("u:"))
                                t2 = int(input("p:"))
                                diatcode.functions.u_p(u=t, p=t2)

                        elif b5 == "listrow":
                            t = list(input("list:"))
                            t2 = int(input("gen:"))
                            t3 = int(input("genrow:"))
                            diatcode.listrow(lis=t, gen=t2, genrow=t3)

                        elif b5 == "searchi":
                            t = list(input("array:"))
                            t2 = int(input("val:"))
                            diatcode.searchi(array=t, val=t2)

                        elif b5 == "isomorphic":
                            t = input("text1:")
                            t2 = input("text2:")
                            diatcode.isomorphic(s=t, t=t2)

                        elif b5 == "Cipher":
                            t = input("choose:")
                            if t == "a1z26":
                                t = input("plaintext:")
                                diatcode.a1z26.encode(self=None, plain=t)
                                t2 = input("encode text:")
                                diatcode.a1z26.decode(self=None, encode=t2)

                            elif t == "Onetime":
                                t = input("text:")
                                diatcode.OneTime.encrypt(self=None, text=t)
                                t2 = int(input("key:"))
                                t3 = input("cipher:")
                                diatcode.OneTime.decrypt(self=None, cipher=t3, key=t2)

                        elif b5 == "binarys":
                            t = list(input("array:"))
                            t2 = int(input("query:"))
                            diatcode.binary_search(array=t, query=t2)

                    elif b == "tinypod":
                        pod = input("method:")
                        if pod == "imagine.color":
                            tinypod.sea.imagine_color()

                        elif pod == "ascii.imagine":
                            tinypod.sea.ascii_imagine()

                        elif pod == "pick.random":
                            liss = list(input("list:"))
                            tinypod.sea.pick_random(lis=liss)

                        elif pod == "opertion":
                            num = int(input("num:"))
                            tinypod.sea.opertion(a=num)

                        elif pod == "loop":
                            A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = None
                            func = eval(input("func:"))
                            rangeint = int(input("range:"))
                            tinypod.land.loop(loopfunc=func, rangeint=rangeint)

            elif a == "feno":
                while True:
                    art.tprint(Fore.BLUE + "Feno")
                    print(Fore.RED + "")
                    n = input("password-onetime:")
                    if not n == keywords1.feno:
                        print(Fore.RED + "ALART!")
                        Seconds = 4.5
                        os.system(f" shoutdown /s /t {Seconds} ")

                    else:
                        c = input(Fore.YELLOW + "@")
                        if c == "profile":
                            print("in Dev...")
                            break

            elif a == "#":
                while True:
                    c = input(Fore.BLUE + "#")