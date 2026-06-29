n=int(input())
i=n
while i>=1:
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    j=1
    while j<=2*i+1:
        print("*",end="")
        j+=1
    
    print()
    i-=1

