def printMat(mat,n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=' ')
        print()
n=int(input('N: '))
mat=[ [i]*n if i<n-1 else [1]*n for i in range(n) ]
for i in range(n):
    mat[i][n-1]=1

for row in range(n-2,-1,-1):
    for col in range(n-2,-1,-1):
        mat[row][col]=mat[row+1][col]+mat[row][col+1]
printMat(mat,n)