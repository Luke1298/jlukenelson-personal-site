
def euclidsMethod(a,b): 
    if(b==0): 
        return a 
    else: 
        return euclidsMethod(b,a%b)

tens = range(10,100)

sols = [(4, 8)]

for numerator in tens:
    for denomenator in tens:
        if numerator / denomenator < 1:
            gcd = euclidsMethod(numerator, denomenator)
            new_numerator = numerator / gcd
            new_denomenator = denomenator / gcd
            num_list = list(str(numerator))
            den_list = list(str(denomenator))
            if (str(new_numerator) in num_list) and (str(new_denomenator) in den_list):
                num_list.remove(str(new_numerator))
                den_list.remove(str(new_denomenator))
                if num_list == den_list and num_list != ["0"]:
                    print str(numerator) + " / " + str(denomenator)
                    print str(new_numerator) + " / " + str(new_denomenator)
                    sols.append((new_numerator, new_denomenator))
                
print sols

sol_num = 1
sol_den = 1

for s in sols:
    sol_num *= s[0]
    sol_den *= s[1]
    
print sol_den/euclidsMethod(sol_num, sol_den)