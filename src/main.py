#!/bin/python3

import os
import sys
import random
import time
import answers
from shortcuts import sudo


def storedata(x):
    with open(cbt, "a") as bleh:
        bleh.write(x)


cbt = os.path.expanduser("~/.pleaserc")

command = " ".join(sys.argv[1:])
if not os.path.isfile(cbt):
    f = open(cbt, "x")

f = open(cbt, "r")
nah = f.read()

if len(command) == 0:
    print("hmph >:3 run an actual command.")
    exit()

answers.handleresponse(nah[0], nah, cbt, command)

mood = random.randint(1, 4)
match mood:
    case 1:
        print("hmph! >:3 fine. ill do it")
        os.system(sudo(command))
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
