
numlist = [3]
denlist = [2]

while len(numlist) < 1000:
    numlist.append(numlist[-1] + 2*denlist[-1])
    denlist.append(numlist[-2] + denlist[-1])
    
#print numlist
sol = 0
for i in range(len(numlist)):
    if len(str(numlist[i])) > len(str(denlist[i])):
        sol += 1
        
print sol