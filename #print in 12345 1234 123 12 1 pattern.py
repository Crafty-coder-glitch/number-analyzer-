#print in 12345 1234 123 12 1 pattern
m = 12345

def nex():
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

nex()
