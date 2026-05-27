#Input: arr[] = [0, 1, 2, 0, 1, 2]
#Output: [0, 0, 1, 1, 2, 2]


def sort(arr):
    n=len(arr)
    left=0
    right=n-1
    mid=0
    while mid<=right:
        if arr[mid]==0:
            arr[left],arr[mid]=arr[mid],arr[left]
            left+=1
            mid+=1

        elif arr[mid]==1:
            mid+=1
        else:
            arr[right],arr[mid]=arr[mid],arr[right]
            right-=1
    return arr

arr=list(map(int,input().split()))
print(sort(arr))