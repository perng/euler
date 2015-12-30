from math import sqrt, floor
sqrt2 = sqrt(2.0)
r = 1.0/(2+sqrt2)
maxsolution = 0
maxp = 0
for p in range(10, 1001):
    n=0
    for a in range(1, int(p*r)):
        aa = a*a
        for b in range(a, int((p-a)/2)):
            c = p - a - b 
            if a<=b<c and c*c==aa +b*b:
                n+=1
                print p, a,b,c                 
    maxsolution = max(maxsolution, n)
    maxp = p if maxsolution==n else maxp
print maxsolution, maxp
                       