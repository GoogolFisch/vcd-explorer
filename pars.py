""" 
This was generated
"""

class Location:
    __slots__ = ("row","col","idx","endRow","endCol","endIdx")
    def __init__(self):
        self.row = self.col = self.endRow = self.endCol = 1
        self.idx = self.endIdx = 0
    def incr(self):
        self.idx += 1
        self.col += 1
        self.endIdx = self.idx
        self.endCol = self.col
    def incrLine(self):
        self.col  = 1
        self.row += 1
        self.endIdx = self.idx
        self.endCol = self.col
    def setRange(self,other:Location):
        self.endIdx = other.endIdx
        self.endCol = other.endCol
        self.endRow = other.endRow
    def update(self,other:Location):
        self.idx = other.endIdx
        self.row = other.endRow
        self.col = other.endCol
        self.endIdx = self.idx
        self.endRow = self.row
        self.endCol = self.col
    def copy(self)->Location:
        l = Location()
        l.row = self.row
        l.col = self.col
        l.idx = self.idx
        l.endRow = self.endRow
        l.endCol = self.endCol
        l.endIdx = self.endIdx
        return l
    def __str__(self):
        return f"({self.row}:{self.col},{self.idx} - {self.endRow}:{self.endCol},{self.endIdx})"
class Node:
    __slots__ = ("__dict__","isRaw","data","name","loc","children")
    def __init__(self,data:str,loc:Location,name:str):
        self.data = data
        self.name = name
        self.loc  = loc
        self.children = list()
        self.isRaw = False
    @staticmethod
    def fromRange(data:str,name:str,loc:Location,next:int)->Node:
        n = Node(data,loc.copy(),name)
        n.loc.endIdx = next
        n.loc.endRow = loc.row
        n.loc.endCol = loc.col
        for i in range(n.loc.idx,n.loc.endIdx):
            n.loc.endCol += 1
            if(data[i] == "\n"):
                n.loc.endCol = 1
                n.loc.endRow += 1
        n.isRaw = True
        return n
    def addChild(self,child:Node):
        self.children.append(child)
    def addChildrenOf(self,child):
        self.children += child.children
    def setRange(self,loc:Location):
        self.endIdx = loc.endIdx
        self.endRow = loc.endRow
        self.endCol = loc.endCol
    def getRaw(self)->str:
        return self.data[self.loc.idx:self.loc.endIdx]
    def print(self,indent:int=0)->str:
        s = " "*indent + f"<{self.loc} {self.name} "
        if(self.isRaw):
            s += f"{self.getRaw()}"
        for ch in self.children:
            s += "\n" + ch.print(indent + 1)
        s += ">"
        return s

