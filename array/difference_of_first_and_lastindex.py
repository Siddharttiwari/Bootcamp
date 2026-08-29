#input=[1, 2, 3, 2, 1, 2, 1]
#output=6

def diff(arr):
    n=len(arr)
    max_diff=0
    freq={}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]]=i
        else:
            max_diff=max(max_diff,i-freq[arr[i]])
            
    return max_diff

arr=list(map(int,input().split()))
print(diff(arr))

"""
Input: arr[] = [2, 1, 3, 4, 2, 1, 5, 1, 7]
Output: 6
Explanation: For the array with 0-based indexing, 
the number 1's first appearance is at index 1 and its last appearance is at index 7. 
The gap is 7 - 1 = 6, which is the maximum gap in this array.
"""