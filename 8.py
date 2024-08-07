#prime number
a=int(input("enter a number"))
flag=0
if(a==1):
    print("Not a prime number")
elif (a>1):
    for i in range(2,a):
        if(a%2==0):
            flag=1
            break
if flag:
    print("Number is not prime")
else:
    print("Number is prime")        

    