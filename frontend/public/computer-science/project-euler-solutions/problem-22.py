import os
import sys



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p022_names.txt")

file = open(src_filename, "r")

src = file.read()

print sum([(i+1) * sum([ord(v_k) - (ord("A")-1) for v_k in v]) for i, v in enumerate(sorted(src.replace("\"", "").split(",")))])
