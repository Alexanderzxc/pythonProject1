x=int(input())
b=x
i=2
a=[1]
s=0
d=1
while x%2==0:
    a.append(int(x/2))
    a.append(2**d)
    d+=1
    x//=2
if sum(a)==2:
    print(*a)
else:
    print(0)
#if x<10000:
#    while i <= x // 2:
#        if x % i == 0:
#            a.append(i)
#        i += 1
#while i<x and x!=1:
#    if x%i==0:
#        if i not in a:
#            a.append(i)
#        else:
#            a.append(i**d)
#            d+=1
#        a.append(int(x/i))
#        x //= i
#        i=2
#    else:
#        i+=1
#if sum(a)==b:
#    print(*a)
#else:
#    print(0)
#