def generator(N):
    for i in range(N,0,-1):
        yield i

N=int(input())
a=generator(N)
for i in a:
    print(i)