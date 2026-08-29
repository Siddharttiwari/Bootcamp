def prefix(arr):
    n=len(arr)
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(n):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix

arr=list(map(int,input().split()))
print(prefix(arr))

"""
Input: arr[] = [10, 20, 10, 5, 15]
Output: [10, 30, 40, 45, 60]
Explanation: For each index i, add all the elements from 0 to i:
prefixSum[0] = 10, 
prefixSum[1] = 10 + 20 = 30, 
prefixSum[2] = 10 + 20 + 10 = 40 and so on
"""