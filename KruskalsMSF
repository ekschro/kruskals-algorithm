# Kruskal's Algorithm
# Ericsson Schroeter
# Created: 4/4/18

import sys, heapq, re

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
    parent = property(_getParent,_setParent)
    height = property(_getHeight,_setHeight)

# makeSet(x)
def makeSet(x):
    z = Set()
    z.value = x
    z.height = 0
    z.parent = z
    return z

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
    if(x.parent is x):
        return x
    else:
        z = findSet(x.parent)
        x.parent = z
        return z

# Begin program
# Read in input filename
filename = sys.argv[1]

# Open file
file = open(filename,"r")

# Save the value found at the first line as the number of vertices
vnum = int(file.readline())

# Initialize arrays for vertex sets, heap, and minimum spanning forest
v = []
H = []
A = []

# For each vertex create a set and add it to list v
for i in range(vnum):
    v.append(makeSet(i))

# For each line in given file: parse value into a tuple and push to min heap.
with open(filename,"r") as f:
    for l in f:
        data = re.search( r'(\d+),(\d+):(\d+)', l, re.M|re.I)
        if (data):
            heapq.heappush(H,(int(data.group(3)),int(data.group(1)),int(data.group(2))))

# While |H| > 0 and |v| > 1: pop minimum edge off heap and if the destination and
# source are not apart of the same set then add edge to minimum spanning tree and
# union the two vertices sets.
while len(H) and (len(v) > 1):
    e = heapq.heappop(H)
    if findSet(v[e[1]]) is not findSet(v[e[2]]) :
        A.append(e)
        union(v[e[1]],v[e[2]])

# For each edge in the minimum spanning tree print the source, destination:weight
for i in A:
    print(str(i[1]) + ", " + str(i[2]) + ":" + str(i[0]))

# Close open file
file.close()
