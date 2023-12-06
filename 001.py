#MATRIKS
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

#Initialize matrix
matrix = []
print("Enter the entries rowwise")

#For user input
for i in range (R):             #A for loop for row(baris) entries
    a = []
    for j in range (C):         #A for loop for column(kolom) entries
        a.append(int(input()))
    matrix.append(a)
    
#for printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()