def generator1(N):
    for i in range(N):
        if i%2==0:
            yield i

N=int(input())
a=generator1(N)
for i in a:
    print(i)
    