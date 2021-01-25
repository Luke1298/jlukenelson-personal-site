import numpy as np
import math
from collections import Counter
import os
import sys
import re

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p102_triangles.txt")

file = open(src_filename, "r")

src = file.read()


allLines = [k for k in src.split("\n")][:-1]

def hasOrigin(points):
    a = points[0]
    b = points[1]
    c = points[2]
    ZeroOnCSide = False
    if float(a[0] - b[0])!=0:
        ab = lambda x: (a[1]-b[1])/float(a[0] - b[0]) * x + (a[1] - ((a[1]-b[1])/float(a[0] - b[0]))*a[0])
        ZeroOnCSide = ((ab(c[0]) > c[1]) == (ab(0) > 0))
    else:
        ZeroOnCSide = ((c[0] > a[0]) == (0 > a[0]))

    ZeroOnBSide = False
    if float(a[0] - c[0])!=0:
        ac = lambda x: (a[1]-c[1])/float(a[0] - c[0]) * x + (a[1] - ((a[1]-c[1])/float(a[0] - c[0]))*a[0])
        ZeroOnBSide = ((ac(b[0]) > b[1]) == (ac(0) > 0))
    else:
        ZeroOnBSide = ((b[0] > a[0]) == (0 > a[0]))

    ZeroOnASide = False
    if float(b[0] - c[0])!=0:
        bc = lambda x: (b[1]-c[1])/float(b[0] - c[0]) * x + (b[1] - ((b[1]-c[1])/float(b[0] - c[0]))*b[0])
        ZeroOnASide = ((bc(a[0]) > a[1]) == (bc(0) > 0))
    else:
        ZeroOnASide = ((a[0] > b[0]) == (0 > b[0]))

    return (ZeroOnCSide and ZeroOnBSide and ZeroOnASide)

numOrginContainers = 0

for line in allLines:
    points = zip(map(int, line.split(","))[::2], map(int, line.split(","))[1::2])
    numOrginContainers += hasOrigin(points)

print numOrginContainers
