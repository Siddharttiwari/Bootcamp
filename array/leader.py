#Input: arr = [16, 17, 4, 3, 5, 2]
#Output: [17, 5, 2]

def leader(arr):
    n=len(arr)
    leader=[]
    rightmax=arr[-1]
    leader.append(rightmax)
    for i in range(n-2,-1,-1):
        if arr[i]>=rightmax:
            rightmax=arr[i]
            leader.append(arr[i])
    leader.reverse()
    return leader

arr=list(map(int,input().split()))
print(leader(arr))