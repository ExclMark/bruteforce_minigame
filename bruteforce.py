import os
from sys import argv
import random
import datetime
from time import sleep
import schedule
import keyboard

os.system("")

try:
    speed = 0.5 if len(argv) == 0 else float(argv[1])
    if speed < 0:
        speed = 0.5
except:
    speed = 0.5


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'


try:
    if os.geteuid() != 0:
        print(
            Colors.RED + "You need to run this program as root or with sudo!" + Colors.END)
        sleep(5)
        exit()
except:
    pass

brute_logo = """\033[92m
             ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____
            | __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|
            |  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|
            | |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___
            |____/|_| \_ \\___/  |_| |_____|_|   \___/|_| \_ \\____|_____|
                    - BUSTING TRHOUGH THE BACKDOOR SINCE 1998 -
                                - Made by: ExclMark -

                                      {TIME}\033[0m
                           {1l} {a1} {2l} {b1} {3l} {c1} {4l} {d1} {5l} {e1} {6l} {f1} {7l} {g1} {8l} {h1} {9l}
                           {1l} {a2} {2l} {b2} {3l} {c2} {4l} {d2} {5l} {e2} {6l} {f2} {7l} {g2} {8l} {h2} {9l}
                           \033[94m―――――――――――――――――――――――――――――――\033[0m
                           {1l} {a3} {2l} {b3} {3l} {c3} {4l} {d3} {5l} {e3} {6l} {f3} {7l} {g3} {8l} {h3} {9l}
                           \033[94m―――――――――――――――――――――――――――――――\033[0m
                           {1l} {a4} {2l} {b4} {3l} {c4} {4l} {d4} {5l} {e4} {6l} {f4} {7l} {g4} {8l} {h4} {9l}
                           {1l} {a5} {2l} {b5} {3l} {c5} {4l} {d5} {5l} {e5} {6l} {f5} {7l} {g5} {8l} {h5} {9l}
"""

win = """\033[92m
             ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____
            | __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|
            |  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|
            | |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___
            |____/|_| \_ \\___/  |_| |_____|_|   \___/|_| \_ \\____|_____|
                    - BUSTING TRHOUGH THE BACKDOOR SINCE 1998 -
                                - Made by: ExclMark -

                                    {TIME}
                        Successfully acquired the password.
                            Press any key to continue.\033[0m
"""

closed = """\033[92m
             ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____
            | __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|
            |  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|
            | |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___
            |____/|_| \_ \\___/  |_| |_____|_|   \___/|_| \_ \\____|_____|
                    - BUSTING TRHOUGH THE BACKDOOR SINCE 1998 -
                                - Made by: ExclMark -

                                      {TIME}
                                 Bruteforce cancelled.
                              Press any key to continue.\033[0m
"""

time_is_up = """\033[92m
             ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____
            | __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|
            |  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|
            | |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___
            |____/|_| \_ \\___/  |_| |_____|_|   \___/|_| \_ \\____|_____|
                    - BUSTING TRHOUGH THE BACKDOOR SINCE 1998 -
                                - Made by: ExclMark -

                                      {TIME}
                                      Time is up.
                                Press enter to retry.\033[0m
"""


def generate_random_letter():
    return chr(random.randint(97, 122))


def clear_display():
    return os.system(
        'cls' if os.name in ('nt', 'dos') else 'clear')


time_left = datetime.datetime.now() + datetime.timedelta(seconds=60)


def wait_for_key():
    while True:
        if keyboard.is_pressed("enter") or keyboard.is_pressed("space"):
            return True


