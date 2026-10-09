"""
Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
"""
def majority(arr):
    n=len(arr)
    count=0
    el=0
    for num in arr:
        if count==0:
            count=1
            el=num
        elif el==num:
            count+=1
        else:
            count-=1
    count=arr.count(el)
    if count>(n//2):
        return el
    return -1
