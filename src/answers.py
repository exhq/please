import os
import time
from shortcuts import sudo


def handleresponse(x, nah, cbt, command):
    if x == "2":
        print("fineeeeee you're nice enough ill do it for you :3")
        os.remove(cbt)
        os.system(sudo(nah.replace("2\n", "")))
        exit()
    if x == "4":
        lmao = nah.split("\n")
        t = int(time.time())

        if t - int(lmao[1]) < 11:
            print("bro it hasnt been 10 seconds yet")
        else:
            print("here get yo command and go away")
            os.system(sudo(command))
            os.remove(cbt)
        exit()
