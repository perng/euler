def pandigital(a,b,c):
    cat = str(a)+str(b)+str(c)
    if '0' in cat or len(cat)!=9:
        return False
    return len(set([x for x in cat]))==9

s=set()
for a in range(1,100):
    for b in range(a,10000):
        c=a*b
        if pandigital(a,b,c):
            print a,b,c
            s.add(c)
print s
print sum(s)
