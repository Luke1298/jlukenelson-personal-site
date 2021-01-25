def digitSum(n):
    return sum(int(i) for i in str(n))
    
print max([digitSum(a**b) for a in range(100) for b in range(100)])