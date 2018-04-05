# Kruskal's Algorithm
# Ericsson Schroeter
# Created: 4/4/18

import sys, heapq

# Class Set
class Set:
    def __init__(self, value=None):
        self._value = value

    def _getHeight(self):
        return self._height

    def _setHeight(self, height):
        self._height = height

    def _getValue(self):
        return self._value

    def _setValue(self, value):
        self._value = value

    def _getParent(self):
        return self._parent

    def _setParent(self, parent):
        self._parent = parent

    value = property(_getValue,_setValue)
    parent = property(_getParent,_setValue)
    height = property(_getHeight,_setHeight)

# makeSet(x)
def makeSet(x):
    z = Set()
    z.value = x
    z.parent = z;
    z.height = 0

# union(x,y) by height
def union(x,y):
    p = findSet(x)
    q = findSet(y)
    if(p.height > q.height):
        q.parent = p
    elif(p.height < q.height):
        p.parent = q
    else:
        q.parent = p
        p.height += 1

# findSet(x) with compression
def findSet(x):
    if(x == x.parent):
        return x
    else:
        z = findSet(x.parent)
        x.parent = z
        return z

# Begin program

filename = sys.argv[1]

with open(filename,"r") as f:
    for l in f:
        # for each line doooooooo

file.close()
