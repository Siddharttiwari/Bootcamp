def reverserow(arr,rows,cols):
    for i in range(rows):
        start=0
        end=cols-1
        while start<end:
            temp=arr[i][start]
            arr[i][start]=arr[i][end]
            arr[i][end]=temp

            start=start+1
            end=end-1

    return arr


rows=int(input())
cols=int(input())

arr=[]

for i in range(rows):
    row=list(map(int,input().split()))
    arr.append(row)

arr=reverserow(arr,rows,cols)

for i in range(rows):
    for j in range(cols):
        print(arr[i][j],end="")
    print()
