n =5
for i in range(1,(n+1)//2+1):
    for j in range((n+1)//2-i):
        print(" ",end="")
    # for k in range(1+2*(i-1)):
    print("*" * (1+2*(i-1)))
    # print('\n')
for i in range(1,(n+1)//2):
    print(" " * i,end="")
    print("*" * (5-(2*i)))