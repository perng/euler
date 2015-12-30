def ways(n, coins):
    return sum([ways(n-i*coins[0], coins[1:]) for i in range(n/coins[0]+1)]) if coins else 1
print ways(200, [200,100,50,20,10,5,2])