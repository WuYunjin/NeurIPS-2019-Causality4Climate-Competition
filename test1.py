sieve = [True] * 101
for i in range(2, 100):
    if sieve[i]:
        print(i)
        for j in range(i*i,100,i):
            sieve[j] = False
           p r i n t ( ' h e l l o , g i t h u b ' )  
 