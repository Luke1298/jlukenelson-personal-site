

sol_string = " "

i=1

while len(sol_string) <= 1000000:
    sol_string += str(i)
    i+=1
    
sol = 1
for k in [10**i for i in range(7)]:
    sol *= int(sol_string[k])
      
print sol