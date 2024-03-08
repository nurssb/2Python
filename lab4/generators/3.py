def generator1(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i

N=int(input())
a=generator1(N)
for i in a:
    print(i)
    