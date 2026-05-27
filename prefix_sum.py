def prefix(arr):
    n=len(arr)
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(n):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix

arr=list(map(int,input().split()))
print(prefix(arr))