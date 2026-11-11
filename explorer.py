#!/usr/bin/env python3

import struct
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

def canCancelInput(prompt:str=":",history=list(),complete=None)->str|None:
    print(end="\x1b[K")#]
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
            print(end="\b"*len(prefix))
            (prefix,suffix) = complete(prefix,suffix)
            print(end=prefix+suffix+"\b"*len(suffix),flush=True)
        elif(c.startswith("\x1b")):pass
        elif(ord(c[0]) >= 0x20):
            print(end=f"{c}{suffix}  \b\b" + "\b" * len(suffix),flush=True)
            prefix += c
    return prefix + suffix

def gotoPlace(x,y):
    print(end=f"\x1b[{y};{x}H")#]
def clear():
    gotoPlace(1,1)
    print(end=f"\x1b[0J",flush=True)#]

def makeAsLength(data,length):
    data = data[:length]
    while(len(data) < length):
        data = " " + data
    return data

def fuzzyFindScore(target:str,pattern:str)->int:
    if(len(pattern) < 1):return 0
    ti = pi = 0
    matches = list()
    while(ti < len(target) and pi < len(pattern)):
        if(target[ti] == pattern[pi]):
            matches.append(ti)
            pi += 1
        elif(pattern[pi] == "*"):
            break
        ti += 1
    if(pi < len(pattern) and pattern[pi] != "*"):return 0
    if(len(matches) == 0):return 0
    score = 1000
    score -= matches[0] * 5
    for idx in range(1,len(matches)):
        gap = matches[idx] - matches[idx - 1] - 1
        score -= gap * 8
    score -= max(0,len(target) - len(pattern)) * 0.5
    return score

def bin2ColorHex(bin,length:int=128):
    if(len(bin) < 2):
        outp = bin
        while(len(outp) < length):
            outp = " " + outp
        return outp
    lookup = "0123456789ABCDEF"
    outp = ""
    counter = 0
    myLength = 0
    value = 0
    isRed = "\x1b[0m"#]
    while len(bin) > 0 and length > myLength:
        ch = bin[-1]
        bin = bin[:-1]
        #
        value += (ch == "1") << (counter % 4)
        if(ch not in "01"):isRed = "\x1b[31m"#]
        counter += 1
        #
        if(counter == 4):
            myLength += 1
            outp = isRed + lookup[value] + outp
            counter = value = 0
    if(counter > 0):
        outp = lookup[value] + outp
        myLength += 1
    while(myLength < length):
        outp = " " + outp
        myLength += 1
    return outp

def fuzzeSelectMaxScore(pattern,data:iter)->list:
    matching = list()
    direktMatch = False
    score = 0
    for x in data:
        if(x == wireName):direktMatch = True
        newScore = fuzzyFindScore(x,pattern)
        if(newScore > score):
            score = newScore
            matching.clear()
        if(newScore == score):
            matching.append(x)
    if(direktMatch):
        return [pattern]
    return matching


class Position:
    __slots__ = ("x","y")
    def __init__(self,x,y):
        self.x = x
        self.y = y


