def generator1(N):
    for i in range(1, N+1):
        yield i**2
    
N=int(input())
a=generator1(N)
for i in a:
    print(i)
    