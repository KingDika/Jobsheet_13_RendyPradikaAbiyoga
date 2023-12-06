n = int(input("Enter a number: "))
for i in range(0,n):                        # variabel i diulangi hingga n
    for j in range(0,n):                    # variabel j diulangi hingga n didalam i
        if(i==j):                           # Misal i dan j in range(0,2) maka i = 0 -> J = 0, 1, 2
            print("1",sep=" ",end=" ")      #                                    = 1 -> J = 0, 1, 2
        else:                               #                                    = 2 -> J = 0, 1, 2
            print("0",sep=" ",end=" ")
    print()