class App:
    nameLength = 9
    __slots__ = ("data","fileName","wires","staticWires","position","error")
    def __init__(self):
        self.data = None
        self.fileName = ""
        self.wires = list()
        self.staticWires = list()
        self.position = Position(0,0)
        self.error = None
        self.redraw()

    def openNewFile(self,fname):
        try:
            with open(fname,"r")as fptr:
                data = fptr.read()
        except:
            self.error = "Error during the opening of a file"
            return
        self.error = None
        self.fileName = fname
        self.data = struct.doParse(data)
        self.position = Position(0,0)
        self.staticWires = list()
        self.wires = list()

    def getInputCmd(self):
        gotoPlace(1,1)
        command = canCancelInput(":")
        if(command is None):return
        if(command.startswith("o ")):
            self.openNewFile(command[2:])
        if(command.isnumeric()):
            self.position.x = int(command)
        if(command == "list" or command.startswith("list ")):
            expr = command[5:]
            for x in self.data.longMap:
                if(x.startswith(expr)):
                    print(x)

    def getAddWire(self):
        if(self.data is None):
            self.error = "You need to open a file!"
            return
        def _getAddWire(pre:str,suf:str)->(str,str):
            if(len(pre) == 0):return pre,suf
            prepend = ""
            if(pre[0] == "*"):
                prepend = "*"
                pre = pre[1:]
            score = 0
            found = pre
            for x in self.data.longMap:
                newScore = fuzzyFindScore(x,pre)
                if(newScore > score):
                    score = newScore
                    found = x
            return prepend+found,suf
        gotoPlace(1,1)
        wireName = canCancelInput("+",complete=_getAddWire)
        if(wireName is None):return
        listing = self.wires
        if(wireName[0] == "*"):
            listing = self.staticWires
            wireName = wireName[1:]
        matching = list()
        matchBlock = list()
        direktMatch = False
        score = 0
        for x,baseWire in self.data.longMap.items():
            if(x == wireName):direktMatch = True
            newScore = fuzzyFindScore(x,wireName)
            if(newScore > score):
                score = newScore
                matchBlock.clear()
                matching.clear()
            if(newScore == score):
                if(baseWire.short in matchBlock):
                    continue
                matching.append(x)
                matchBlock.append(baseWire.short)
        matching = fuzzeSelectMaxScore(wireName,self.data.longMap)
        #TODO
        if(direktMatch):
            listing.append(tuple(wireName.split(".")))
        else:
            for x in matching:
                listing.append(tuple(x.split(".")))

    def run(self,input:str):
        if(len(input) == 0):return True
        didConsume = False
        step = 1
        if(len(input) == 1 and ord("A") <= ord(input) <= ord("Z")):
            step = 10
        doRedraw = False
        if(input in ("0",               )): self.position.x  = 0   ;doRedraw = True
        if(input in ("l","L",     "\x06")): self.position.x += step;doRedraw = True
        if(input in ("h","H",     "\x02")): self.position.x -= step;doRedraw = True
        if(input in ("k","K","\n","\x0e")): self.position.y += step;doRedraw = True
        if(input in ("j","J",     "\x10")): self.position.y -= step;doRedraw = True
        if(input == ":"): self.getInputCmd(); doRedraw = True
        if(input == "+"): self.getAddWire(); doRedraw = True
        if(doRedraw):
            self.doClip()
            self.redraw()
        didConsume |= doRedraw
        return didConsume


    def doClip(self):
        if(self.position.x < 0):
            self.position.x = 0
        if(self.position.y < 0):
            self.position.y = 0
        if(self.position.x > self.data.stamps[-1].stamp):
            self.position.x = self.data.stamps[-1].stamp
        if(self.position.y > len(self.wires)):
            self.position.y = len(self.wires)

    def redraw(self):
        tsize = os.get_terminal_size()
        if(self.error is not None):
            gotoPlace(1,1)
            print(error)
        if(self.data == None):
            gotoPlace(1,1)
            print("You need to open a file!")
            return
        goDown = 2
        gotoPlace(1,goDown)
        print(end=f"{self.fileName}  {self.data.info.date}  "
                  f"{self.data.info.version}  {self.data.info.timescale}  "
                  f"{self.data.stamps[-1].stamp}")
        goDown += 1
        gotoPlace(1,goDown)
        print(end=" " * App.nameLength)
        self.drawTimeStamp(tsize)
        goDown += 1
        for wire in self.staticWires:
            if(goDown > tsize.lines):return
            gotoPlace(1,goDown)
            print(end=f"*{makeAsLength(wire[-1],App.nameLength - 2)} ")
            self.drawForWire(wire,tsize)
            goDown += 1

        for idx,wire in enumerate(self.wires):
            if(idx < self.position.y):continue
            if(goDown > tsize.lines):return
            gotoPlace(1,goDown)
            #print(end=f"{makeAsLength(wire[-1],App.nameLength - 1)} ")
            print(end=f"{makeAsLength(".".join(wire)[-App.nameLength + 1:],App.nameLength - 1)} ")
            self.drawForWire(wire,tsize)
            goDown += 1

        print(end="",flush=True)

    def drawTimeStamp(self,tsize:os.terminal_size):
        for stamp in range(self.position.x,self.position.x + (tsize.columns - App.nameLength)//5):
            print(end=f" {makeAsLength(str(stamp),4)}")

    def drawForWire(self,wire:tuple,tsize:os.terminal_size):
        nameWire = ".".join(wire)
        wireBase = self.data.longMap.get(nameWire,None)
        if(wireBase is None):
            print(end="?")
            return
        idx = 0
        oldBase = None
        for stamp in range(self.position.x,self.position.x + (tsize.columns - App.nameLength)//5):
            while(idx < len(wireBase.assign) and wireBase.assign[idx].time.stamp <= stamp):
                idx += 1
            if(idx > len(wireBase.assign)):break
            if(idx == 0):continue
            base = wireBase.assign[idx-1]
            if(oldBase is not base):
                print(end="|")
            else:
                print(end=" ")
            print(end=bin2ColorHex(base.value,4))
            oldBase = base



try:
    clear()
    a = App()
    if(len(sys.argv) > 1):
        a.openNewFile(sys.argv[1])
    a.redraw()
    while 1:
        try:
            c = sys.stdin.read(1)
            if(not a.run(c)):
                print("Got character", repr(c))
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

