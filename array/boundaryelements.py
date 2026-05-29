#input
'''
4 4
1 2 3 4
5 6 7 8
9 1 2 3
5 6 7 8
'''
#output
'''
1 2 3 4 
5     8 
9     3 
5 6 7 8 
'''


def boundary(arr):
    n=len(arr)
    m=len(arr[0])
    for i in range(n):
        for j in range(m):
            if i==0 or j==0 or i==m-1 or j==n-1:
                print(arr[i][j],end=" ")
            else:
                print(' ',end=" ")
        print()


m,n=map(int,input().split())
arr=[]
for i in range(m):
    row=list(map(int,input().split()))
    arr.append(row)
boundary(arr)
