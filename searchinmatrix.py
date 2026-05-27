def search_in_matrix(arr,x):
    rows,cols=len(arr),len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==x:
                return True
            
    return False


rows=int(input())
cols=int(input())

arr=[]
for i in range(rows):
    row=list(map(int,input().split()))
    arr.append(row)

x=int(input())

if search_in_matrix(arr,x):
    print("Yes")
else:
    print("No")
