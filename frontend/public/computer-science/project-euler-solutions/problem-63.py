from collections import Counter


bases = [1, 2,3,4,5,6,7,8,9]

def getNPowers(base):
    i = 1
    toReturn = []
    while len(str(base**i)) >= i:
        toReturn.append(base**i)
        i+=1
    return toReturn
answerList = []

for b in bases:
    answerList += getNPowers(b)

print(len(answerList))
