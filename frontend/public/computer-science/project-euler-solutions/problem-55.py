def reverse(n):
    return int(str(n)[::-1])

def isPalinDrome(n):
    return n[:len(n)/2] == n[(len(n)+1)/2:][::-1]
    
def isLychrel(n):
    iters = 0
    while iters < 50:
        iters += 1
        n = n + reverse(n)
        if isPalinDrome(str(n)):
            return False
    return True
    
 
print sum(isLychrel(i) for i in range(10001))