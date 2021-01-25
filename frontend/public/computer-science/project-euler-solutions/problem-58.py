import math

def isPrime(n):
    if n == 2:
        return True 
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True
    
class Spiral():
    def __init__(self):
        self.sideLength = 1
        self.diags = [1]
        self.primesInDiag = []
    def addLayer(self):
        self.sideLength += 2
        self.diags += [self.sideLength**2 - i*(self.sideLength-1) for i in range(4)]
        self.primesInDiag += [self.sideLength**2 - i*(self.sideLength-1) for i in range(4) if isPrime(self.sideLength**2 - i*(self.sideLength-1))]
        self.ratio = len(self.primesInDiag)/float(len(self.diags)) 

spiral = Spiral()
spiral.addLayer()
spiral.addLayer()
spiral.addLayer()

while spiral.ratio > .1:
    spiral.addLayer()

print spiral.sideLength