#print in 1,12,123,1234,12345 pattern 
def nex():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end="")
        print()
        