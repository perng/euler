from eulerlib.prime_numbers import *

pp = primes(1000000)

longest = 0
n=0

for i in range(len(pp)):
    #print pp[i]
    for j in range(i):
        k=j
        s = pp[k]

        while k < len(pp) and s<=pp[i]:
            if s == pp[i]:
                if k-j+1> longest:
                    longest = k-j+1
                    n = pp[i]
                    print '********', n, k-j+1
                    break
        
            k += 1     
            s += pp[k]
        else:
            continue
        break

print n, longest
            
            