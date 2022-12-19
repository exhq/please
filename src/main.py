#!/bin/python3

import os
import sys
import random
import time


def storedata(x):
    with open(os.path.expanduser('~')+"/.pleaserc", "a") as bleh:
        bleh.write(x)


command = " ".join(sys.argv[1:])
if not os.path.isfile(os.path.expanduser('~')+"/.pleaserc"):
    f = open(os.path.expanduser('~')+"/.pleaserc", "x")

f = open(os.path.expanduser('~')+"/.pleaserc", "r")
nah = f.read()
if len(nah) > 1 and nah[0] == "2":
    print("fineeeeee you're nice enough ill do it for you :3")
    os.remove(os.path.expanduser('~')+"/.pleaserc")
    os.system("sudo " + nah.replace("2\n", ""))
    exit()

if len(nah) > 1 and nah[0] == "4":
    lmao = nah.split("\n")
    t = int(time.time())

    if t - int(lmao[1]) < 11:
        print("bro it hasnt been 10 seconds yet")
        exit()
    else:
        print("here get yo command and go away")
        os.system("sudo " + command)
        os.remove(os.path.expanduser('~')+"/.pleaserc")
        exit()

mood = random.randint(4, 4)
match mood:
    case 1:
        print("hmph! >:3 fine. ill do it")
        os.system("sudo " + command)
    case 2:
        print("(￣^￣) 凸 say please again")
        storedata("2\n" + command)
    case 3:
        print("less add sum color in ther >:D")
        os.system("sudo " + command + " | lolcat")
    case 4:
        print("ion feel like it, wait like 10 seconds")
        t = int(time.time())
        storedata("4\n" + str(t) + "\n" + command)
