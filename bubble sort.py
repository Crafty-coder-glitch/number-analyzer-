x=[1,3,6,21,345,234533,2343,55692,21,355,5]
num=len(x)
for i in range(num):
    for j in range(num-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
            print(x)
            