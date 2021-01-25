import math

## Could we do newtons method for integers??

def bisectsqrt(num):
    lguess = 0
    rguess = num
    guess = num
    oldDistance = float('inf')
    while True:
        oguess = guess
        if (guess**2) < num:
            guess = (lguess+rguess)//2
        else:
            guess = (rguess-lguess)//2
        if (guess**2) > num:
            rguess = guess
        else:
            lguess = guess
        distance = abs(num - guess**2)
        if oguess == guess:
            return guess
        oldDistance = distance


nums = [k for k in range(1, 100) if k not in [i**2 for i in range(1, 10)]]

print(sum([sum(map(int, str(bisectsqrt(x*(10**198))))) for x in nums]))

#def SquareRootIntegerBisection(x): #Gives 100 decimal digits
#    num = x*(10**(len(x)+1))
#    bisectsqrt
