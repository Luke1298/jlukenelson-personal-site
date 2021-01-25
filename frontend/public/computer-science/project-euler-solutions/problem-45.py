
tri = lambda n: n*(n+1)/2
penta = lambda n: n*(3*n-1)/2
hexa = lambda n: n*(2*n-1)

ltt, lpt, lht = 286, 166, 143
#ltt, lpt, lht = 2, 2, 2
last_tri, last_penta, last_hexa  = tri(ltt), penta(lpt), hexa(lht)

while last_tri!=last_penta or last_tri!=last_hexa:
    ltt += 1
    last_tri = tri(ltt)
    if last_penta < last_tri:
        lpt += 1
        last_penta = penta(lpt)
    if last_hexa < last_tri:
        lht +=1 
        last_hexa = hexa(lht)
        
print ltt, lpt, lht
print "ANS: {}".format(last_tri)