for i in range(1,6,1):
    for j in range(1,6,1):
        if (i==1 or i==5 or j==1 or j==5) and ((i*j)!=4 and (i*j)!=10):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")