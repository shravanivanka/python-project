def fact(n):
    if n==0:
        return 1
    else:
        n=n*fact(n-1)
        return n
n=int(input())
i=n//2
prob=working_count=0
while i<=n:
    working_count+=int(fact(i+1)/(fact(n-i)*fact(2*i-n+1)))
    if i<n:
        prob+=int(fact(i)/(fact(n-i-1)*fact(2*i-n+1)))

    i+=1
print(str(prob)+"/"+str(working_count))