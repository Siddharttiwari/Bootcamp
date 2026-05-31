def rotate_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
    for i in range(n):
        matrix[i].reverse()


n = int(input("Enter size of matrix: "))

matrix = []

print("Enter rows:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rotate_matrix(matrix)

print("Rotated matrix:")
for row in matrix:
    print(row)