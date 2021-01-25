from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy
import os
import sys

import itertools

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p107_network.txt")

file = open(src_filename, "r")

src = file.read()


def intMap(s):
    if s == "-":
        return 0
    else:
        return int(s)


numpy.set_printoptions(threshold=sys.maxsize)


X = csr_matrix([map(intMap, t.split(",")) for t in src.split("\n")[:-1]])
minTree = minimum_spanning_tree(X)


print sum(map(sum, [map(intMap, t.split(",")) for t in src.split("\n")[:-1]]))/2 - sum(sum(minTree.toarray().astype(int)))
