

rationalExpressList = [1,2,1]

U = [2, 3, 8, 11]
L = [1, 1, 3, 4]



i = 2
while len(rationalExpressList) < 100:
    rationalExpressList += [1, 2*i, 1]
    L.append(1*L[-1] + L[-2])
    L.append(2*i*L[-1] + L[-2])
    L.append(1*L[-1] + L[-2])
    U.append(1*U[-1] + U[-2])
    U.append(2*i*U[-1] + U[-2])
    U.append(1*U[-1] + U[-2])
    i += 1

print(sum(map(int, str(U[99]))))
