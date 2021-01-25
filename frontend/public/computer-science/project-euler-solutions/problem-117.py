def rgb(n):
    a = [1, 1, 2, 4]
    while len(a) < n+1:
        a.append(a[-1] + a[-2] + a[-3] + a[-4])
    return a[-1]

if __name__ == '__main__':
    #Verify
    print(rgb(5))
    #Solve
    print(rgb(50))
