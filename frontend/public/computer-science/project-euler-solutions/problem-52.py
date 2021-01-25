import collections

i = 1

while True:
    i += 1
    if all([collections.Counter(str(i)) == collections.Counter(str(i * t)) for t in range(1,7)]):
        print i
        break