def createMat(n):
    mat=[ [i+1]*(i+1) for i in range(n)]
    mat[n-1]= [i for i in range(n,0,-1)]
    for i in range(n-2,0,-1):
        for j in range(1,mat[i][0]):
            mat[i][j]=mat[i+1][j]+mat[i][j-1]+mat[i+1][j-1]
    return mat
def printMat(mat):
        for row in range(n):
            for col in range(mat[row][0]):
                print(mat[row][col],end=' ') 
            print()
n=int(input("Numar : "))
result=createMat(n)
printMat(result)
