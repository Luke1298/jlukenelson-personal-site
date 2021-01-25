def is_bouncy(x):
    digits = [int(d) for d in str(x)]
    s_digist = sorted(digits)
    return digits != sorted(digits) and digits != sorted(digits)[::-1]

if __name__ == '__main__':
    nbouncy = 0
    c = 1
    while (nbouncy/c) != .99:
        nbouncy += is_bouncy(c)
        c+=1
        #We need to do c-1 since we are counting 0
        if nbouncy == 99*((c-1)-nbouncy):
            print(c-1)
    #print(c)
    #print(nbouncy)
