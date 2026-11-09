#!/usr/bin/env python3

import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

def canCancelInput(prompt:str=":",history=list(),complete=None)->str|None:
    prefix = ""
    suffix = ""
    print(end=prompt,flush=True)
    while True:
        c = sys.stdin.read(16)
        if(len(c) == 0):continue
        elif(c == "\n"):break
        elif(c == "\x1b"):
            return None
        elif(c == "\x1b[D" or c == "\x02"):#] # Left Arrow
            if(len(prefix) > 0):
                suffix = prefix[-1] + suffix
                prefix = prefix[:-1]
                print(end="\b",flush=True)
        elif(c == "\x1b[C" or c == "\x06"):#] # Right Arrow
            if(len(suffix) > 0):
                ch = suffix[0]
                prefix += ch
                suffix = suffix[1:]
                print(end=ch,flush=True)
        elif(c == "\x05"): # endofline
            ss = suffix
            prefix = prefix + suffix
            suffix = ""
            print(end=ss,flush=True)
        elif(c == "\x01"): # beginning
            ps = prefix
            suffix = prefix + suffix
            prefix = ""
            print(end="\b" * len(ps),flush=True)
        elif(c == "\x7f"):
            if(len(prefix) > 0):
                prefix = prefix[:-1]
                print(end=f"\b{suffix} \b" + "\b" * len(suffix),flush=True)
        elif(c == "\t" and complete is not None):
            prefix = complete(prefix,suffix)
        elif(c.startswith("\x1b")):pass
        elif(ord(c[0]) >= 0x20):
            print(end=f"{c}{suffix}" + "\b" * len(suffix),flush=True)
            prefix += c
    return prefix + suffix

def gotoPlace(x,y):
    print(end=f"\x1b[{y};{x}H")#]



try:
    while 1:
        try:
            c = sys.stdin.read(1)
            if(len(c) == 1 and c in ":+-/"):
                gotoPlace(1,1)
                print(end="\x1b[2K")#]
                print(canCancelInput(c))
            elif c:
                print("Got character", repr(c))
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

