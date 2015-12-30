from operator import mul

c = ''

i=1
while len(c) < 1000000:
    c+=str(i)
    i+=1
print [int(c[10**x-1]) for x in range(7)  ]

print reduce(mul, [int(c[10**x-1]) for x in range(7)  ])
