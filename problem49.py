from eulerlib.prime_numbers import *

def itoset(n):
    return set([x for x in str(n)])

pp = set(primes(9999))

for a in range(1000, 9801):
    #print a
    for d in range(1, (10000-a)/2+1):
        if a not in pp:
            continue
        b = a+d
        c = b+d
        if (itoset(a) == itoset(b) == itoset(c)) and b in pp and c in pp:
            print str(a)+str(b)+str(c)
            
            
print 'done'