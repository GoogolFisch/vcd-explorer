#!/usr/bin/env python3

import pars
import sys

class WaveData:
    __slots__ = ("name","value","time")
    def __init__(self,time:WaveTime,value:str,name:str):
        self.name  = name
        self.value = value
        self.time  = time

class WaveTime:
    __slots__= ("stamp","data")
    def __init__(self,stamp:int):
        self.stamp = stamp
        self.data  = list()
    def append(self,wd:WaveData):
        self.data.append(wd)

class WaveMap:
    __slots__ = ("names","typ","size","short","assign")
    def __init__(self,typ:str,size:int,short:str,name:tuple):
        self.names  = [name]
        self.typ    = typ
        self.size   = size
        self.short  = short
        self.assign = list()
    def setAlias(self,other:WaveMap):
        self.names += other.names
        # Other things could be different.....
    def addTo(self,data:WaveData):
        while(len(data.value) < self.size):
            data.value = "0" + data.value
        self.assign.append(data)

class ScopeInfo:
    __slots__ = ("date","version","timescale")
    def __init__(self):
        self.date = self.version = self.timescale = str()
    def __str__(self):
        return f"({self.date},{self.version},{self.timescale})"

class ScopeWave:
    __slots__ = ("info","map","longMap","stamps")
    def __init__(self,node:pars.Node):
        self.map     = dict()
        self.longMap = dict()
        self.stamps  = list()
        self.info    = ScopeInfo()
        if(len(node.children) > 0):
            self._parseNode(node.children[0])


    def _parseNode(self,node:pars.Node):
        for sub in node.children:
            if(sub.name == "HeadDate"):
                self.info.date = sub.children[0].getRaw().strip()
            elif(sub.name == "HeadVersion"):
                self.info.version = sub.children[0].getRaw().strip()
            elif(sub.name == "HeadTimescale"):
                self.info.timescale = sub.children[0].getRaw().strip()
            elif(sub.name == "HeadScope"):
                self._parseModule(sub)
            elif(sub.name == "HeadDump"):
                self._parseDump(sub)

    def _parseModule(self,node:pars.Node,prefix=list()):
        name  = node.children[0]
        child = node.children[1]
        prefix = prefix + [name.children[1].getRaw()]
        for sub in child.children:
            if(sub.name == "ScopeNewVar"):
                subp = prefix + [sub.children[3].getRaw()]
                wm = WaveMap(
                        sub.children[0].getRaw(),
                        int(sub.children[1].getRaw()),
                        sub.children[2].getRaw(),
                        tuple(subp))
                fetch = self.map.get(wm.short,None)
                self.longMap[".".join(subp)] = wm
                if(fetch is not None):
                    fetch.setAlias(wm)
                else:
                    self.map[wm.short] = wm
            elif(sub.name == "HeadScope"):
                self._parseModule(sub,prefix)

    def _parseDump(self,node:pars.Node):
        for timeNode in node.children:
            wt = WaveTime(int(timeNode.children[0].getRaw()[1:]))
            self.stamps.append(wt)
            for dumpNode in timeNode.children[1].children:
                wd = WaveData(wt,
                              self._parseValue(dumpNode.children[0].getRaw()),
                              dumpNode.children[1].getRaw())
                wt.append(wd)
                self.map[wd.name].addTo(wd)

    def _parseValue(self,data:str)->list(str):
        if(data[0] in "01xz"):
            return data[0]
        return data[1:]

    def __str__(self):
        data = f"{self.info}-{self.stamps[-1].stamp}\n"
        wire = list(self.map.values())[0]
        data += " ".join([".".join(x) for x in wire.names])
        return data

def doParse(data)->ScopeWave:
    lp = pars.Parser.parse(data)
    #print(lp.print())
    sc = ScopeWave(lp)
    return sc

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file,"r")as fptr:
        data = fptr.read()
    sc = doParse(data)
    print(sc)

