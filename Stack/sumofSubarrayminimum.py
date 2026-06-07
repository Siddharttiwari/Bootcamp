def sumofsubarrayminimum(arr):
    ans=0
    n=len(arr)
    for i in range(n):
        minelement=arr[i]
        for j in range(i,n):
            minelement=min(minelement,arr[j])
            ans+=minelement
    return ans

arr=list(map(int,input().split()))
print(sumofsubarrayminimum(arr))