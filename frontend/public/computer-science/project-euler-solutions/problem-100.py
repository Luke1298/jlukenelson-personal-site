import math
from tqdm import tqdm


numRed = lambda numBlue: (math.sqrt(8*numBlue*(numBlue - 1)+1) - 2*numBlue + 1)/2

xPos = [15, 85]

while xPos[-1] < 500000000000:
    xPos.append(((xPos[-1]+2) * xPos[-1])/xPos[-2])

print xPos

for x in xPos:
    print x, numRed(x), x+numRed(x) > 1000000000000