class Parser:
  @staticmethod
  def parse(data:str):
    return Parser.__(data,Location())

  def _regSStatement(data:str,loc:Location):
    _x0 = Parser._regSStatement0(data,loc)
    if(_x0):return _x0
    return None
  def _regSScope(data:str,loc:Location):
    _x1 = Parser._regSScope1(data,loc)
    if(_x1):return _x1
    return None
  def _regSEnd(data:str,loc:Location):
    _x2 = Parser._regSEnd2(data,loc)
    if(_x2):return _x2
    return None
  def _regSVar(data:str,loc:Location):
    _x3 = Parser._regSVar3(data,loc)
    if(_x3):return _x3
    return None
  def _regSscope(data:str,loc:Location):
    _x4 = Parser._regSscope4(data,loc)
    if(_x4):return _x4
    return None
  def _regSDumpvars(data:str,loc:Location):
    _x5 = Parser._regSDumpvars5(data,loc)
    if(_x5):return _x5
    return None
  def _regSDumpall(data:str,loc:Location):
    _x6 = Parser._regSDumpall6(data,loc)
    if(_x6):return _x6
    return None
  def _regSDate(data:str,loc:Location):
    _x7 = Parser._regSDate7(data,loc)
    if(_x7):return _x7
    return None
  def _regSVersion(data:str,loc:Location):
    _x8 = Parser._regSVersion8(data,loc)
    if(_x8):return _x8
    return None
  def _regSTimescale(data:str,loc:Location):
    _x9 = Parser._regSTimescale9(data,loc)
    if(_x9):return _x9
    return None
  def _regSUpscope(data:str,loc:Location):
    _xa = Parser._regSUpscope10(data,loc)
    if(_xa):return _xa
    return None
  def _regSDumpAll(data:str,loc:Location):
    _xb = Parser._regSDumpAll11(data,loc)
    if(_xb):return _xb
    return None
  def _regSComment(data:str,loc:Location):
    _xc = Parser._regSComment12(data,loc)
    if(_xc):return _xc
    return None
  def _regSEnddefinitions(data:str,loc:Location):
    _xd = Parser._regSEnddefinitions13(data,loc)
    if(_xd):return _xd
    return None
  def _regRegion(data:str,loc:Location):
    _xe = Parser._regRegion14(data,loc)
    if(_xe):return _xe
    return None
  def _regBinary(data:str,loc:Location):
    _xf = Parser._regBinary15(data,loc)
    if(_xf):return _xf
    return None
  def _charNewLine(data:str,loc:Location):
    _x10 = Parser._charNewLine16(data,loc)
    if(_x10):return _x10
    return None
  def _charBinValue(data:str,loc:Location):
    _x11 = Parser._charBinValue17(data,loc)
    if(_x11):return _x11
    return None
  def _regTimestep(data:str,loc:Location):
    _x12 = Parser._regTimestep18(data,loc)
    if(_x12):return _x12
    return None
  def _regNumber(data:str,loc:Location):
    _x13 = Parser._regNumber19(data,loc)
    if(_x13):return _x13
    return None
  def _regSpace(data:str,loc:Location):
    _x14 = Parser._regSpace20(data,loc)
    if(_x14):return _x14
    return None
  def _regRange(data:str,loc:Location):
    _x15 = Parser._regRange21(data,loc)
    if(_x15):return _x15
    return None
  def _regTillLine(data:str,loc:Location):
    _x16 = Parser._regTillLine22(data,loc)
    if(_x16):return _x16
    return None
  def _regWord(data:str,loc:Location):
    _x17 = Parser._regWord23(data,loc)
    if(_x17):return _x17
    return None
  def _HeadDate(data:str,loc:Location):
    _x18 = Parser._HeadDate24(data,loc)
    if(_x18):return _x18
    return None
  def _HeadVersion(data:str,loc:Location):
    _x19 = Parser._HeadVersion25(data,loc)
    if(_x19):return _x19
    return None
  def _HeadComment(data:str,loc:Location):
    _x1a = Parser._HeadComment26(data,loc)
    if(_x1a):return _x1a
    return None
  def _HeadTimescale(data:str,loc:Location):
    _x1b = Parser._HeadTimescale27(data,loc)
    if(_x1b):return _x1b
    return None
  def _HeadEndDef(data:str,loc:Location):
    _x1c = Parser._HeadEndDef28(data,loc)
    if(_x1c):return _x1c
    return None
  def _HeadDumpAll(data:str,loc:Location):
    _x1d = Parser._HeadDumpAll29(data,loc)
    if(_x1d):return _x1d
    return None
  def _HeadDump(data:str,loc:Location):
    _x1e = Parser._HeadDump30(data,loc)
    if(_x1e):return _x1e
    _x1f = Parser._HeadDump31(data,loc)
    if(_x1f):return _x1f
    return None
  def _HeadTimeStep(data:str,loc:Location):
    _x20 = Parser._HeadTimeStep32(data,loc)
    if(_x20):return _x20
    return None
  def _BodyTimeStep(data:str,loc:Location):
    _x21 = Parser._BodyTimeStep33(data,loc)
    if(_x21):return _x21
    _x22 = Parser._BodyTimeStep34(data,loc)
    if(_x22):return _x22
    return None
  def _BodyDump(data:str,loc:Location):
    _x23 = Parser._BodyDump35(data,loc)
    if(_x23):return _x23
    _x24 = Parser._BodyDump36(data,loc)
    if(_x24):return _x24
    return None
  def _BodyDumpIgnore(data:str,loc:Location):
    _x25 = Parser._BodyDumpIgnore37(data,loc)
    if(_x25):return _x25
    return None
  def _HeadScope(data:str,loc:Location):
    _x26 = Parser._HeadScope38(data,loc)
    if(_x26):return _x26
    return None
  def _BodyScope(data:str,loc:Location):
    _x27 = Parser._BodyScope39(data,loc)
    if(_x27):return _x27
    _x28 = Parser._BodyScope40(data,loc)
    if(_x28):return _x28
    return None
  def _ScopeModule(data:str,loc:Location):
    _x29 = Parser._ScopeModule41(data,loc)
    if(_x29):return _x29
    return None
  def _ScopeNewVar(data:str,loc:Location):
    _x2a = Parser._ScopeNewVar42(data,loc)
    if(_x2a):return _x2a
    return None
  def __(data:str,loc:Location):
    _x2b = Parser.__43(data,loc)
    if(_x2b):return _x2b
    return None
  def _Start(data:str,loc:Location):
    _x2c = Parser._Start44(data,loc)
    if(_x2c):return _x2c
    _x2d = Parser._Start45(data,loc)
    if(_x2d):return _x2d
    _x2e = Parser._Start46(data,loc)
    if(_x2e):return _x2e
    _x2f = Parser._Start47(data,loc)
    if(_x2f):return _x2f
    _x30 = Parser._Start48(data,loc)
    if(_x30):return _x30
    _x31 = Parser._Start49(data,loc)
    if(_x31):return _x31
    _x32 = Parser._Start50(data,loc)
    if(_x32):return _x32
    return None
  def _regSStatement0(data:str,loc:Location):
    offset = loc.idx
    _x33 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x33 = True
    if(_x33 and offset < len(data)):offset += 1
    else:return None
    _x35 = False
    while(True):
      _x34 = False
      if(len(data) > offset and ord(data[offset]) >= 97 and ord(data[offset]) < 123):_x34 = True
      if(not _x34 or offset >= len(data)):break
      offset += 1
      _x35=True
    if(not _x35):return None
    return Node.fromRange(data,"regSStatement",loc,offset)
  def _regSScope1(data:str,loc:Location):
    offset = loc.idx
    _x36 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x36 = True
    if(_x36 and offset < len(data)):offset += 1
    else:return None
    _x37 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x37 = True
    if(_x37 and offset < len(data)):offset += 1
    else:return None
    _x38 = False
    if(len(data) > offset and ord(data[offset]) == 99):_x38 = True
    if(_x38 and offset < len(data)):offset += 1
    else:return None
    _x39 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x39 = True
    if(_x39 and offset < len(data)):offset += 1
    else:return None
    _x3a = False
    if(len(data) > offset and ord(data[offset]) == 112):_x3a = True
    if(_x3a and offset < len(data)):offset += 1
    else:return None
    _x3b = False
    if(len(data) > offset and ord(data[offset]) == 101):_x3b = True
    if(_x3b and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSScope",loc,offset)
  def _regSEnd2(data:str,loc:Location):
    offset = loc.idx
    _x3c = False
    if(len(data) > offset and ord(data[offset]) == 36):_x3c = True
    if(_x3c and offset < len(data)):offset += 1
    else:return None
    _x3d = False
    if(len(data) > offset and ord(data[offset]) == 101):_x3d = True
    if(_x3d and offset < len(data)):offset += 1
    else:return None
    _x3e = False
    if(len(data) > offset and ord(data[offset]) == 110):_x3e = True
    if(_x3e and offset < len(data)):offset += 1
    else:return None
    _x3f = False
    if(len(data) > offset and ord(data[offset]) == 100):_x3f = True
    if(_x3f and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSEnd",loc,offset)
  def _regSVar3(data:str,loc:Location):
    offset = loc.idx
    _x40 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x40 = True
    if(_x40 and offset < len(data)):offset += 1
    else:return None
    _x41 = False
    if(len(data) > offset and ord(data[offset]) == 118):_x41 = True
    if(_x41 and offset < len(data)):offset += 1
    else:return None
    _x42 = False
    if(len(data) > offset and ord(data[offset]) == 97):_x42 = True
    if(_x42 and offset < len(data)):offset += 1
    else:return None
    _x43 = False
    if(len(data) > offset and ord(data[offset]) == 114):_x43 = True
    if(_x43 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSVar",loc,offset)
  def _regSscope4(data:str,loc:Location):
    offset = loc.idx
    _x44 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x44 = True
    if(_x44 and offset < len(data)):offset += 1
    else:return None
    _x45 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x45 = True
    if(_x45 and offset < len(data)):offset += 1
    else:return None
    _x46 = False
    if(len(data) > offset and ord(data[offset]) == 99):_x46 = True
    if(_x46 and offset < len(data)):offset += 1
    else:return None
    _x47 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x47 = True
    if(_x47 and offset < len(data)):offset += 1
    else:return None
    _x48 = False
    if(len(data) > offset and ord(data[offset]) == 112):_x48 = True
    if(_x48 and offset < len(data)):offset += 1
    else:return None
    _x49 = False
    if(len(data) > offset and ord(data[offset]) == 101):_x49 = True
    if(_x49 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSscope",loc,offset)
  def _regSDumpvars5(data:str,loc:Location):
    offset = loc.idx
    _x4a = False
    if(len(data) > offset and ord(data[offset]) == 36):_x4a = True
    if(_x4a and offset < len(data)):offset += 1
    else:return None
    _x4b = False
    if(len(data) > offset and ord(data[offset]) == 100):_x4b = True
    if(_x4b and offset < len(data)):offset += 1
    else:return None
    _x4c = False
    if(len(data) > offset and ord(data[offset]) == 117):_x4c = True
    if(_x4c and offset < len(data)):offset += 1
    else:return None
    _x4d = False
    if(len(data) > offset and ord(data[offset]) == 109):_x4d = True
    if(_x4d and offset < len(data)):offset += 1
    else:return None
    _x4e = False
    if(len(data) > offset and ord(data[offset]) == 112):_x4e = True
    if(_x4e and offset < len(data)):offset += 1
    else:return None
    _x4f = False
    if(len(data) > offset and ord(data[offset]) == 118):_x4f = True
    if(_x4f and offset < len(data)):offset += 1
    else:return None
    _x50 = False
    if(len(data) > offset and ord(data[offset]) == 97):_x50 = True
    if(_x50 and offset < len(data)):offset += 1
    else:return None
    _x51 = False
    if(len(data) > offset and ord(data[offset]) == 114):_x51 = True
    if(_x51 and offset < len(data)):offset += 1
    else:return None
    _x52 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x52 = True
    if(_x52 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSDumpvars",loc,offset)
  def _regSDumpall6(data:str,loc:Location):
    offset = loc.idx
    _x53 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x53 = True
    if(_x53 and offset < len(data)):offset += 1
    else:return None
    _x54 = False
    if(len(data) > offset and ord(data[offset]) == 100):_x54 = True
    if(_x54 and offset < len(data)):offset += 1
    else:return None
    _x55 = False
    if(len(data) > offset and ord(data[offset]) == 117):_x55 = True
    if(_x55 and offset < len(data)):offset += 1
    else:return None
    _x56 = False
    if(len(data) > offset and ord(data[offset]) == 109):_x56 = True
    if(_x56 and offset < len(data)):offset += 1
    else:return None
    _x57 = False
    if(len(data) > offset and ord(data[offset]) == 112):_x57 = True
    if(_x57 and offset < len(data)):offset += 1
    else:return None
    _x58 = False
    if(len(data) > offset and ord(data[offset]) == 97):_x58 = True
    if(_x58 and offset < len(data)):offset += 1
    else:return None
    _x59 = False
    if(len(data) > offset and ord(data[offset]) == 108):_x59 = True
    if(_x59 and offset < len(data)):offset += 1
    else:return None
    _x5a = False
    if(len(data) > offset and ord(data[offset]) == 108):_x5a = True
    if(_x5a and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSDumpall",loc,offset)
  def _regSDate7(data:str,loc:Location):
    offset = loc.idx
    _x5b = False
    if(len(data) > offset and ord(data[offset]) == 36):_x5b = True
    if(_x5b and offset < len(data)):offset += 1
    else:return None
    _x5c = False
    if(len(data) > offset and ord(data[offset]) == 100):_x5c = True
    if(_x5c and offset < len(data)):offset += 1
    else:return None
    _x5d = False
    if(len(data) > offset and ord(data[offset]) == 97):_x5d = True
    if(_x5d and offset < len(data)):offset += 1
    else:return None
    _x5e = False
    if(len(data) > offset and ord(data[offset]) == 116):_x5e = True
    if(_x5e and offset < len(data)):offset += 1
    else:return None
    _x5f = False
    if(len(data) > offset and ord(data[offset]) == 101):_x5f = True
    if(_x5f and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSDate",loc,offset)
  def _regSVersion8(data:str,loc:Location):
    offset = loc.idx
    _x60 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x60 = True
    if(_x60 and offset < len(data)):offset += 1
    else:return None
    _x61 = False
    if(len(data) > offset and ord(data[offset]) == 118):_x61 = True
    if(_x61 and offset < len(data)):offset += 1
    else:return None
    _x62 = False
    if(len(data) > offset and ord(data[offset]) == 101):_x62 = True
    if(_x62 and offset < len(data)):offset += 1
    else:return None
    _x63 = False
    if(len(data) > offset and ord(data[offset]) == 114):_x63 = True
    if(_x63 and offset < len(data)):offset += 1
    else:return None
    _x64 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x64 = True
    if(_x64 and offset < len(data)):offset += 1
    else:return None
    _x65 = False
    if(len(data) > offset and ord(data[offset]) == 105):_x65 = True
    if(_x65 and offset < len(data)):offset += 1
    else:return None
    _x66 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x66 = True
    if(_x66 and offset < len(data)):offset += 1
    else:return None
    _x67 = False
    if(len(data) > offset and ord(data[offset]) == 110):_x67 = True
    if(_x67 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSVersion",loc,offset)
  def _regSTimescale9(data:str,loc:Location):
    offset = loc.idx
    _x68 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x68 = True
    if(_x68 and offset < len(data)):offset += 1
    else:return None
    _x69 = False
    if(len(data) > offset and ord(data[offset]) == 116):_x69 = True
    if(_x69 and offset < len(data)):offset += 1
    else:return None
    _x6a = False
    if(len(data) > offset and ord(data[offset]) == 105):_x6a = True
    if(_x6a and offset < len(data)):offset += 1
    else:return None
    _x6b = False
    if(len(data) > offset and ord(data[offset]) == 109):_x6b = True
    if(_x6b and offset < len(data)):offset += 1
    else:return None
    _x6c = False
    if(len(data) > offset and ord(data[offset]) == 101):_x6c = True
    if(_x6c and offset < len(data)):offset += 1
    else:return None
    _x6d = False
    if(len(data) > offset and ord(data[offset]) == 115):_x6d = True
    if(_x6d and offset < len(data)):offset += 1
    else:return None
    _x6e = False
    if(len(data) > offset and ord(data[offset]) == 99):_x6e = True
    if(_x6e and offset < len(data)):offset += 1
    else:return None
    _x6f = False
    if(len(data) > offset and ord(data[offset]) == 97):_x6f = True
    if(_x6f and offset < len(data)):offset += 1
    else:return None
    _x70 = False
    if(len(data) > offset and ord(data[offset]) == 108):_x70 = True
    if(_x70 and offset < len(data)):offset += 1
    else:return None
    _x71 = False
    if(len(data) > offset and ord(data[offset]) == 101):_x71 = True
    if(_x71 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSTimescale",loc,offset)
  def _regSUpscope10(data:str,loc:Location):
    offset = loc.idx
    _x72 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x72 = True
    if(_x72 and offset < len(data)):offset += 1
    else:return None
    _x73 = False
    if(len(data) > offset and ord(data[offset]) == 117):_x73 = True
    if(_x73 and offset < len(data)):offset += 1
    else:return None
    _x74 = False
    if(len(data) > offset and ord(data[offset]) == 112):_x74 = True
    if(_x74 and offset < len(data)):offset += 1
    else:return None
    _x75 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x75 = True
    if(_x75 and offset < len(data)):offset += 1
    else:return None
    _x76 = False
    if(len(data) > offset and ord(data[offset]) == 99):_x76 = True
    if(_x76 and offset < len(data)):offset += 1
    else:return None
    _x77 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x77 = True
    if(_x77 and offset < len(data)):offset += 1
    else:return None
    _x78 = False
    if(len(data) > offset and ord(data[offset]) == 112):_x78 = True
    if(_x78 and offset < len(data)):offset += 1
    else:return None
    _x79 = False
    if(len(data) > offset and ord(data[offset]) == 101):_x79 = True
    if(_x79 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSUpscope",loc,offset)
  def _regSDumpAll11(data:str,loc:Location):
    offset = loc.idx
    _x7a = False
    if(len(data) > offset and ord(data[offset]) == 36):_x7a = True
    if(_x7a and offset < len(data)):offset += 1
    else:return None
    _x7b = False
    if(len(data) > offset and ord(data[offset]) == 100):_x7b = True
    if(_x7b and offset < len(data)):offset += 1
    else:return None
    _x7c = False
    if(len(data) > offset and ord(data[offset]) == 117):_x7c = True
    if(_x7c and offset < len(data)):offset += 1
    else:return None
    _x7d = False
    if(len(data) > offset and ord(data[offset]) == 109):_x7d = True
    if(_x7d and offset < len(data)):offset += 1
    else:return None
    _x7e = False
    if(len(data) > offset and ord(data[offset]) == 112):_x7e = True
    if(_x7e and offset < len(data)):offset += 1
    else:return None
    _x7f = False
    if(len(data) > offset and ord(data[offset]) == 97):_x7f = True
    if(_x7f and offset < len(data)):offset += 1
    else:return None
    _x80 = False
    if(len(data) > offset and ord(data[offset]) == 108):_x80 = True
    if(_x80 and offset < len(data)):offset += 1
    else:return None
    _x81 = False
    if(len(data) > offset and ord(data[offset]) == 108):_x81 = True
    if(_x81 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSDumpAll",loc,offset)
  def _regSComment12(data:str,loc:Location):
    offset = loc.idx
    _x82 = False
    if(len(data) > offset and ord(data[offset]) == 36):_x82 = True
    if(_x82 and offset < len(data)):offset += 1
    else:return None
    _x83 = False
    if(len(data) > offset and ord(data[offset]) == 99):_x83 = True
    if(_x83 and offset < len(data)):offset += 1
    else:return None
    _x84 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x84 = True
    if(_x84 and offset < len(data)):offset += 1
    else:return None
    _x85 = False
    if(len(data) > offset and ord(data[offset]) == 109):_x85 = True
    if(_x85 and offset < len(data)):offset += 1
    else:return None
    _x86 = False
    if(len(data) > offset and ord(data[offset]) == 109):_x86 = True
    if(_x86 and offset < len(data)):offset += 1
    else:return None
    _x87 = False
    if(len(data) > offset and ord(data[offset]) == 101):_x87 = True
    if(_x87 and offset < len(data)):offset += 1
    else:return None
    _x88 = False
    if(len(data) > offset and ord(data[offset]) == 110):_x88 = True
    if(_x88 and offset < len(data)):offset += 1
    else:return None
    _x89 = False
    if(len(data) > offset and ord(data[offset]) == 116):_x89 = True
    if(_x89 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSComment",loc,offset)
  def _regSEnddefinitions13(data:str,loc:Location):
    offset = loc.idx
    _x8a = False
    if(len(data) > offset and ord(data[offset]) == 36):_x8a = True
    if(_x8a and offset < len(data)):offset += 1
    else:return None
    _x8b = False
    if(len(data) > offset and ord(data[offset]) == 101):_x8b = True
    if(_x8b and offset < len(data)):offset += 1
    else:return None
    _x8c = False
    if(len(data) > offset and ord(data[offset]) == 110):_x8c = True
    if(_x8c and offset < len(data)):offset += 1
    else:return None
    _x8d = False
    if(len(data) > offset and ord(data[offset]) == 100):_x8d = True
    if(_x8d and offset < len(data)):offset += 1
    else:return None
    _x8e = False
    if(len(data) > offset and ord(data[offset]) == 100):_x8e = True
    if(_x8e and offset < len(data)):offset += 1
    else:return None
    _x8f = False
    if(len(data) > offset and ord(data[offset]) == 101):_x8f = True
    if(_x8f and offset < len(data)):offset += 1
    else:return None
    _x90 = False
    if(len(data) > offset and ord(data[offset]) == 102):_x90 = True
    if(_x90 and offset < len(data)):offset += 1
    else:return None
    _x91 = False
    if(len(data) > offset and ord(data[offset]) == 105):_x91 = True
    if(_x91 and offset < len(data)):offset += 1
    else:return None
    _x92 = False
    if(len(data) > offset and ord(data[offset]) == 110):_x92 = True
    if(_x92 and offset < len(data)):offset += 1
    else:return None
    _x93 = False
    if(len(data) > offset and ord(data[offset]) == 105):_x93 = True
    if(_x93 and offset < len(data)):offset += 1
    else:return None
    _x94 = False
    if(len(data) > offset and ord(data[offset]) == 116):_x94 = True
    if(_x94 and offset < len(data)):offset += 1
    else:return None
    _x95 = False
    if(len(data) > offset and ord(data[offset]) == 105):_x95 = True
    if(_x95 and offset < len(data)):offset += 1
    else:return None
    _x96 = False
    if(len(data) > offset and ord(data[offset]) == 111):_x96 = True
    if(_x96 and offset < len(data)):offset += 1
    else:return None
    _x97 = False
    if(len(data) > offset and ord(data[offset]) == 110):_x97 = True
    if(_x97 and offset < len(data)):offset += 1
    else:return None
    _x98 = False
    if(len(data) > offset and ord(data[offset]) == 115):_x98 = True
    if(_x98 and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regSEnddefinitions",loc,offset)
  def _regRegion14(data:str,loc:Location):
    offset = loc.idx
    _x9a = False
    while(True):
      _x99 = False
      if(len(data) > offset and ord(data[offset]) == 36):_x99 = True
      _x99 = not _x99
      if(not _x99 or offset >= len(data)):break
      offset += 1
      _x9a=True
    if(not _x9a):return None
    return Node.fromRange(data,"regRegion",loc,offset)
  def _regBinary15(data:str,loc:Location):
    offset = loc.idx
    _x9b = False
    if(len(data) > offset and ord(data[offset]) == 98):_x9b = True
    if(_x9b and offset < len(data)):offset += 1
    else:return None
    _x9d = False
    while(True):
      _x9c = False
      if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 50):_x9c = True
      elif(len(data) > offset and ord(data[offset]) == 120):_x9c = True
      elif(len(data) > offset and ord(data[offset]) == 122):_x9c = True
      if(not _x9c or offset >= len(data)):break
      offset += 1
      _x9d=True
    if(not _x9d):return None
    return Node.fromRange(data,"regBinary",loc,offset)
  def _charNewLine16(data:str,loc:Location):
    offset = loc.idx
    _x9e = False
    if(len(data) > offset and ord(data[offset]) == 10):_x9e = True
    if(_x9e and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"charNewLine",loc,offset)
  def _charBinValue17(data:str,loc:Location):
    offset = loc.idx
    _x9f = False
    if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 50):_x9f = True
    elif(len(data) > offset and ord(data[offset]) == 120):_x9f = True
    elif(len(data) > offset and ord(data[offset]) == 122):_x9f = True
    if(_x9f and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"charBinValue",loc,offset)
  def _regTimestep18(data:str,loc:Location):
    offset = loc.idx
    _xa0 = False
    if(len(data) > offset and ord(data[offset]) == 35):_xa0 = True
    if(_xa0 and offset < len(data)):offset += 1
    else:return None
    _xa2 = False
    while(True):
      _xa1 = False
      if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 58):_xa1 = True
      if(not _xa1 or offset >= len(data)):break
      offset += 1
      _xa2=True
    if(not _xa2):return None
    return Node.fromRange(data,"regTimestep",loc,offset)
  def _regNumber19(data:str,loc:Location):
    offset = loc.idx
    _xa4 = False
    while(True):
      _xa3 = False
      if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 58):_xa3 = True
      if(not _xa3 or offset >= len(data)):break
      offset += 1
      _xa4=True
    if(not _xa4):return None
    return Node.fromRange(data,"regNumber",loc,offset)
  def _regSpace20(data:str,loc:Location):
    offset = loc.idx
    while(True):
      _xa5 = False
      if(len(data) > offset and ord(data[offset]) >= 9 and ord(data[offset]) < 11):_xa5 = True
      elif(len(data) > offset and ord(data[offset]) == 13):_xa5 = True
      elif(len(data) > offset and ord(data[offset]) == 32):_xa5 = True
      if(not _xa5 or offset >= len(data)):break
      offset += 1
    return Node.fromRange(data,"regSpace",loc,offset)
  def _regRange21(data:str,loc:Location):
    offset = loc.idx
    _xa6 = False
    if(len(data) > offset and ord(data[offset]) == 91):_xa6 = True
    if(_xa6 and offset < len(data)):offset += 1
    else:return None
    _xa8 = False
    while(True):
      _xa7 = False
      if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 58):_xa7 = True
      if(not _xa7 or offset >= len(data)):break
      offset += 1
      _xa8=True
    if(not _xa8):return None
    _xa9 = False
    if(len(data) > offset and ord(data[offset]) == 58):_xa9 = True
    if(_xa9 and offset < len(data)):offset += 1
    else:return None
    _xab = False
    while(True):
      _xaa = False
      if(len(data) > offset and ord(data[offset]) >= 48 and ord(data[offset]) < 58):_xaa = True
      if(not _xaa or offset >= len(data)):break
      offset += 1
      _xab=True
    if(not _xab):return None
    _xac = False
    if(len(data) > offset and ord(data[offset]) == 93):_xac = True
    if(_xac and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regRange",loc,offset)
  def _regTillLine22(data:str,loc:Location):
    offset = loc.idx
    while(True):
      _xad = False
      if(len(data) > offset and ord(data[offset]) == 10):_xad = True
      _xad = not _xad
      if(not _xad or offset >= len(data)):break
      offset += 1
    _xae = False
    if(len(data) > offset and ord(data[offset]) == 10):_xae = True
    if(_xae and offset < len(data)):offset += 1
    else:return None
    return Node.fromRange(data,"regTillLine",loc,offset)
  def _regWord23(data:str,loc:Location):
    offset = loc.idx
    _xb0 = False
    while(True):
      _xaf = False
      if(len(data) > offset and ord(data[offset]) >= 9 and ord(data[offset]) < 11):_xaf = True
      elif(len(data) > offset and ord(data[offset]) == 13):_xaf = True
      elif(len(data) > offset and ord(data[offset]) == 32):_xaf = True
      _xaf = not _xaf
      if(not _xaf or offset >= len(data)):break
      offset += 1
      _xb0=True
    if(not _xb0):return None
    return Node.fromRange(data,"regWord",loc,offset)
  def _HeadDate24(data:str,loc:Location):
    node = Node(data,loc,"HeadDate")
    _xb1 = Parser._regSDate(data,loc)
    if(not _xb1):return None
    if(_xb1):loc.update(_xb1.loc)
    _xb2 = Parser._regRegion(data,loc)
    if(_xb2):node.addChild(_xb2)
    if(not _xb2):return None
    if(_xb2):loc.update(_xb2.loc)
    _xb3 = Parser._regSEnd(data,loc)
    if(not _xb3):return None
    if(_xb3):loc.update(_xb3.loc)
    node.setRange(loc)
    return node
  def _HeadVersion25(data:str,loc:Location):
    node = Node(data,loc,"HeadVersion")
    _xb4 = Parser._regSVersion(data,loc)
    if(not _xb4):return None
    if(_xb4):loc.update(_xb4.loc)
    _xb5 = Parser._regRegion(data,loc)
    if(_xb5):node.addChild(_xb5)
    if(not _xb5):return None
    if(_xb5):loc.update(_xb5.loc)
    _xb6 = Parser._regSEnd(data,loc)
    if(not _xb6):return None
    if(_xb6):loc.update(_xb6.loc)
    node.setRange(loc)
    return node
  def _HeadComment26(data:str,loc:Location):
    node = Node(data,loc,"HeadComment")
    _xb7 = Parser._regSComment(data,loc)
    if(not _xb7):return None
    if(_xb7):loc.update(_xb7.loc)
    _xb8 = Parser._regRegion(data,loc)
    if(_xb8):node.addChild(_xb8)
    if(not _xb8):return None
    if(_xb8):loc.update(_xb8.loc)
    _xb9 = Parser._regSEnd(data,loc)
    if(not _xb9):return None
    if(_xb9):loc.update(_xb9.loc)
    node.setRange(loc)
    return node
  def _HeadTimescale27(data:str,loc:Location):
    node = Node(data,loc,"HeadTimescale")
    _xba = Parser._regSTimescale(data,loc)
    if(not _xba):return None
    if(_xba):loc.update(_xba.loc)
    _xbb = Parser._regRegion(data,loc)
    if(_xbb):node.addChild(_xbb)
    if(not _xbb):return None
    if(_xbb):loc.update(_xbb.loc)
    _xbc = Parser._regSEnd(data,loc)
    if(not _xbc):return None
    if(_xbc):loc.update(_xbc.loc)
    node.setRange(loc)
    return node
  def _HeadEndDef28(data:str,loc:Location):
    node = Node(data,loc,"HeadEndDef")
    _xbd = Parser._regSEnddefinitions(data,loc)
    if(not _xbd):return None
    if(_xbd):loc.update(_xbd.loc)
    _xbe = Parser._regSpace(data,loc)
    if(not _xbe):return None
    if(_xbe):loc.update(_xbe.loc)
    _xbf = Parser._regSEnd(data,loc)
    if(not _xbf):return None
    if(_xbf):loc.update(_xbf.loc)
    node.setRange(loc)
    return node
  def _HeadDumpAll29(data:str,loc:Location):
    node = Node(data,loc,"HeadDumpAll")
    _xc0 = Parser._regSDumpall(data,loc)
    if(not _xc0):return None
    if(_xc0):loc.update(_xc0.loc)
    _xc1 = Parser._regSpace(data,loc)
    if(not _xc1):return None
    if(_xc1):loc.update(_xc1.loc)
    _xc2 = Parser._regSEnd(data,loc)
    if(not _xc2):return None
    if(_xc2):loc.update(_xc2.loc)
    _xc3 = Parser._regSpace(data,loc)
    if(not _xc3):return None
    if(_xc3):loc.update(_xc3.loc)
    _xc4 = Parser._HeadDump(data,loc)
    if(_xc4):node.addChildrenOf(_xc4)
    if(not _xc4):return None
    node.name = _xc4.name
    if(_xc4):loc.update(_xc4.loc)
    node.setRange(loc)
    return node
  def _HeadDump30(data:str,loc:Location):
    node = Node(data,loc,"HeadDump")
    _xc5 = Parser._HeadTimeStep(data,loc)
    if(_xc5):node.addChild(_xc5)
    if(not _xc5):return None
    if(_xc5):loc.update(_xc5.loc)
    _xc6 = Parser._HeadTimeStep(data,loc)
    if(_xc6):node.addChild(_xc6)
    if(_xc6):loc.update(_xc6.loc)
    _xc7 = Parser._HeadTimeStep(data,loc)
    if(_xc7):node.addChild(_xc7)
    if(_xc7):loc.update(_xc7.loc)
    _xc8 = Parser._HeadDump(data,loc)
    if(_xc8):node.addChildrenOf(_xc8)
    if(_xc8):loc.update(_xc8.loc)
    node.setRange(loc)
    return node
  def _HeadDump31(data:str,loc:Location):
    node = Node(data,loc,"HeadDump")
    _xc9 = Parser._regSStatement(data,loc)
    if(not _xc9):return None
    if(_xc9):loc.update(_xc9.loc)
    _xca = Parser._HeadTimeStep(data,loc)
    if(_xca):node.addChild(_xca)
    if(_xca):loc.update(_xca.loc)
    _xcb = Parser._HeadTimeStep(data,loc)
    if(_xcb):node.addChild(_xcb)
    if(_xcb):loc.update(_xcb.loc)
    _xcc = Parser._HeadDump(data,loc)
    if(_xcc):node.addChildrenOf(_xcc)
    if(_xcc):loc.update(_xcc.loc)
    node.setRange(loc)
    return node
  def _HeadTimeStep32(data:str,loc:Location):
    node = Node(data,loc,"HeadTimeStep")
    _xcd = Parser._regTimestep(data,loc)
    if(_xcd):node.addChild(_xcd)
    if(not _xcd):return None
    if(_xcd):loc.update(_xcd.loc)
    _xce = Parser._regSpace(data,loc)
    if(not _xce):return None
    if(_xce):loc.update(_xce.loc)
    _xcf = Parser._BodyTimeStep(data,loc)
    if(_xcf):node.addChild(_xcf)
    if(not _xcf):return None
    if(_xcf):loc.update(_xcf.loc)
    node.setRange(loc)
    return node
  def _BodyTimeStep33(data:str,loc:Location):
    node = Node(data,loc,"BodyTimeStep")
    _xd0 = Parser._BodyDump(data,loc)
    if(_xd0):node.addChild(_xd0)
    if(not _xd0):return None
    if(_xd0):loc.update(_xd0.loc)
    _xd1 = Parser._regSpace(data,loc)
    if(not _xd1):return None
    if(_xd1):loc.update(_xd1.loc)
    _xd2 = Parser._BodyDump(data,loc)
    if(_xd2):node.addChild(_xd2)
    if(_xd2):loc.update(_xd2.loc)
    _xd3 = Parser._regSpace(data,loc)
    if(not _xd3):return None
    if(_xd3):loc.update(_xd3.loc)
    _xd4 = Parser._BodyDump(data,loc)
    if(_xd4):node.addChild(_xd4)
    if(_xd4):loc.update(_xd4.loc)
    _xd5 = Parser._regSpace(data,loc)
    if(not _xd5):return None
    if(_xd5):loc.update(_xd5.loc)
    _xd6 = Parser._BodyTimeStep(data,loc)
    if(_xd6):node.addChildrenOf(_xd6)
    if(_xd6):loc.update(_xd6.loc)
    node.setRange(loc)
    return node
  def _BodyTimeStep34(data:str,loc:Location):
    node = Node(data,loc,"BodyTimeStep")
    _xd7 = Parser._BodyDumpIgnore(data,loc)
    if(not _xd7):return None
    if(_xd7):loc.update(_xd7.loc)
    _xd8 = Parser._regSpace(data,loc)
    if(not _xd8):return None
    if(_xd8):loc.update(_xd8.loc)
    _xd9 = Parser._BodyDump(data,loc)
    if(_xd9):node.addChild(_xd9)
    if(_xd9):loc.update(_xd9.loc)
    _xda = Parser._regSpace(data,loc)
    if(not _xda):return None
    if(_xda):loc.update(_xda.loc)
    _xdb = Parser._BodyDump(data,loc)
    if(_xdb):node.addChild(_xdb)
    if(_xdb):loc.update(_xdb.loc)
    _xdc = Parser._regSpace(data,loc)
    if(not _xdc):return None
    if(_xdc):loc.update(_xdc.loc)
    _xdd = Parser._BodyTimeStep(data,loc)
    if(_xdd):node.addChildrenOf(_xdd)
    if(_xdd):loc.update(_xdd.loc)
    node.setRange(loc)
    return node
  def _BodyDump35(data:str,loc:Location):
    node = Node(data,loc,"BodyDump")
    _xde = Parser._regBinary(data,loc)
    if(_xde):node.addChild(_xde)
    if(not _xde):return None
    if(_xde):loc.update(_xde.loc)
    _xdf = Parser._regSpace(data,loc)
    if(not _xdf):return None
    if(_xdf):loc.update(_xdf.loc)
    _xe0 = Parser._regWord(data,loc)
    if(_xe0):node.addChild(_xe0)
    if(not _xe0):return None
    if(_xe0):loc.update(_xe0.loc)
    node.setRange(loc)
    return node
  def _BodyDump36(data:str,loc:Location):
    node = Node(data,loc,"BodyDump")
    _xe1 = Parser._charBinValue(data,loc)
    if(_xe1):node.addChild(_xe1)
    if(not _xe1):return None
    if(_xe1):loc.update(_xe1.loc)
    _xe2 = Parser._regWord(data,loc)
    if(_xe2):node.addChild(_xe2)
    if(not _xe2):return None
    if(_xe2):loc.update(_xe2.loc)
    node.setRange(loc)
    return node
  def _BodyDumpIgnore37(data:str,loc:Location):
    node = Node(data,loc,"BodyDumpIgnore")
    _xe3 = Parser._regSStatement(data,loc)
    if(not _xe3):return None
    if(_xe3):loc.update(_xe3.loc)
    _xe4 = Parser._regSpace(data,loc)
    if(not _xe4):return None
    if(_xe4):loc.update(_xe4.loc)
    node.setRange(loc)
    return node
  def _HeadScope38(data:str,loc:Location):
    node = Node(data,loc,"HeadScope")
    _xe5 = Parser._regSScope(data,loc)
    if(not _xe5):return None
    if(_xe5):loc.update(_xe5.loc)
    _xe6 = Parser._regSpace(data,loc)
    if(not _xe6):return None
    if(_xe6):loc.update(_xe6.loc)
    _xe7 = Parser._ScopeModule(data,loc)
    if(_xe7):node.addChild(_xe7)
    if(not _xe7):return None
    if(_xe7):loc.update(_xe7.loc)
    _xe8 = Parser._regSEnd(data,loc)
    if(not _xe8):return None
    if(_xe8):loc.update(_xe8.loc)
    _xe9 = Parser._regSpace(data,loc)
    if(not _xe9):return None
    if(_xe9):loc.update(_xe9.loc)
    _xea = Parser._BodyScope(data,loc)
    if(_xea):node.addChild(_xea)
    if(_xea):loc.update(_xea.loc)
    _xeb = Parser._regSUpscope(data,loc)
    if(not _xeb):return None
    if(_xeb):loc.update(_xeb.loc)
    _xec = Parser._regSpace(data,loc)
    if(not _xec):return None
    if(_xec):loc.update(_xec.loc)
    _xed = Parser._regSEnd(data,loc)
    if(not _xed):return None
    if(_xed):loc.update(_xed.loc)
    node.setRange(loc)
    return node
  def _BodyScope39(data:str,loc:Location):
    node = Node(data,loc,"BodyScope")
    _xee = Parser._regSVar(data,loc)
    if(not _xee):return None
    if(_xee):loc.update(_xee.loc)
    _xef = Parser._regSpace(data,loc)
    if(not _xef):return None
    if(_xef):loc.update(_xef.loc)
    _xf0 = Parser._ScopeNewVar(data,loc)
    if(_xf0):node.addChild(_xf0)
    if(not _xf0):return None
    if(_xf0):loc.update(_xf0.loc)
    _xf1 = Parser._regSpace(data,loc)
    if(not _xf1):return None
    if(_xf1):loc.update(_xf1.loc)
    _xf2 = Parser._regSEnd(data,loc)
    if(not _xf2):return None
    if(_xf2):loc.update(_xf2.loc)
    _xf3 = Parser._regSpace(data,loc)
    if(not _xf3):return None
    if(_xf3):loc.update(_xf3.loc)
    _xf4 = Parser._BodyScope(data,loc)
    if(_xf4):node.addChildrenOf(_xf4)
    if(_xf4):loc.update(_xf4.loc)
    node.setRange(loc)
    return node
  def _BodyScope40(data:str,loc:Location):
    node = Node(data,loc,"BodyScope")
    _xf5 = Parser._HeadScope(data,loc)
    if(_xf5):node.addChild(_xf5)
    if(not _xf5):return None
    if(_xf5):loc.update(_xf5.loc)
    _xf6 = Parser._regSpace(data,loc)
    if(not _xf6):return None
    if(_xf6):loc.update(_xf6.loc)
    _xf7 = Parser._BodyScope(data,loc)
    if(_xf7):node.addChildrenOf(_xf7)
    if(_xf7):loc.update(_xf7.loc)
    node.setRange(loc)
    return node
  def _ScopeModule41(data:str,loc:Location):
    node = Node(data,loc,"ScopeModule")
    _xf8 = Parser._regWord(data,loc)
    if(_xf8):node.addChild(_xf8)
    if(not _xf8):return None
    if(_xf8):loc.update(_xf8.loc)
    _xf9 = Parser._regSpace(data,loc)
    if(not _xf9):return None
    if(_xf9):loc.update(_xf9.loc)
    _xfa = Parser._regWord(data,loc)
    if(_xfa):node.addChild(_xfa)
    if(not _xfa):return None
    if(_xfa):loc.update(_xfa.loc)
    _xfb = Parser._regSpace(data,loc)
    if(not _xfb):return None
    if(_xfb):loc.update(_xfb.loc)
    node.setRange(loc)
    return node
  def _ScopeNewVar42(data:str,loc:Location):
    node = Node(data,loc,"ScopeNewVar")
    _xfc = Parser._regWord(data,loc)
    if(_xfc):node.addChild(_xfc)
    if(not _xfc):return None
    if(_xfc):loc.update(_xfc.loc)
    _xfd = Parser._regSpace(data,loc)
    if(not _xfd):return None
    if(_xfd):loc.update(_xfd.loc)
    _xfe = Parser._regNumber(data,loc)
    if(_xfe):node.addChild(_xfe)
    if(not _xfe):return None
    if(_xfe):loc.update(_xfe.loc)
    _xff = Parser._regSpace(data,loc)
    if(not _xff):return None
    if(_xff):loc.update(_xff.loc)
    _x100 = Parser._regWord(data,loc)
    if(_x100):node.addChild(_x100)
    if(not _x100):return None
    if(_x100):loc.update(_x100.loc)
    _x101 = Parser._regSpace(data,loc)
    if(not _x101):return None
    if(_x101):loc.update(_x101.loc)
    _x102 = Parser._regWord(data,loc)
    if(_x102):node.addChild(_x102)
    if(not _x102):return None
    if(_x102):loc.update(_x102.loc)
    _x103 = Parser._regSpace(data,loc)
    if(not _x103):return None
    if(_x103):loc.update(_x103.loc)
    _x104 = Parser._regRange(data,loc)
    if(_x104):node.addChild(_x104)
    if(_x104):loc.update(_x104.loc)
    _x105 = Parser._regSpace(data,loc)
    if(_x105):loc.update(_x105.loc)
    node.setRange(loc)
    return node
  def __43(data:str,loc:Location):
    node = Node(data,loc,"_")
    _x106 = Parser._Start(data,loc)
    if(_x106):node.addChild(_x106)
    if(not _x106):return None
    if(_x106):loc.update(_x106.loc)
    node.setRange(loc)
    return node
  def _Start44(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x107 = Parser._HeadVersion(data,loc)
    if(_x107):node.addChild(_x107)
    if(not _x107):return None
    if(_x107):loc.update(_x107.loc)
    _x108 = Parser._regSpace(data,loc)
    if(not _x108):return None
    if(_x108):loc.update(_x108.loc)
    _x109 = Parser._Start(data,loc)
    if(_x109):node.addChildrenOf(_x109)
    if(_x109):loc.update(_x109.loc)
    node.setRange(loc)
    return node
  def _Start45(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x10a = Parser._HeadDate(data,loc)
    if(_x10a):node.addChild(_x10a)
    if(not _x10a):return None
    if(_x10a):loc.update(_x10a.loc)
    _x10b = Parser._regSpace(data,loc)
    if(not _x10b):return None
    if(_x10b):loc.update(_x10b.loc)
    _x10c = Parser._Start(data,loc)
    if(_x10c):node.addChildrenOf(_x10c)
    if(_x10c):loc.update(_x10c.loc)
    node.setRange(loc)
    return node
  def _Start46(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x10d = Parser._HeadTimescale(data,loc)
    if(_x10d):node.addChild(_x10d)
    if(not _x10d):return None
    if(_x10d):loc.update(_x10d.loc)
    _x10e = Parser._regSpace(data,loc)
    if(not _x10e):return None
    if(_x10e):loc.update(_x10e.loc)
    _x10f = Parser._Start(data,loc)
    if(_x10f):node.addChildrenOf(_x10f)
    if(_x10f):loc.update(_x10f.loc)
    node.setRange(loc)
    return node
  def _Start47(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x110 = Parser._HeadScope(data,loc)
    if(_x110):node.addChild(_x110)
    if(not _x110):return None
    if(_x110):loc.update(_x110.loc)
    _x111 = Parser._regSpace(data,loc)
    if(not _x111):return None
    if(_x111):loc.update(_x111.loc)
    _x112 = Parser._Start(data,loc)
    if(_x112):node.addChildrenOf(_x112)
    if(_x112):loc.update(_x112.loc)
    node.setRange(loc)
    return node
  def _Start48(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x113 = Parser._HeadComment(data,loc)
    if(_x113):node.addChild(_x113)
    if(not _x113):return None
    if(_x113):loc.update(_x113.loc)
    _x114 = Parser._regSpace(data,loc)
    if(not _x114):return None
    if(_x114):loc.update(_x114.loc)
    _x115 = Parser._Start(data,loc)
    if(_x115):node.addChildrenOf(_x115)
    if(_x115):loc.update(_x115.loc)
    node.setRange(loc)
    return node
  def _Start49(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x116 = Parser._HeadEndDef(data,loc)
    if(_x116):node.addChild(_x116)
    if(not _x116):return None
    if(_x116):loc.update(_x116.loc)
    _x117 = Parser._regSpace(data,loc)
    if(not _x117):return None
    if(_x117):loc.update(_x117.loc)
    _x118 = Parser._Start(data,loc)
    if(_x118):node.addChildrenOf(_x118)
    if(_x118):loc.update(_x118.loc)
    node.setRange(loc)
    return node
  def _Start50(data:str,loc:Location):
    node = Node(data,loc,"Start")
    _x119 = Parser._HeadDumpAll(data,loc)
    if(_x119):node.addChild(_x119)
    if(not _x119):return None
    if(_x119):loc.update(_x119.loc)
    _x11a = Parser._regSpace(data,loc)
    if(not _x11a):return None
    if(_x11a):loc.update(_x11a.loc)
    _x11b = Parser._Start(data,loc)
    if(_x11b):node.addChildrenOf(_x11b)
    if(_x11b):loc.update(_x11b.loc)
    node.setRange(loc)
    return node
