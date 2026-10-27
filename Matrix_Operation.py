A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

# Matrix Addition
print("Matrix Addition:")
for i in range(2):
    for j in range(2):
        print(A[i][j]+B[i][j],end="")
    print()
    
#Matrix Subtraction
print("\nMatrix Subtraction:")
for i in range(2):
    for j in range(2):
        print(A[i][j]-B[i][j],end="")
    print()

#Matrix Multiplication
print("\nMatrix Multiplication:")
result=[[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j]+=A[i][k]*B[k][j]

for row in result:
    print(row)

#Matrix Transpose of Matrix A
print("\nTranspose of Matrix A:")
transpose=[]

for i in range(len(A[0])):
    row=[]
    for j in range(len(A)):
          row.append(A[j][i])
    transpose.append(row)
      
for row in transpose:
      print(row)
