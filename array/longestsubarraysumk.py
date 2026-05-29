"""
arr=1 2 3 4 5 6 7
x=11           
output=2
"""
"""
def subarray(arr,x):
    n=len(arr)
    largest=0
    for i in range(n):
        for j in range(i+1,n):
            csum=0
            for k in range(i,j+1):
                csum+=arr[k]

            if csum==x:
                largest=max(largest,j-i+1)
    print(largest)

arr=list(map(int,input().split()))
x=int(input())
subarray(arr,x)

"""

"""
better approach
"""
"""
def subarray(arr,x):
    n=len(arr)
    largest=0
    for i in range(n):
        csum=0
        for j in range(i,n):
            csum+=arr[j]
            if csum==x:
              largest=max(largest,j-i+1)
    print(largest)

arr=list(map(int,input().split()))
x=int(input())
subarray(arr,x)

"""