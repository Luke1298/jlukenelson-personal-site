import os
import sys



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p059_cipher.txt")

file = open(src_filename, "r")

src = map(int, file.read().split(","))

def decrypt(k):
    return "".join([chr(s^k[i%3]) for i, s in enumerate(src)])


for i in range(26):
    for j in range(26):
        for k in range(26):
            key = [ord("a") + i, ord("a") + j, ord("a") + k]
            if " the " in decrypt(key):
                print sum(map(ord, decrypt(key)))
                print key
                print "".join([chr(k) for k in key])