import os
import sys



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p042_words.txt")

file = open(src_filename, "r")

src = file.read()

clean_words = lambda x: x[1:-1]

data = map(clean_words, src.split(","))

triangle_numbers = [1]
# -64 on ord, because ORD(A) == 65

sol = 0

for d in data:
    word_val = sum(ord(t)-64 for t in d)
    while word_val > triangle_numbers[-1]:
        triangle_numbers.append((len(triangle_numbers)*(len(triangle_numbers) + 1))/2)
    if word_val in triangle_numbers:
        sol+=1
        
print sol
    