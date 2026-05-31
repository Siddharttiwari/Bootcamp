def zero_matrix(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows=[0]*m
    cols=[0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows[i]=1
                cols[j]=1
    
    for i in range(m):
        for j in range(n):
            if rows[i]==1 or cols[j]==1:
                matrix[i][j]=0

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix row by row:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

zero_matrix(matrix)
print("Result:")
for row in matrix:
    print(row)