def time():
    global time_left
    now = datetime.datetime.now()
    time = time_left - now
    if time < datetime.timedelta(seconds=0):
        clear_display()
        print(time_is_up.replace("{TIME}", "00:00.000"))
        wait_for_key()
        time_left = datetime.datetime.now() + datetime.timedelta(seconds=60)
    time = str(time).split(":")[1] + ":" + str(time).split(":")[2]
    time = time.split(".")[0] + "." + str(int(time.split(".")[1]) // 1000)
    return time


wordlist = ['CREAMPIE', 'DEADLOCK', 'MORPHEUS', 'SENTINEL', 'WORMSIGN',
            'PASSWORD', 'PETSNAME', 'DYNAMITE', 'BACKDOOR', 'UNLOCKED',
            'BLUEBOOK', 'DECIPHER', 'JUNKYARD', 'YETARIAN'
            ]

word = random.choice(wordlist)

canvas = []
for _ in range(8):
    canvas.append([generate_random_letter() for _ in range(0, 10)])

for x in range(8):
    canvas[x][random.randint(0, 8)] = f"+{word[x]};"


alist = []
blist = []
clist = []
dlist = []
elist = []
flist = []
glist = []
hlist = []
acorr = False
bcorr = False
ccorr = False
dcorr = False
ecorr = False
fcorr = False
gcorr = False
hcorr = False
stage = 0
active_zone = 1


def roll():
    global alist, blist, clist, dlist, elist, flist, glist, hlist, acorr, bcorr, ccorr, dcorr, ecorr, fcorr, gcorr, hcorr, stage
    i = stage
    if not acorr:
        alist = []
        l = canvas[0]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            alist.append(res.split(" ")[x])
    if not bcorr:
        blist = []
        l = canvas[1]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            blist.append(res.split(" ")[x])
    if not ccorr:
        clist = []
        l = canvas[2]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            clist.append(res.split(" ")[x])
    if not dcorr:
        dlist = []
        l = canvas[3]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            dlist.append(res.split(" ")[x])
    if not ecorr:
        elist = []
        l = canvas[4]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            elist.append(res.split(" ")[x])
    if not fcorr:
        flist = []
        l = canvas[5]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            flist.append(res.split(" ")[x])
    if not gcorr:
        glist = []
        l = canvas[6]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            glist.append(res.split(" ")[x])
    if not hcorr:
        hlist = []
        l = canvas[7]
        _len = len(l)
        res = f"{l[i % _len]} {l[(i+1) % _len]} {l[(i+2) % _len]} {l[(i+3) % _len]} {l[(i+4) % _len]}".upper()
        for x in range(0, 5):
            hlist.append(res.split(" ")[x])
    stage -= 1


def display():
    global acorr, bcorr, ccorr, dcorr, ecorr, fcorr, gcorr, hcorr, active_zone
    # Display the logo
    clear_display()
    text = brute_logo.replace("{TIME}", str(time()))

    text = text.replace("{a1}", alist[0])
    text = text.replace("{a2}", alist[1])
    text = text.replace("{a3}", alist[2])
    text = text.replace("{a4}", alist[3])
    text = text.replace("{a5}", alist[4])

    text = text.replace("{b1}", blist[0])
    text = text.replace("{b2}", blist[1])
    text = text.replace("{b3}", blist[2])
    text = text.replace("{b4}", blist[3])
    text = text.replace("{b5}", blist[4])

    text = text.replace("{c1}", clist[0])
    text = text.replace("{c2}", clist[1])
    text = text.replace("{c3}", clist[2])
    text = text.replace("{c4}", clist[3])
    text = text.replace("{c5}", clist[4])

    text = text.replace("{d1}", dlist[0])
    text = text.replace("{d2}", dlist[1])
    text = text.replace("{d3}", dlist[2])
    text = text.replace("{d4}", dlist[3])
    text = text.replace("{d5}", dlist[4])

    text = text.replace("{e1}", elist[0])
    text = text.replace("{e2}", elist[1])
    text = text.replace("{e3}", elist[2])
    text = text.replace("{e4}", elist[3])
    text = text.replace("{e5}", elist[4])

    text = text.replace("{f1}", flist[0])
    text = text.replace("{f2}", flist[1])
    text = text.replace("{f3}", flist[2])
    text = text.replace("{f4}", flist[3])
    text = text.replace("{f5}", flist[4])

    text = text.replace("{g1}", glist[0])
    text = text.replace("{g2}", glist[1])
    text = text.replace("{g3}", glist[2])
    text = text.replace("{g4}", glist[3])
    text = text.replace("{g5}", glist[4])

    text = text.replace("{h1}", hlist[0])
    text = text.replace("{h2}", hlist[1])
    text = text.replace("{h3}", hlist[2])
    text = text.replace("{h4}", hlist[3])
    text = text.replace("{h5}", hlist[4])

    if active_zone == 1:
        text = text.replace(
            "{1l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{2l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 2:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{3l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 3:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{4l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 4:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{5l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 5:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{6l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 6:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{7l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{8l}", f" ")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 7:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{8l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{9l}", f" ")
    elif active_zone == 8:
        text = text.replace(
            "{1l}", f" ")
        text = text.replace(
            "{2l}", f" ")
        text = text.replace(
            "{3l}", f" ")
        text = text.replace(
            "{4l}", f" ")
        text = text.replace(
            "{5l}", f" ")
        text = text.replace(
            "{6l}", f" ")
        text = text.replace(
            "{7l}", f" ")
        text = text.replace(
            "{8l}", f"{Colors.GREEN}|{Colors.END}")
        text = text.replace(
            "{9l}", f"{Colors.GREEN}|{Colors.END}")

    if keyboard.is_pressed('space') or keyboard.is_pressed('enter'):
        if active_zone == 1:
            if alist[2].startswith("+"):
                alist[2] = alist[2].replace("+", "!")
                acorr = True
                active_zone = 2
            else:
                acorr = False
                active_zone = 1
        elif active_zone == 2:
            if blist[2].startswith("+"):
                blist[2] = blist[2].replace("+", "!")
                bcorr = True
                active_zone = 3
            else:
                acorr, bcorr = False, False
                active_zone = 1
        elif active_zone == 3:
            if clist[2].startswith("+"):
                clist[2] = clist[2].replace("+", "!")
                ccorr = True
                active_zone = 4
            else:
                acorr, bcorr, ccorr = False, False, False
                active_zone = 1
        elif active_zone == 4:
            if dlist[2].startswith("+"):
                dlist[2] = dlist[2].replace("+", "!")
                dcorr = True
                active_zone = 5
            else:
                acorr, bcorr, ccorr, dcorr = False, False, False, False
                active_zone = 1
        elif active_zone == 5:
            if elist[2].startswith("+"):
                elist[2] = elist[2].replace("+", "!")
                ecorr = True
                active_zone = 6
            else:
                acorr, bcorr, ccorr, dcorr, ecorr = False, False, False, False, False
                active_zone = 1
        elif active_zone == 6:
            if flist[2].startswith("+"):
                flist[2] = flist[2].replace("+", "!")
                fcorr = True
                active_zone = 7
            else:
                acorr, bcorr, ccorr, dcorr, ecorr, fcorr = False, False, False, False, False, False
                active_zone = 1
        elif active_zone == 7:
            if glist[2].startswith("+"):
                glist[2] = glist[2].replace("+", "!")
                gcorr = True
                active_zone = 8
            else:
                acorr, bcorr, ccorr, dcorr, ecorr, fcorr, gcorr = False, False, False, False, False, False, False
                active_zone = 1
        elif active_zone == 8:
            if hlist[2].startswith("+"):
                hlist[2] = hlist[2].replace("+", "!")
                hcorr = True
            else:
                acorr, bcorr, ccorr, dcorr, ecorr, fcorr, gcorr, hcorr = False, False, False, False, False, False, False, False
                active_zone = 1

    text = text.replace("+", f"{Colors.RED}")
    text = text.replace("!", f"{Colors.GREEN}")
    text = text.replace(";", f"{Colors.END}")
    print(text)
    sleep(0.1)


def main():
    global hcorr
    # Main function
    schedule.every(speed).seconds.do(roll)
    while True:
        try:
            if not hcorr:
                display()
                schedule.run_pending()
                if time == "00:00":
                    break
            else:
                clear_display()
                print(win.replace("{TIME}", str(time())))
                wait_for_key()
                exit()
        except KeyboardInterrupt:
            clear_display()
            print(closed.replace("{TIME}", str(time())))
            wait_for_key()
            exit()


if __name__ == '__main__':
    roll()
    main()
