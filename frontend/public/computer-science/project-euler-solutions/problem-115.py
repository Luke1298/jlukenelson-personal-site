
def F(m,n):
    a = [1]*m
    a += [2]
    while len(a) < n+1:
        a.append(2*a[-1]-a[-2]+a[-1*(m+1)])
    return a[n]

if __name__ == '__main__':
    #Verify
    print(F(3, 6))
    print(F(3, 29))
    print(F(3, 30))
    print(F(10, 56))
    print(F(10, 57))
    n = 50
    while F(50, n) < 10**6:
        n+=1
    print(n)
