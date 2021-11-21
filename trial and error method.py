N1=int(input("Enter the value of coefficient of n1 "))
N2=int(input("Enter the value of coefficient of n2 "))
N=int(input("Enter the value of constant "))
for n1 in range(101):
    for n2 in range(101):
        if N1*n1+ N2*n2 == N:
            print(n1, n2)
        elif N1*n1-N2*n2 ==N:
            print (n1,n2)

