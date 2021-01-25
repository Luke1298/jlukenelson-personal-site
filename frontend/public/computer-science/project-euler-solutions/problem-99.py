import numpy as np
import math
from collections import Counter
import os
import sys
import re

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p099_base_exp.txt")

file = open(src_filename, "r")

src = file.read()


allLines = [k for k in src.split("\n")]

maxBase = max([int(line.split(",")[0]) for line in allLines])

ans = (0, 0)

for e, line in enumerate(allLines):
    if int(line.split(",")[1])*math.log(int(line.split(",")[0])) >= ans[1]:
        ans = (e, int(line.split(",")[1])*math.log(int(line.split(",")[0])))


print ans
