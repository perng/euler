

def yes(n):
    return n == sum([int(i)**5 for i in str(n)])

total = 0
for i in range(2,1000000):
    if yes(i):
        print i
        total += i
        
print 'answer=',total