A=[[4,5],[6,7]]
T=[[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        T[j][i]=A[i][j]

print("Matrix Transpose:")
for i in range(2):
    for j in range(2):
        print(T[i])